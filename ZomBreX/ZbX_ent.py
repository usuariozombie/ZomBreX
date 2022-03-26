from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/zombot")
def zombot():
    return render_template("zombot.html")

@app.route("/zombeats")
def zombeats():
    return render_template("zombeats.html")

@app.route("/crypto")
def crypto():
    return render_template("crypto.html")

if __name__ == "__main__":
    app.run(debug=True, host="", port=2052)