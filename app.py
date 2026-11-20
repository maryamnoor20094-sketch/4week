from flask import Flask, request, jsonify

app = Flask(__name__)

# Day 01 - Home page
@app.route("/")
def home():
    return "Welcome to Maryam's First Python Backend Application!"

# Day 01 - About page
@app.route("/about")
def about():
    return "This is my first Flask application at Renusoft."

# Day 01 - Contact page
@app.route("/contact")
def contact():
    return "Contact page - My Flask application."

# Day 02 - GET API
@app.route("/api/student", methods=["GET"])
def get_student():
    student = {
        "name": "Maryam Noor",
        "department": "Information Technology",
        "program": "DevSecOps Internship",
        "week": 4
    }
    return jsonify(student), 200

# Day 02 - POST API
@app.route("/api/message", methods=["POST"])
def receive_message():
    data = request.get_json(silent=True) or {}

    if not isinstance(data, dict) or not data.get("message"):
        return jsonify({
            "error": "Message is required"
        }), 400

    return jsonify({
        "status": "success",
        "received_message": data["message"]
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
