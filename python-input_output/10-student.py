#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """This class defines a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation of Student with public instances"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve dictionnary representation of a student instance"""
        new_dict = {}
        if attrs is None:
            return self.__dict__
        else:
            for i in self.__dict__:
                if i in attrs:
                    new_dict[i] = self.__dict__[i]
            return new_dict
