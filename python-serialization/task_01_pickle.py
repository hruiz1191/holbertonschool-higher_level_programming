#!/usr/bin/env python3
"""
task_01_pickle.py:
Module to serialize and deserialize a custom object using pickle.
"""

import pickle


class CustomObject:
    """
    A class representing a custom object with serialization
    and deserialization using the pickle module.
    """

    def __init__(self, name, age, is_student):
        """
        Initializes a CustomObject instance.
        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            is_student (bool): Whether the person is a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints the attributes of the object in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the object and saves it to a file.

        Args:
            filename (str): The filename to store the serialized object.
        Returns:
            None
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except (OSError, IOError) as e:
            print(f"Error saving file: {e}")

    @classmethod
    def deserialize(cls, filename):
        """
        Loads a serialized object from a file.

        Args:
            filename (str): The filename containing the serialized object.
        Returns:
            CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (OSError, IOError, pickle.PickleError) as e:
            print(f"Error loading file: {e}")
            return None
