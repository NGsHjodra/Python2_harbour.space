from flask import Flask, request, render_template

app = Flask(__name__)

def increase(value: int)->int:
    return value**2

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/test")
def test_action():
    val = request.args.get('value')
    res = increase(int(val))
    return render_template("main.html", value = res)

if __name__=='__main__':
    app.run(debug=True)

