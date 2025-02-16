#!/usr/bin/env python3
"""
task_03_xml.py:
Module for serializing and deserializing a dictionary using XML.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The filename to save the XML data.

    Returns:
        None
    """
    root = ET.Element("data")  # Crear el elemento raíz <data>

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)  # Crear subelementos con claves
        child.text = str(value)  # Convertir el valor a string

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)  # Guardar XML


def deserialize_from_xml(filename):
    """
    Deserializes an XML file into a Python dictionary.

    Args:
        filename (str): The filename containing the XML data.

    Returns:
        dict: The deserialized Python dictionary.
    """
    try:
        tree = ET.parse(filename)  # Cargar el archivo XML
        root = tree.getroot()  # Obtener el elemento raíz <data>

        # Convertir los elementos XML en un diccionario
        result_dict = {child.tag: child.text for child in root}
        return result_dict

    except (OSError, IOError, ET.ParseError) as e:
        print(f"Error loading file '{filename}': {e}")
        return None
