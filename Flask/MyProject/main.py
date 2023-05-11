from flask import Flask, url_for, request, render_template
from markupsafe import escape


app = Flask(__name__)


# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"


@app.route("/index")
@app.route("/index/<name>")
def index(name=None):
    return render_template("index.html", name=name)

@app.route("/about")
def about():
    return "Это страница о нашей компании"

@app.route("/login", methods=["GET", "POST"])
def login():
    return "Страничка входа"

@app.route("/user/<username>")
def profile(username):
    return f'<h1>{username}\'s profile<h1>'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for("profile", username='John Doe'))

