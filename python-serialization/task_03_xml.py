#!/usr/bin/python3
"""Serializing and Deserializing with XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize the dictionary into XML
    and save it to the given filename
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = value
    ET.ElementTree(root).write(filename)


def deserialize_from_xml(filename):
    """
    Read XML data from filename and
    return a deserialized Python dictionary
    """
    data = ET.parse(filename)
    root = data.getroot()
    dictionary = {}
    for child in root:
        dictionary.update({child.tag: child.text})
    return dictionary
