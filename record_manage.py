# Student Record Management System in Python

students = []


def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")

    student = {
        "ID": student_id,
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\n--- Student Records ---")
        for student in students:
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            print("----------------------")



def search_student():
    search_id = input("Enter student ID to search: ")

    for student in students:
        if student["ID"] == search_id:
            print("\nStudent found:")
            print("ID:", student["ID"])
            print("Name:", student["Name"])
            print("Age:", student["Age"])
            print("Course:", student["Course"])
            return

    print("Student not found.")


def delete_student():
    delete_id = input("Enter student ID to delete: ")

    for student in students:
        if student["ID"] == delete_id:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Exiting Student Record Management System.")
        break

    else:
        print("Invalid choice! Please select a valid option.")