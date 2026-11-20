from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to Maryam's First Python Backend Application!"


@app.route("/about")
def about():
    return "This is my first Flask application at Renusoft."


@app.route("/contact")
def contact():
    return "Contact page - My Flask application."


if __name__ == "__main__":
    app.run(debug=True)
