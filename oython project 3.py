
# Student Data Organizer
# Created by: Jaineel Shingala

students = {}

subjects_offered = [
    "Math",
    "Science",
    "English"
]


def add_student():
    print("\nEnter student details:")

    student_id = input("Student ID: ")
    
    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Name: ")
    age = input("Age: ")
    grade = input("Grade: ")
    dob = input("Date of Birth (YYYY-MM-DD): ")
    subjects = input("Subjects : ")

    students[student_id] = {
        "name": name,
        "age": age,
        "grade": grade,
        "dob": dob,
        "subjects": subjects
    }

    print("\nStudent added successfully!")


def display_students():
    print("\nStudent Records:")

    if not students:
        print("No students found.")
        return

    for student_id, details in students.items():
        print("\nStudent ID:", student_id)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Grade:", details["grade"])
        print("Date of Birth:", details["dob"])
        print("Subjects:", details["subjects"])


def update_student():
    print("\nUpdate Student Information")
    student_id = input("Enter Student ID to update: ")

    if student_id not in students:
        print("Student not found!")
        return

    details = students[student_id]

    details["name"] = input("Name: ")
    details["age"] = input("Age: ")
    details["grade"] = input("Grade: ")
    details["dob"] = input("Date of Birth (YYYY-MM-DD): ")
    details["subjects"] = input("Subjects : ")

    print("Student information updated successfully!")


def delete_student():
    print("\nDelete Student")
    student_id = input("Enter Student ID to delete: ")

    if student_id in students:
        del students[student_id]
        print("Student deleted successfully!")
   

def display_subjects():
    print("\nSubjects Offered:")

    for number, subject in enumerate(subjects_offered, start=1):
        print(f"{number}. {subject}")


def main():
    print("Welcome to the Student Data Organizer!")

    while True:
        print("\nSelect an option:")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            display_subjects()

        elif choice == "6":
            print("Thank you for using Student Data Organizer!")
            break

        else:
            print("Invalid choice! Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()

