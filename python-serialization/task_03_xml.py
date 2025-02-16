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
