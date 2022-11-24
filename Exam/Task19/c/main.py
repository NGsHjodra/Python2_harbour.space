from flask import Flask, request, render_template

app = Flask(__name__)

sm = 0

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/test")
def test_action():
    global sm
    val = request.args.get('value')
    sm += val
    return render_template("main.html", value = sm)

if __name__=='__main__':
    app.run(debug=True)

