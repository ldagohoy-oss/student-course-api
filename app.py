# app.py

import os
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

courses = [
    {
        "id": 1,
        "code": "ITAS 3228",
        "name": "Web and Mobile Development",
        "description": "Introduction to web and mobile applications."
    },
    {
        "id": 2,
        "code": "ITAS 3215",
        "name": "System Integration and Architecture",
        "description": "Study of system integration and architecture."
    },
    {
        "id": 3,
        "code": "ITAS 3204",
        "name": "Database Management",
        "description": "Introduction to database management."
    },
    {
        "id": 4,
        "code": "ITAS 3230",
        "name": "Information Assurance and Security",
        "description": "Fundamentals of information security."
    },
    {
        "id": 5,
        "code": "ITAS 3242",
        "name": "Systems Analysis and Design",
        "description": "Methods of analyzing and designing systems."
    }
]


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Student Course API"
    }), 200


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "success",
        "message": "API is running"
    }), 200


@app.route("/api/courses", methods=["GET"])
def get_courses():
    return jsonify(courses), 200


@app.route("/api/courses/<int:course_id>", methods=["GET"])
def get_course(course_id):
    course = next(
        (course for course in courses if course["id"] == course_id),
        None
    )

    if course is None:
        return jsonify({
            "status": "error",
            "message": "Course not found"
        }), 404

    return jsonify(course), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
