#!/usr/bin/pythom3
"""This program writes a file using python"""


def write_file(filename="", text=""):
    """Reads a text file (UTF8) and prints its content to stdout."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
