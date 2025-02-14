#!/usr/bin/python3
"""This script adds all command-line arguments to a list and saves them to a file."""

import sys
import os
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file


filename = "add_item.json"

# Si el archivo existe, cargamos la lista. Si no, usamos una lista vacía.
if os.path.exists(filename):
    my_list = load_from_json_file(filename)
else:
    my_list = []

# Agregamos los argumentos de la línea de comandos (excepto el nombre del script).
my_list.extend(sys.argv[1:])

# Guardamos la lista actualizada en el archivo JSON.
save_to_json_file(my_list, filename)
