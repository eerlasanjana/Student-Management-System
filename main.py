from student import Student
from student_manager import StudentManager


manager = StudentManager()

try:

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))

        except ValueError:
            print("Please enter a valid number")
            continue

        # 1. Add Student
        if choice == 1:

            try:
                student_id = int(input("Enter Student ID: "))
                name = input("Enter Name: ").strip()
                cgpa = float(input("Enter CGPA: "))
                marks = int(input("Enter Marks: "))
                branch = input("Enter Branch: ").strip()
                section = input("Enter Section: ").strip()

                student = Student(
                    student_id, name, cgpa, marks, branch, section
                )

                manager.add_student(student)

            except ValueError:
                print("Invalid input. Please enter the correct values.")

        # 2. View Students
        elif choice == 2:
            manager.view_students()

        # 3. Search Student
        elif choice == 3:

            try:
                student_id = int(input("Enter Student ID: "))
                manager.search_student(student_id)

            except ValueError:
                print("Please enter a valid student ID")

        # 4. Update Student
        elif choice == 4:

            try:
                student_id = int(input("Enter Student ID: "))

                print("\n1. Update Name")
                print("2. Update CGPA")
                print("3. Update Marks")
                print("4. Update Branch")
                print("5. Update Section")

                update_choice = int(input("Enter your choice: "))

                fields = {
                    1: "name",
                    2: "cgpa",
                    3: "marks",
                    4: "branch",
                    5: "section"
                }

                if update_choice not in fields:
                    print("Invalid choice")
                    continue

                field = fields[update_choice]

                if field in ["name", "branch", "section"]:
                    new_value = input("Enter new value: ").strip()

                elif field == "cgpa":
                    new_value = float(input("Enter new CGPA: "))

                else:
                    new_value = int(input("Enter new marks: "))

                manager.update_student(student_id, field, new_value)

            except ValueError:
                print("Invalid input")

        # 5. Delete Student
        elif choice == 5:

            try:
                student_id = int(input("Enter Student ID: "))
                manager.delete_student(student_id)

            except ValueError:
                print("Please enter a valid student ID")

        # 6. Exit
        elif choice == 6:
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid choice. Please try again.")

finally:
    manager.close()