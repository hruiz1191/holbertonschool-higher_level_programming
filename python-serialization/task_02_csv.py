#!/usr/bin/env python3
"""
task_02_csv.py:
Module for converting CSV data to JSON format.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file into JSON format.
    Args:
        csv_filename (str): The filename of the CSV file to read.
    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    try:
        # Leer el archivo CSV
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Convertir los datos en una lista de diccionarios
            data_list = list(csv_reader)

        # Escribir el JSON en el archivo de salida
        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data_list, json_file, indent=4)

        return True

    except (OSError, IOError) as e:
        print(f"Error reading file '{csv_filename}': {e}")
        return False
