#!/usr/bin/python3
"""Module for Student class with JSON serialization and deserialization."""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student instance.
        If attrs is a list of strings, only attributes in the list
        are included in the dictionary.
        """
        if isinstance(attrs, list) and all(
                isinstance(attr, str) for attr in attrs):
            return {
                key: getattr(self, key) for key in attrs if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        with values from the given dictionary.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
