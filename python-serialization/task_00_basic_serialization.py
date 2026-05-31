#!usr/bin/python3
import pickle


def serialize_and_save_to_file(data, filename):
    with open(filename, mode="w") as myFile:
        pickle.dump(data, myFile)
    pass


def load_and_deserialize(filename):
    with open(filename, "rb") as myFile:
        return pickle.load(myFile)
    pass
