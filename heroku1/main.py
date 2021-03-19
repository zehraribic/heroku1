from flask import Flask, render_template 



app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/create account")
def createaccount():
    return render_template("create account.html")


if __name__ == "__main__":
    app.run()
