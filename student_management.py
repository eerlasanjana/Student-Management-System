import json
def save_student():
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)
def load_student():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def add_student():
    print("\nYour choice is Add Student")
    student_id = int(input("Enter the student ID: "))
    for student in students:
        if student["student_id"] == student_id:
            print("Student ID already exists")
            return
    name = input("Enter the name: ")
    if name.strip() == "":
        print("Name cannot be empty")
        return
    cgpa = float(input("Enter the student CGPA: "))
    if cgpa < 0 or cgpa > 10:
        print("CGPA should be between 0 and 10")
        return
    marks = int(input("Enter the student marks: "))
    if marks < 0 or marks > 100:
        print("Marks should be between 0 and 100")
        return
    branch = input("Enter the student branch: ")
    if branch.strip() == "":
        print("Branch cannot be empty")
        return
    section = input("Enter the student section: ")
    if section.strip() == "":
        print("Section cannot be empty")
        return
    student = {
        "student_id": student_id,
        "name": name,
        "cgpa": cgpa,
        "marks": marks,
        "branch": branch,
        "section": section
    }
    students.append(student)
    save_student()
    print("Student added successfully")
def view_student():
    print("\nYour choice is View Student")
    if len(students) == 0:
        print("No students found")
        return
    for student in students:
        print("----------------------")
        for key, value in student.items():
            print(key, ":", value)
        print("----------------------")
def search_student():
    print("\nYour choice is Search Student")
    student_id = int(input("Enter the student ID: "))
    for student in students:
        if student["student_id"] == student_id:
            print("Student found")
            for key, value in student.items():
                print(key, ":", value)
            return
    print("Student details not found")
def update_student():
    print("\nYour choice is Update Student")
    student_id = int(input("Enter the student ID to update: "))
    for i in range(len(students)):
        if students[i]["student_id"] == student_id:
            print("\nWhat do you want to update?")
            print("1. Update Name")
            print("2. Update CGPA")
            print("3. Update Marks")
            print("4. Update Branch")
            print("5. Update Section")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                name = input("Enter the new name: ")
                if name.strip() == "":
                    print("Name cannot be empty")
                    return
                students[i]["name"] = name
            elif choice == 2:
                cgpa = float(input("Enter the new CGPA: "))
                if cgpa < 0 or cgpa > 10:
                    print("CGPA should be between 0 and 10")
                    return
                students[i]["cgpa"] = cgpa
            elif choice == 3:
                marks = int(input("Enter the new marks: "))
                if marks < 0 or marks > 100:
                    print("Marks should be between 0 and 100")
                    return
                students[i]["marks"] = marks
            elif choice == 4:
                branch = input("Enter the new branch: ")
                if branch.strip() == "":
                    print("Branch cannot be empty")
                    return
                students[i]["branch"] = branch
            elif choice == 5:
                section = input("Enter the new section: ")
                if section.strip() == "":
                    print("Section cannot be empty")
                    return
                students[i]["section"] = section
            else:
                print("Invalid choice")
                return
            save_student()
            print("Student updated successfully")
            return
    print("Student ID not found")
def delete_student():
    print("\nYour choice is Delete Student")
    student_id = int(input("Enter the student ID to delete: "))
    for i in range(len(students)):
        if students[i]["student_id"] == student_id:
            students.pop(i)
            save_student()
            print("Student deleted successfully")
            return
    print("Student ID not found")
print("========== Welcome to Student Management System ==========")
students = load_student()
while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        view_student()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_student()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        print("Thank you for using the Student Management System")
        break
    else:
        print("Invalid choice. Please try again")