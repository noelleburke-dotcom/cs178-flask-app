# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT
#add and delete made with help from chatgpt template-> add or delete to/from database

from flask import Flask,render_template,request, redirect, url_for, flash
from dbCode import get_conn, execute_query 

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        conn= get_conn()
        cursor= conn.cursor()
        name = request.form['name']
        sql="INSERT INTO `User` (name) VALUES(%s)"
        cursor.execute(sql,(name,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Name added:", name)
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('add_user.html')

@app.route('/delete-user',methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        conn= get_conn()
        cursor= conn.cursor()
        name = request.form['name']
        sql="DELETE FROM `User` WHERE name = %s"
        cursor.execute(sql,(name))
        conn.commit()
        cursor.close()
        conn.close()
        
        flash('User deleted successfully!') 
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('delete_user.html')


@app.route('/display-users')
@app.route('/update-user/')
def display_users():
    rows = execute_query("SELECT user_id, name FROM `User`;")
    users_list = [{'user_id': row['user_id'], 'name': row['name']} for row in rows]
    return render_template('display_users.html', users=users_list)

@app.route('/user/<int:user_id>/playlist')
@app.route('/update-user/<int:user_id>/')
def user_playlist(user_id):
    user_info = execute_query("SELECT name FROM User WHERE user_id=%s", (user_id,))
    if not user_info:
        return "User not found", 404

    user_name = user_info[0]['name'] 

    playlist_rows = execute_query("""
        SELECT Song.title, Artist.name AS artist
        FROM Playlist
        JOIN PlaylistSong ON Playlist.playlist_id = PlaylistSong.playlist_id
        JOIN Song ON PlaylistSong.song_id = Song.song_id
        JOIN Artist ON Song.artist_id = Artist.artist_id
        WHERE Playlist.user_id = %s
        ORDER BY PlaylistSong.position
    """, (user_id,))

    playlist = [(row['title'], row['artist']) for row in playlist_rows]
    return render_template('user_playlist.html', user_name=user_name, playlist=playlist) 
    

@app.route('/update-user')
def update_user():
    rows = execute_query("SELECT user_id, name FROM `User`;")
    users_list = [{'user_id': row['user_id'], 'name': row['name']} for row in rows]

    return render_template('update_user.html', users=users_list)

@app.route('/update-user/<int:user_id>/edit', methods=['GET', 'POST'])
def update_playlist(user_id):
    user= execute_query(f"SELECT * FROM `User` WHERE user_id = {user_id};")[0]
    if request.method == 'POST':
        action = request.form.get('action')
        song_id = request.form.get('song_id')
        conn = get_conn()
        cursor = conn.cursor()
        if action == 'add': #add here
       
            cursor.execute("""
            INSERT INTO PlaylistSong (playlist_id, song_id, position)
            SELECT playlist_id, %s, IFNULL(MAX(position)+1,1)
            FROM Playlist
            WHERE user_id=%s
            """, (song_id, user_id))
        
        elif action == 'delete': #delete here
            cursor.execute("""
            DELETE FROM PlaylistSong
            WHERE playlist_id = (SELECT playlist_id FROM Playlist WHERE user_id=%s)
            AND song_id = %s
            """, (user_id, song_id))
        
        conn.commit()
        cursor.close()
        conn.close()
#update here 
        playlist_rows = execute_query("""
        SELECT Song.song_id, Song.title, Artist.name AS artist
        FROM Playlist
        JOIN PlaylistSong ON Playlist.playlist_id = PlaylistSong.playlist_id
        JOIN Song ON PlaylistSong.song_id = Song.song_id
        JOIN Artist ON Song.artist_id = Artist.artist_id
        WHERE Playlist.user_id = %s
        ORDER BY PlaylistSong.position
    """, (user_id,))
    playlist = [{'song_id': r['song_id'], 'title': r['title'], 'artist': r['artist']} for r in playlist_rows]
#show all here
    all_songs = execute_query("""
        SELECT Song.song_id, Song.title, Artist.name AS artist
        FROM Song
        JOIN Artist ON Song.artist_id = Artist.artist_id
        ORDER BY Song.title
    """)

    return render_template('update_user.html', user=user, playlist=playlist, all_songs=all_songs)

# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
