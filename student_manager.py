from student import Student


class StudentManager:

    def __init__(self):
        self.students = []

    # Add Student
    def add_student(self, student):

        if student.student_id <= 0:
            print("Student ID must be positive")
            return

        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                print("Student ID already exists")
                return

        if not student.name.strip():
            print("Name cannot be empty")
            return

        if not 0 <= student.cgpa <= 10:
            print("CGPA should be between 0 and 10")
            return

        if not 0 <= student.marks <= 100:
            print("Marks should be between 0 and 100")
            return

        if not student.branch.strip() or not student.section.strip():
            print("Branch and section cannot be empty")
            return

        self.students.append(student)
        print("Student added successfully")

    # View Students
    def view_students(self):

        if not self.students:
            print("No students found")
            return

        for student in self.students:
            print("----------------------")
            student.display_details()
            print("----------------------")

    # Search Student
    def search_student(self, student_id):

        for student in self.students:
            if student.student_id == student_id:
                print("Student found!")
                student.display_details()
                return student

        print("Student not found")
        return None

    # Update Student
    def update_student(self, student_id, field, new_value):

        for student in self.students:

            if student.student_id == student_id:

                if field == "name":
                    if not str(new_value).strip():
                        print("Name cannot be empty")
                        return
                    student.name = new_value

                elif field == "cgpa":
                    if not 0 <= new_value <= 10:
                        print("CGPA should be between 0 and 10")
                        return
                    student.cgpa = new_value

                elif field == "marks":
                    if not 0 <= new_value <= 100:
                        print("Marks should be between 0 and 100")
                        return
                    student.marks = new_value

                elif field == "branch":
                    if not str(new_value).strip():
                        print("Branch cannot be empty")
                        return
                    student.branch = new_value

                elif field == "section":
                    if not str(new_value).strip():
                        print("Section cannot be empty")
                        return
                    student.section = new_value

                else:
                    print("Invalid field")
                    return

                print("Student updated successfully")
                return

        print("Student ID not found")

    # Delete Student
    def delete_student(self, student_id):

        for student in self.students:

            if student.student_id == student_id:
                self.students.remove(student)
                print("Student deleted successfully")
                return

        print("Student ID not found")