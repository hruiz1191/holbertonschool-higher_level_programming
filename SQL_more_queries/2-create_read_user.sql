-- Crear la base de datos (si no existe)
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Crear el usuario (si no existe) con contraseña
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
