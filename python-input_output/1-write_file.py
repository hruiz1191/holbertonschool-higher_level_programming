#!/usr/bin/python3
"""This program writes a string to a file using Python."""


def write_file(filename="", text=""):
    """Writes a string to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
