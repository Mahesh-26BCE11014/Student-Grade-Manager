"""
main.py

Student Grade Management System
--------------------------------
A simple console program to add students, record their marks,
and view grades/statistics for the whole class.

Run with: python main.py
"""

from student import Student
import file_handler

# load existing data (if any) when the program starts
students = file_handler.load_students()


def find_student(roll_no):
    """Loops through the students list and returns the matching one,
    or None if not found. Basic control flow + functions."""
    for s in students:
        if s.roll_no == roll_no:
            return s
    return None


def add_student():
    roll_no = input("Enter roll number: ")

    if find_student(roll_no) is not None:
        print("A student with this roll number already exists!")
        return

    name = input("Enter student name: ")

    marks = []
    print("Enter marks for 4 subjects:")
    for i in range(1, 5):
        while True:
            try:
                mark = int(input(f"  Subject {i}: "))
                if mark < 0 or mark > 50:
                    print("  Marks should be between 0 and 50.")
                    continue
                marks.append(mark)
                break
            except ValueError:
                print("  Please enter a valid whole number.")

    new_student = Student(roll_no, name, marks)
    students.append(new_student)
    print("Student added successfully!\n")


def view_all_students():
    if len(students) == 0:
        print("No student records found.\n")
        return

    for s in students:
        s.display()


def view_one_student():
    roll_no = input("Enter roll number to search: ")
    s = find_student(roll_no)

    if s is None:
        print("No student found with that roll number.\n")
    else:
        s.display()


def update_marks():
    roll_no = input("Enter roll number to update: ")
    s = find_student(roll_no)

    if s is None:
        print("No student found with that roll number.\n")
        return

    new_marks = []
    print("Enter new marks for 4 subjects:")
    for i in range(1, 5):
        while True:
            try:
                mark = int(input(f"  Subject {i}: "))
                new_marks.append(mark)
                break
            except ValueError:
                print("  Please enter a valid whole number.")

    from array import array
    s.marks = array('i', new_marks)
    print("Marks updated successfully!\n")


def delete_student():
    roll_no = input("Enter roll number to delete: ")
    s = find_student(roll_no)

    if s is None:
        print("No student found with that roll number.\n")
        return

    students.remove(s)
    print("Student record deleted.\n")


def class_statistics():
    """Calculates the class average and finds the topper.
    Shows use of loops + basic data structures (list, dict)."""
    if len(students) == 0:
        print("No student records to calculate statistics.\n")
        return

    total_of_all = 0
    topper = students[0]
    grade_count = {"A+": 0, "A": 0, "B": 0, "C": 0, "Fail": 0}

    for s in students:
        total_of_all += s.average_marks()
        if s.average_marks() > topper.average_marks():
            topper = s
        grade_count[s.get_grade()] += 1

    class_average = total_of_all / len(students)

    print("-" * 40)
    print("CLASS STATISTICS")
    print("Number of students :", len(students))
    print("Class average      :", round(class_average, 2))
    print("Topper              :", topper.name, f"({topper.roll_no})")
    print("Grade distribution  :", grade_count)
    print("-" * 40)


def show_menu():
    print("\n===== STUDENT GRADE MANAGEMENT SYSTEM =====")
    print("1. Add a new student")
    print("2. View all students")
    print("3. View one student")
    print("4. Update a student's marks")
    print("5. Delete a student")
    print("6. View class statistics")
    print("7. Save and exit")
    print("=============================================")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all_students()
        elif choice == "3":
            view_one_student()
        elif choice == "4":
            update_marks()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            class_statistics()
        elif choice == "7":
            file_handler.save_students(students)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 7.\n")


if __name__ == "__main__":
    main()
