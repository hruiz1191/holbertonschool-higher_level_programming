#!/usr/bin/python3
"""Developing a simple API using Flask"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos en memoria (diccionario)
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
}

# RUTA PRINCIPAL "/"
@app.route("/", methods=["GET"])
def home():
    """Devuelve un mensaje de bienvenida"""
    return "Welcome to the Flask API!"

# RUTA "/data" - Devuelve una lista con los nombres de los usuarios
@app.route("/data", methods=["GET"])
def get_users():
    """Devuelve una lista de todos los nombres de usuario en la API"""
    return jsonify(list(users.keys()))  # Devuelve solo los nombres de usuario

# RUTA "/status" - Devuelve "OK"
@app.route("/status", methods=["GET"])
def status():
    """Devuelve el estado de la API"""
    return "OK"

# RUTA "/users/<username>" - Devuelve los datos de un usuario específico
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Devuelve la información del usuario si existe"""
    if username in users:
        return jsonify(users[username])  # Devuelve la información del usuario
    else:
        return jsonify({"error": "User not found"}), 404  # Devuelve un error 404

# RUTA "/add_user" - Agrega un nuevo usuario a la API (Método POST)
@app.route("/add_user", methods=["POST"])
def add_user():
    """Recibe datos JSON y agrega un nuevo usuario a la API"""
    data = request.get_json()

    # Validación: verificar si se proporciona un username
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Verificar si el usuario ya existe
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Agregar el usuario a la base de datos
    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201  # Código 201 -> Creado

# Ejecutar el servidor Flask en puerto 5000
if __name__ == "__main__":
    app.run(debug=True)
