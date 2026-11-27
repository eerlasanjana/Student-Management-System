class Student:
    def __init__(self, student_id, name, cgpa, marks, branch, section):
        self.student_id = student_id
        self.name = name
        self.cgpa = cgpa
        self.marks = marks
        self.branch = branch
        self.section = section

    def display_details(self):
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("CGPA:", self.cgpa)
        print("Marks:", self.marks)
        print("Branch:", self.branch)
        print("Section:", self.section)