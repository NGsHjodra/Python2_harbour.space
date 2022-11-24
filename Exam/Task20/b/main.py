from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html")

@app.route("/test")
def test_action():
    val = request.args.get('value')
    return render_template("greeting.html", value = val)

if __name__=='__main__':
    app.run(debug=True)

