#!/usr/bin/python3
"""Pickling Custom Classes"""
import pickle


class CustomObject:
    """Custom Python class"""

    def __init__(self, name, age, is_student):
        """Initialise a Custom Object instance"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print attributes of the objects"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current instance of the object
        and save it to the provided filename
        """
        try:
            with open(filename, "wb") as myFile:
                pickle.dump(self, myFile)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of CustomObject
        from provided filename
        """
        try:
            with open(filename, "rb") as myFile:
                return pickle.load(myFile)
        except Exception:
            return None
