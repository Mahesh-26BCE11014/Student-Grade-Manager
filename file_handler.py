
import json
import os

from student import Student

DATA_FILE = "students_data.json"


def load_students():
    
    students = []

    if not os.path.exists(DATA_FILE):
        return students

    with open(DATA_FILE, "r") as data file:
        data = json.load(data file)

    for record in data:
        student = Student(record["roll_no"], record["name"], record["marks"])
        students.append(student)

    return students


def save_students(students):
    
    data = []
    for student in students:
        data.append(student.to_dict())

    with open(DATA_FILE, "w") as data file:
        json.dump(data, data file, indent=4)
