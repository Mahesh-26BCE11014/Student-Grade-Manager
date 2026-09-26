
from array import array


class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
       
        self.marks = array('i', marks)

    def total_marks(self):
        total = 0
        for mark in self.marks:
            total = total + mark
        return total

    def average_marks(self):
        return self.total_marks() / len(self.marks)

    def get_grade(self):
        avg = self.average_marks()
        
        if avg >= 40:
            return "A+"
        elif avg >= 30:
            return "A"
        elif avg >= 25:
            return "B"
        elif avg >= 22:
            return "C"
        else:
            return "Fail"

    def to_dict(self):
       
        return {
            "roll_no": self.roll_no,
            "name": self.name,
            "marks": list(self.marks)
        }
     
    def display(self):
        print("-" * 40)
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Marks   :", list(self.marks))
        print("Total   :", self.total_marks())
        print("Average :", round(self.average_marks(), 2))
        print("Grade   :", self.get_grade())
        print("-" * 40)
