from database import DatabaseManager


class StudentManager:

    def __init__(self):
        self.db = DatabaseManager()

    # 1. Add Student
    def add_student(self, student):

        if student.student_id <= 0:
            print("Student ID must be positive")
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

        self.db.add_student(student)

    # 2. View Students
    def view_students(self):
        self.db.view_students()

    # 3. Search Student
    def search_student(self, student_id):

        student = self.db.search_student(student_id)

        if student is not None:
            student.display_details()

        return student

    # 4. Update Student
    def update_student(self, student_id, field, new_value):

        if field not in ["name", "cgpa", "marks", "branch", "section"]:
            print("Invalid field")
            return

        if field in ["name", "branch", "section"]:
            if not str(new_value).strip():
                print(f"{field.capitalize()} cannot be empty")
                return

        elif field == "cgpa":
            if not 0 <= new_value <= 10:
                print("CGPA should be between 0 and 10")
                return

        elif field == "marks":
            if not 0 <= new_value <= 100:
                print("Marks should be between 0 and 100")
                return

        self.db.update_student(student_id, field, new_value)

    # 5. Delete Student
    def delete_student(self, student_id):
        self.db.delete_student(student_id)

    # 6. Close Database
    def close(self):
        self.db.close()