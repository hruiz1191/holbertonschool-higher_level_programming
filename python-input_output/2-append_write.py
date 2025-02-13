#!/usr/bin/python3
"""  function that appends and returns the number of characters added: """


def append_write(filename="", text=""):
    """Appends a string the number of characters added."""

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
