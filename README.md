# Student Grade Management System

A simple console-based Python program to manage student records and
calculate grades. Made as a project for the Python Essentials course.

## What it does
- Add a new student with roll number, name, and marks in 5 subjects
- View all students or search for one by roll number
- Update a student's marks
- Delete a student record
- View class statistics (class average, topper, grade distribution)
- Saves all data to a `students_data.json` file so records aren't lost
  when you close the program

## Python concepts used
- Variables, loops, and if/elif/else conditions
- Functions
- Lists and dictionaries
- The `array` module (marks are stored as an array, not a plain list)
- Object-Oriented Programming (the `Student` class in `student.py`)
- Splitting code into multiple files/modules and importing them
- File handling with JSON (`file_handler.py`)
- Basic exception handling (try/except) for invalid mark input

## Files
```
student-grade-manager/
├── main.py            # menu + program flow
├── student.py          # Student class
├── file_handler.py       # save/load functions
└── students_data.json      # created automatically when you save
```

## How to run
1. Make sure Python 3 is installed:
   ```
   python3 --version
   ```
2. Run the program:
   ```
   python3 main.py
   ```
3. Follow the on-screen menu (enter a number from 1 to 7).

No extra libraries need to be installed — everything used here is part
of standard Python.
