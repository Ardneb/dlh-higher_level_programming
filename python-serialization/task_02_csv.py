#!/usr/bin/python3
"""Converting CSV Data to JSON Format"""
import csv
import json


def convert_csv_to_json(filename):
    """
    reading data from one format (CSV)
    and converting it into another format (JSON)
    using serialization techniques.
    """
    try:
        with open(filename, newline='') as csvfile:
            with open("data.json", "w") as jsonfile:
                reader = csv.DictReader(csvfile)
                data = list(reader)
                json.dump(data, jsonfile)
        return True
    except Exception:
        return False
