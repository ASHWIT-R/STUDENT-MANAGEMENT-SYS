import json


# ==============================
# Student Class
# ==============================

class Student:

    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = {}

    def add_marks(self, subject, marks):
        self.marks[subject] = marks

    def get_total(self):
        return sum(self.marks.values())

    def get_percentage(self):
        if not self.marks:
            return 0

        return self.get_total() / len(self.marks)

    def get_grade(self):
        percentage = self.get_percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("\n----------------------------")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)

        if self.marks:
            print("\nMarks:")

            for subject, marks in self.marks.items():
                print(f"{subject}: {marks}")

            print("Total:", self.get_total())
            print("Percentage:", self.get_percentage(), "%")
            print("Grade:", self.get_grade())

        print("----------------------------")


# ==============================
# Student List
# ==============================

students = []


# ==============================
# Add Student
# ==============================

def add_student():

    student_id = input("Enter Student ID: ")

    # Check duplicate ID
    for student in students:
        if student.student_id == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Student Name: ")

    try:
        age = int(input("Enter Student Age: "))
    except ValueError:
        print("Age must be a number.")
        return

    course = input("Enter Course: ")

    student = Student(student_id, name, age, course)

    students.append(student)

    print("\nStudent added successfully!")


# ==============================
# View Students
# ==============================

def view_students():

    if not students:
        print("\nNo students found.")
        return

    print("\n========== ALL STUDENTS ==========")

    for student in students:
        student.display()


# ==============================
# Search Student
# ==============================

def search_student():

    student_id = input("Enter Student ID to search: ")

    for student in students:

        if student.student_id == student_id:
            student.display()
            return

    print("\nStudent not found.")


# ==============================
# Update Student
# ==============================

def update_student():

    student_id = input("Enter Student ID to update: ")

    for student in students:

        if student.student_id == student_id:

            print("\n1. Update Name")
            print("2. Update Age")
            print("3. Update Course")

            choice = input("Enter your choice: ")

            if choice == "1":
                student.name = input("Enter new name: ")
                print("Name updated successfully.")

            elif choice == "2":

                try:
                    student.age = int(input("Enter new age: "))
                    print("Age updated successfully.")
                except ValueError:
                    print("Age must be a number.")

            elif choice == "3":
                student.course = input("Enter new course: ")
                print("Course updated successfully.")

            else:
                print("Invalid choice.")

            return

    print("\nStudent not found.")


# ==============================
# Delete Student
# ==============================

def delete_student():

    student_id = input("Enter Student ID to delete: ")

    for student in students:

        if student.student_id == student_id:

            students.remove(student)

            print("\nStudent deleted successfully.")
            return

    print("\nStudent not found.")


# ==============================
# Add Marks
# ==============================

def add_marks():

    student_id = input("Enter Student ID: ")

    for student in students:

        if student.student_id == student_id:

            subject = input("Enter Subject: ")

            try:
                marks = float(input("Enter Marks: "))

                if marks < 0 or marks > 100:
                    print("Marks must be between 0 and 100.")
                    return

            except ValueError:
                print("Marks must be a number.")
                return

            student.add_marks(subject, marks)

            print("\nMarks added successfully.")
            return

    print("\nStudent not found.")


# ==============================
# Show Result
# ==============================

def show_result():

    student_id = input("Enter Student ID: ")

    for student in students:

        if student.student_id == student_id:

            if not student.marks:
                print("\nNo marks available for this student.")
                return

            print("\n========== RESULT ==========")

            print("Name:", student.name)
            print("Course:", student.course)

            print("\nSubject Marks:")

            for subject, marks in student.marks.items():
                print(f"{subject}: {marks}")

            print("\nTotal:", student.get_total())
            print("Percentage:", student.get_percentage(), "%")
            print("Grade:", student.get_grade())

            return

    print("\nStudent not found.")


# ==============================
# Class Statistics
# ==============================

def class_statistics():

    if not students:
        print("\nNo students available.")
        return

    percentages = []

    for student in students:

        if student.marks:
            percentages.append(student.get_percentage())

    print("\n========== CLASS STATISTICS ==========")

    print("Total Students:", len(students))

    if not percentages:
        print("No marks available.")
        return

    average = sum(percentages) / len(percentages)

    highest = max(percentages)
    lowest = min(percentages)

    passed = 0
    failed = 0

    for percentage in percentages:

        if percentage >= 40:
            passed += 1
        else:
            failed += 1

    print("Average Percentage:", round(average, 2), "%")
    print("Highest Percentage:", highest, "%")
    print("Lowest Percentage:", lowest, "%")
    print("Passed Students:", passed)
    print("Failed Students:", failed)


# ==============================
# Save Data
# ==============================

def save_data():

    data = []

    for student in students:

        student_data = {
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "course": student.course,
            "marks": student.marks
        }

        data.append(student_data)

    with open("students.json", "w") as file:

        json.dump(data, file, indent=4)

    print("\nStudent data saved successfully.")


# ==============================
# Load Data
# ==============================

def load_data():

    try:

        with open("students.json", "r") as file:

            data = json.load(file)

            for item in data:

                student = Student(
                    item["student_id"],
                    item["name"],
                    item["age"],
                    item["course"]
                )

                student.marks = item.get("marks", {})

                students.append(student)

        print("Student data loaded successfully.")

    except FileNotFoundError:

        print("No previous student data found.")


# ==============================
# Main Menu
# ==============================

def main():

    load_data()

    while True:

        print("\n")
        print("========================================")
        print("       STUDENT MANAGEMENT SYSTEM")
        print("========================================")

        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Add Marks")
        print("7. Show Result")
        print("8. Class Statistics")
        print("9. Save Data")
        print("10. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            update_student()

        elif choice == "5":
            delete_student()

        elif choice == "6":
            add_marks()

        elif choice == "7":
            show_result()

        elif choice == "8":
            class_statistics()

        elif choice == "9":
            save_data()

        elif choice == "10":

            save_data()

            print("\nThank you for using Student Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# ==============================
# Program Start
# ==============================

if __name__ == "__main__":
    main()