from flask import Flask, render_template
from app import create_app

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


app = create_app()

if __name__ == '__main__':
    app.run(host='localhost', debug=True)

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=5000)