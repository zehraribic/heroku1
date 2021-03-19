from flask import Flask, render_template 



app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/prijava")
def prijava():
    return render_template("prijava.html")


if __name__ == "__main__":
    app.run()
