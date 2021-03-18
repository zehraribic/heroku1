from flask import Flask, render_template, url_for
import random
from models import User, db


app = Flask(__name__)
db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run()