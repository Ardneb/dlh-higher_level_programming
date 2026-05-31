#!/usr/bin/python3
"""Basic Serialization"""
import pickle


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file"""
    with open(filename, "wb") as myFile:
        pickle.dump(data, myFile)
    pass


def load_and_deserialize(filename):
    """Deserialize the JSON file to recreate the Python Dictionary"""
    with open(filename, "rb") as myFile:
        return pickle.load(myFile)
    pass
