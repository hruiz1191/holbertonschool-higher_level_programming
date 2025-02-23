#!/usr/bin/env python3
"""
Flask API with Basic and JWT Authentication
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Configuración de la clave secreta para JWT
app.config["JWT_SECRET_KEY"] = "supersecretkey"
jwt = JWTManager(app)

auth = HTTPBasicAuth()

# Base de datos en memoria con usuarios
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Verifica que el usuario y contraseña sean correctos.
    """
    if username in users and check_password_hash(users[username]["password"], password):
        return username
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Ruta protegida con autenticación básica.
    """
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


@app.route("/login", methods=["POST"])
def login():
    """
    Ruta para autenticar usuario y generar un token JWT.
    """
    data = request.get_json()

    if not data or "username" not in data or "password" not in data:
        return jsonify({"error": "Missing credentials"}), 400

    username = data["username"]
    password = data["password"]

    if username not in users or not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity={"username": username, "role": users[username]["role"]}
    )
    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    Ruta protegida con JWT.
    """
    return jsonify({"message": "JWT Auth: Access Granted"}), 200


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Ruta accesible solo para administradores.
    """
    current_user = get_jwt_identity()

    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({"message": "Admin Access: Granted"}), 200


# Manejo de errores para JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Manejo de error para token no autorizado.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Manejo de error para token inválido.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Manejo de error para token expirado.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Manejo de error para token revocado.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Manejo de error para tokens que requieren ser frescos.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run(debug=True)
