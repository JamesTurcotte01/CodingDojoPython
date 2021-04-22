from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL
app = Flask(__name__)

@app.route("/users")
def index():
    mysql = connectToMySQL('users_schema')
    users = mysql.query_db('SELECT * FROM users;')
    print(users)
    return render_template("readall.html", users=users)

@app.route("/create")
def display():
    return render_template("create.html")

@app.route("/users/new", methods=['POST'])
def new():
    mysql = connectToMySQL('users_schema')
    query = "INSERT INTO users(First_Name, Last_Name, Email, Created_at, Updated_at) VALUES (%(First_Name)s, %(Last_Name)s, %(Email)s, NOW(), NOW());"
    data = {
        "First_Name": request.form["First_Name"],
        "Last_Name": request.form["Last_Name"],
        "Email": request.form["Email"],
    }
    user_id=mysql.query_db(query,data)
    print("user", user_id)
    return redirect(f"/show/{user_id}")

@app.route("/show/<user_id>")
def show(user_id):
    mysql = connectToMySQL("users_schema")
    query = "SELECT * FROM users WHERE id = (%(id)s);"
    data = {
        "id": user_id
    }
    user=mysql.query_db(query,data)
    print(user)
    return render_template("ReadOne.html", one_user=user)

@app.route("/edit/<user_id>")
def edit_user(user_id):
    mysql = connectToMySQL("users_schema")
    query = "SELECT * FROM users WHERE id = (%(id)s);"
    data = {
        "id": user_id
    }
    user=mysql.query_db(query,data)
    print(user)
    return render_template("edit.html", one_user=user)

@app.route("/edit/<user_id>", methods=['POST'])
def edit(user_id):
    mysql= connectToMySQL("users_schema")
    query= "UPDATE users SET First_Name = %(First_Name)s, last_name=%(Last_Name)s, email = %(Email)s, created_at =NOW(), updated_at=NOW() WHERE id= %(id)s;"
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email" : request.form["email"],
        "id": user_id
    }
    user=mysql.query_db(query,data)
    print(user)
    return redirect(f'/show/{user_id}')

@app.route("/delete/<user_id>")
def delete(user_id):
    mysql = connectToMySQL("users_schema")
    query = "DELETE FROM users WHERE id = (%(id)s);"
    data = {
        "id": user_id
    }
    new_user_id=mysql.query_db(query,data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)