from flask import *
import sqlite3


app=Flask(__name__)



@app.route('/')
def login():
    return render_template("login.html")

@app.route('/register')
def register():
    return render_template("register.html")

@app.route('/home')
def home():
    return render_template("home.html")

@app.route("/registeruser", methods=['POST','GET'])
def my_regiser_user():
    entered_username = request.form.get("username")
    entered_companyname = request.form.get("companyname")
    entered_email = request.form.get("email")
    entered_password = request.form.get("password")
    entered_password = entered_password.lower()



    print(entered_username, entered_companyname, entered_email, entered_password)

    con = sqlite3.connect("my_database1.sqlite3")

    cur = con.cursor()

    my_table_query = "create table if not exists userstable(name varchar(20),company name varchar(20),email varchar(30),password varchar(10))"
    cur.execute(my_table_query)

    cur.execute(f"select email from userstable where email='{entered_email}'")
    result = cur.fetchone()
    if result != None:
        return "Email Already Exists....Try again"
    else:
        my_insert_query = f"insert into userstable values('{entered_username}','{entered_companyname}','{entered_email}','{entered_password}')"
        cur.execute(my_insert_query)
        con.commit()
        return "User Registered Successfully"

@app.route("/loginuser", methods=['POST','GET'])
def my_login():
    entered_username = request.form.get("username")
    entered_password = request.form.get("password")
    con = sqlite3.connect("my_database1.sqlite3")
    cur = con.cursor()
    cur.execute(f"select * from userstable where name='{entered_username}' and password='{entered_password}'")

    result = cur.fetchone()
    if result is None:
        return "Invalid User Credentials....try again"
    else:
        return render_template('home.html')



if __name__=="__main__":
    app.run(debug=True)