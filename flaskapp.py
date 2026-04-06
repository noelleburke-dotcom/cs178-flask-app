# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT
#add and delete made with help from chatgpt template-> add or delete to/from database

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *

app = Flask(__name__)
app.secret_key = 'your_secret_key' # this is an artifact for using flash displays; 
                                   # it is required, but you can leave this alone

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Extract form data 
        cursor= connection.cursor()
        name = request.form['name']
        sql="INSERT INTO USERS (name) VALUES(%s)"
        cursor.execute(sql,(name,))
        connection.commit()
        cursor.close()
        print("Name:", name)
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('add_user.html')

@app.route('/delete-user',methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        # Extract form data
        cursor= connection.cursor()
        name = request.form['name']
        sql="DELETE FROM Users WHERE user_id = %s"
        cursor.execute(sql,(user_id,))
        connection.commit
        cursor.close()
        print("Name to delete:", name)
        
        flash('User deleted successfully! Hoorah!', 'warning') 
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('delete_user.html')


@app.route('/display-users')
def display_users():
    # hard code a value to the users_list;
    # note that this could have been a result from an SQL query :) 
    users_list = (('John','Doe','Comedy'),('Jane', 'Doe','Drama'))
    return render_template('display_users.html', users = users_list)

@app.route('/update-user')
def update_user(user_id):
    rows = execute_query("""
    SELECT Track.Name
    FROM Playlist
    JOIN PlaylistTrack USING (PlaylistId)
    JOIN Track USING (TrackId)
    WHERE Playlist.UserId = %s
""", (user_id,))
    return render_template('update_user.html', tracks=rows)

# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
