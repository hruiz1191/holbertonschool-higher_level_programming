#!/usr/bin/python3
"""Script that adds command-line arguments to a list
and saves them to a file.
"""


import sys
import os

# Importamos usando __import__() para evitar problemas con nombres numéricos.
save_to_json_file = __import__(
    "5-save_to_json_file"
).save_to_json_file
load_from_json_file = __import__(
    "6-load_from_json_file"
).load_from_json_file

filename = "add_item.json"

# Si el archivo existe, lo cargamos; si no, usamos una lista vacía.
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Agregamos los argumentos de la línea de comandos (excepto el nombre del script).
my_list.extend(sys.argv[1:])

# Guardamos la lista actualizada en el archivo JSON.
save_to_json_file(my_list, filename)
