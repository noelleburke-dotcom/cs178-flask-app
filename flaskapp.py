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
        sql="INSERT INTO USERS (name) VALUES(%s)"
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
        sql="DELETE FROM Users WHERE name = %s"
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
def display_users():
    rows = execute_query("SELECT user_id, name FROM `User`;")
    users_list = [{'user_id': row[0], 'name': row[1]} for row in rows]
    return render_template('display_users.html', users=users_list)


@app.route('/update-user/<int:user_id>')
def update_user(user_id):
    rows = execute_query("SELECT user_id, name FROM User WHERE user_id = %s", (user_id,))
    if not rows:
        return "User not found", 404

    user = rows[0]  
    return render_template('update_user.html', user=user)

# these two lines of code should always be the last in the file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
