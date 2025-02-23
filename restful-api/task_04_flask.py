#!/usr/bin/python3
from flask import Flask, jsonify, request

# Inicializa la aplicación Flask
app = Flask(__name__)

# Base de datos en memoria (diccionario)
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
}

# Ruta raíz "/"
@app.route("/", methods=["GET"])
def home():
    """Devuelve un mensaje de bienvenida"""
    return "Welcome to the Flask API!"

# Ruta "/data" - Devuelve la lista de usuarios
@app.route("/data", methods=["GET"])
def get_users():
    """Devuelve una lista con todos los nombres de usuario"""
    return jsonify(list(users.keys()))

# Ruta "/status" - Devuelve "OK"
@app.route("/status", methods=["GET"])
def status():
    """Devuelve el estado de la API"""
    return "OK"

# Ruta "/users/<username>" - Obtiene información de un usuario
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """Devuelve la información del usuario si existe"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Ruta "/add_user" - Agregar un nuevo usuario con método POST
@app.route("/add_user", methods=["POST"])
def add_user():
    """Agrega un nuevo usuario a la base de datos"""
    new_user = request.json  # Obtiene el JSON enviado en la solicitud
    username = new_user.get("username")

    # Validar si se envió un username
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Verificar si el usuario ya existe
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Agregar el nuevo usuario
    users[username] = new_user

    return jsonify({"message": "User added", "user": new_user}), 201

# Iniciar el servidor Flask en el puerto 5000
if __name__ == "__main__":
    app.run(debug=True)

