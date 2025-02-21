#!/usr/bin/python3
"""Developing a Simple API using Python with Flask"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Users dictionary to store user data in memory
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    """Root endpoint"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    """Return a list of all usernames"""
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    """Return API status"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Return user details if user exists, else return error message"""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Handle POST request to add a new user"""
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True)
