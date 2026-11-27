import sqlite3
from student import Student


class DatabaseManager:

    def __init__(self):
        self.connection = sqlite3.connect("students.db")
        self.cursor = self.connection.cursor()

        self.create_table()

    # 1. Create Student Table
    def create_table(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                cgpa REAL NOT NULL,
                marks INTEGER NOT NULL,
                branch TEXT NOT NULL,
                section TEXT NOT NULL
            )
        """)

        self.connection.commit()

        print("Database connected successfully!")
        print("Student table created successfully!")

    # 2. Add Student
    def add_student(self, student):

        try:
            self.cursor.execute("""
                INSERT INTO students
                (student_id, name, cgpa, marks, branch, section)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                student.student_id,
                student.name,
                student.cgpa,
                student.marks,
                student.branch,
                student.section
            ))

            self.connection.commit()

            print("Student added successfully!")

        except sqlite3.IntegrityError:
            print("Student ID already exists!")

        except sqlite3.Error as e:
            print("Database error:", e)

    # 3. View All Students
    def view_students(self):

        try:
            self.cursor.execute("SELECT * FROM students")

            students = self.cursor.fetchall()

            if not students:
                print("No students found")
                return

            for student in students:

                print("----------------------")
                print("Student ID:", student[0])
                print("Name:", student[1])
                print("CGPA:", student[2])
                print("Marks:", student[3])
                print("Branch:", student[4])
                print("Section:", student[5])
                print("----------------------")

        except sqlite3.Error as e:
            print("Database error:", e)

    # 4. Search Student
    def search_student(self, student_id):

        try:
            self.cursor.execute("""
                SELECT * FROM students
                WHERE student_id = ?
            """, (student_id,))

            student = self.cursor.fetchone()

            if student is None:
                print("Student not found")
                return None

            print("Student found!")

            return Student(
                student[0],
                student[1],
                student[2],
                student[3],
                student[4],
                student[5]
            )

        except sqlite3.Error as e:
            print("Database error:", e)
            return None

    # 5. Update Student
    def update_student(self, student_id, field, new_value):

        allowed_fields = [
            "name",
            "cgpa",
            "marks",
            "branch",
            "section"
        ]

        if field not in allowed_fields:
            print("Invalid field")
            return

        try:
            query = f"""
                UPDATE students
                SET {field} = ?
                WHERE student_id = ?
            """

            self.cursor.execute(query, (new_value, student_id))

            self.connection.commit()

            if self.cursor.rowcount == 0:
                print("Student ID not found")
            else:
                print("Student updated successfully!")

        except sqlite3.Error as e:
            print("Database error:", e)

    # 6. Delete Student
    def delete_student(self, student_id):

        try:
            self.cursor.execute("""
                DELETE FROM students
                WHERE student_id = ?
            """, (student_id,))

            self.connection.commit()

            if self.cursor.rowcount == 0:
                print("Student ID not found")
            else:
                print("Student deleted successfully!")

        except sqlite3.Error as e:
            print("Database error:", e)

    # 7. Close Database Connection
    def close(self):

        self.connection.close()
        print("Database connection closed!")


# Testing
if __name__ == "__main__":

    db = DatabaseManager()

    try:
        db.view_students()

    finally:
        db.close()