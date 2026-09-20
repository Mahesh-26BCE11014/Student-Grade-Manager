"""
file_handler.py

Functions to save and load student records using a JSON file.
This is our "Modules and Packages" part of the project - this file
is imported into main.py just like we learned in Module 10.
"""

import json
import os

from student import Student

DATA_FILE = "students_data.json"


def load_students():
    """Reads the JSON file and returns a list of Student objects.
    If the file doesn't exist yet, just returns an empty list."""
    students = []

    if not os.path.exists(DATA_FILE):
        return students

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    for record in data:
        s = Student(record["roll_no"], record["name"], record["marks"])
        students.append(s)

    return students


def save_students(students):
    """Converts every Student object back to a dictionary and writes
    the whole list to the JSON file."""
    data = []
    for s in students:
        data.append(s.to_dict())

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
