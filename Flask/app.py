from flask import jsonify, request, Flask, render_template
from markupsafe import escape
from Functions import factorial

app = Flask(__name__)

data = {}
f = open("secretdata.txt", "r")
for line in f:
    user,pw = line.split(":")
    data[user] = pw

@app.route("/check_login/json")
def check_login_json():
    username = request.args.get('username', type=str)
    password = request.args.get('password', type=str)    
    return jsonify({'authourized': password == data[username]})

@app.route("/check_login")
def check_login():
    username = request.args.get('username', type=str)
    password = request.args.get('password', type=str)    
    if password != data[username]:
        return f"Incorrect username/password, <b>{escape(username)}!</b>"
    return f"Welcome, <b>{escape(username)}!</b>"

@app.route("/fac4now")
def fac4now():
    a = request.args.get('a', type=int)   
    return jsonify({'fac': factorial(a)})

@app.route("/add")
def add():
    a = request.args.get('a', type=float)  
    b = request.args.get('b', type=float)  
    return jsonify({'ans': a+b})

@app.route("/test-number")
def test_number_action(num:int):
    if num >= 0:
        return f"{escape(num)} is ok"

@app.route("/login")
def loginpage():
    return render_template('login.html')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"