# Student Record System

students = []

def display_menu():
    print("\nStudent Record System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    course = input("Enter student course: ")

    student = {
        "student_id": student_id,
        "name": name,
        "course": course
    }

    students.append(student)
    print("Student record added successfully.")

def view_students():
    if not students:
        print("No student records available.")
    else:
        print("\nStudent Records:")
        for index, student in enumerate(students, start=1):
            print(f"{index}. ID: {student['student_id']}, Name: {student['name']}, Course: {student['course']}")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Exiting Student Record System.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
