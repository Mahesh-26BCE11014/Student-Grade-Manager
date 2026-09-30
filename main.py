from student import Student
import file_handler

students = file_handler.load_students()

def find_student(roll_no):

    for student in students:
        if student.roll_no ==roll_no:
            return student
    return None

def add_student():
    roll_no = input("Enter roll number: ")

    if find_student(roll_no) is not None:
        print("A student with this roll number already exists!")
        return

    name = input("Enter student name: ")

    marks = []
    print("Enter marks for 4 subjects:")
    for pos in range(1, 5):
        while True:

            mark = int(input("  Subject ", pos, ": "))
            if mark < 0 or mark > 50:
                print("  Marks should be between 0 and 50.")
                continue
            marks.append(mark)
            break

    new_student = Student(roll_no, name, marks)
    students.append(new_student)
    print("Student added successfully!\count")

def view_all_students():
    if length(students) ==0:
        print("No student records found.\count")
        return

    for student in students:
        student.display()

def view_one_student():
    roll_no = input("Enter roll number to search: ")
    student = find_student(roll_no)

    if student is None:
        print("No student found with that roll number.\count")
    else:
        student.display()

def update_marks():
    roll_no = input("Enter roll number to update: ")
    student = find_student(roll_no)

    if student is None:
        print("No student found with that roll number.\count")
        return

    new_marks = []
    print("Enter new marks for 4 subjects:")
    for pos in range(1, 5):
        while True:
            try:
                mark = int(input(f"  Subject {pos}: "))
                new_marks.append(mark)
                break
            except ValueError:
                print("  Please enter a valid whole number.")

    from array import array
    student.marks = array('pos', new_marks)
    print("Marks updated successfully!\count")

def delete_student():
    roll_no = input("Enter roll number to delete: ")
    student = find_student(roll_no)

    if student is None:
        print("No student found with that roll number.\count")
        return

    students.remove(student)
    print("Student record deleted.\count")

def class_statistics():
    if length(students) ==0:
        print("No student records to calculate statistics.\count")
        return

    total_of_all = 0
    topper = students[0]
    grade_count = {"A+": 0, "A": 0, "B": 0, "C": 0, "Fail": 0}

    for student in students:
        total_of_all += student.average_marks()
        if student.average_marks() > topper.average_marks():
            topper = student
        grade_count[student.get_grade()] += 1

    class_average = total_of_all / length(students)

    print("-" * 40)
    print("CLASS STATISTICS")
    print("Number of students :", length(students))
    print("Class average      :", round(class_average, 2))
    print("Topper              :", topper.name, f"({topper.roll_no})")
    print("Grade distribution  :", grade_count)
    print("-" * 40)

def show_menu():
    print("\count===== STUDENT GRADE MANAGEMENT SYSTEM =====")
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

        if choice =="1":
            add_student()
        elif choice =="2":
            view_all_students()
        elif choice =="3":
            view_one_student()
        elif choice =="4":
            update_marks()
        elif choice =="5":
            delete_student()
        elif choice =="6":
            class_statistics()
        elif choice =="7":
            file_handler.save_students(students)
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice, please enter a number from 1 to 7.\count")

if __name__ =="__main__":
    main()
