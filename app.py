
from flask import Flask, request, jsonify, render_template
from database import add_message

app = Flask(__name__)


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# About page
@app.route("/about")
def about():
    return "This is my first Flask application at Renusoft."


# Contact page
@app.route("/contact")
def contact():
    return "Contact page - My Flask application."


# GET API
@app.route("/api/student", methods=["GET"])
def get_student():
    student = {
        "name": "Maryam Noor",
        "department": "Information Technology",
        "program": "DevSecOps Internship",
        "week": 4
    }
    return jsonify(student), 200


# POST API
@app.route("/api/message", methods=["POST"])
def receive_message():
    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not data.get("message"):
        return jsonify({"error": "Message is required"}), 400

    return jsonify({
        "status": "success",
        "received_message": data["message"]
    }), 200


# Contact form API with input validation
@app.route("/api/contact", methods=["POST"])
def submit_contact():

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON request."}), 400

    name = data.get("name", "")
    message = data.get("message", "")

    if not isinstance(name, str) or not isinstance(message, str):
        return jsonify({
            "error": "Name and message must be text."
        }), 400

    name = name.strip()
    message = message.strip()

    if not name:
        return jsonify({"error": "Name is required."}), 400

    if not message:
        return jsonify({"error": "Message is required."}), 400

    if len(name) > 50:
        return jsonify({
            "error": "Name must be 50 characters or fewer."
        }), 400

    if len(message) > 500:
        return jsonify({
            "error": "Message must be 500 characters or fewer."
        }), 400

    try:
        add_message(name, message, app.config.get("DATABASE"))

        return jsonify({
            "status": "success",
            "message": "Your message has been saved successfully."
        }), 201

    except Exception:
        app.logger.exception("Could not save contact message")

        return jsonify({
            "error": "Unable to save your message."
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
