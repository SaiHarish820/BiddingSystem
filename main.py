from flask import *
import pymongo
from urllib.parse import quote_plus
import pprint
from User.modules import User
app=Flask(__name__)

username = quote_plus('vinay_ch')
password = quote_plus('test@123')

url = 'mongodb+srv://' + username + ':' + password + '@vinnu.vyjljja.mongodb.net/?retryWrites=true&w=majority'
client = pymongo.MongoClient(url, serverSelectionTimeoutMS=5000)
db = client['BroBid']
col = db.users

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/logreg')
def register():
    return render_template("logreg.html")

@app.route("/logreg", methods=['POST'])
def my_regiser_user():
    
    col.insert_one(User().register())
    return "Successfully regestered User"

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def log():
    user_log = {
            "username": request.form.get('lun'),
            "password": request.form.get('lpd')
        }
    #name= user_log["username"]
    v=(col.find_one({"username": "vinay"}))
    print(v['Password'])
    print(user_log['password'])
    print(user_log)
    if(v['Password']==user_log['password']):
        return "credentials are correct"
    else:
        return "credentials are wrong"    


if __name__=="__main__":
    app.run(debug=True)