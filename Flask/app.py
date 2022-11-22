from flask import jsonify, request, Flask, render_template
from markupsafe import escape
from Functions import factorial
import json

app = Flask(__name__)

sc_file = open('secret.json', 'r')
secret_data = json.load(sc_file)['user']
    
def isourcustomer(username : str,password : str)->bool: 
    for i,data in enumerate(secret_data):
        if data["username"]==username and data["password"]==password:
            return True
    return False
#stioarnstst
@app.route("/login/json")
def check_login_json():
    username = request.args.get('username', type=str)
    password = request.args.get('password', type=str)
    for data in secret_data:
        if data["username"]==username and data["password"]==password:
            return render_template('facpage.html', name = data['name'], reveal = True)
    return render_template('facpage.html', name = username, reveal = False)

@app.route("/login/fac")
def loginfac():
    num = request.args.get('num', type=int)
    return render_template('facpage.html', fac = factorial(num), reveal = True)

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