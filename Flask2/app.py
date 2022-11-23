from flask import jsonify, request, Flask, render_template

app = Flask(__name__)

def factorial(n: int)->int:
    if n == 0:
        return 1
    else:
        return factorial(n-1)*n

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/test-number")
def test_number_action():
    val = request.args.get('value')
    fac = factorial(int(val))
    return {"result" : fac}