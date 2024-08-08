class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {
            "Math": 0,
            "English": 0,
            "Physics": 0,
            "Chemistry": 0,
            "Biology": 0
        }

    def add_grade(self, subject, score):
        if subject in self.grades:
            grade = self.calculate_letter_grade(score)
            self.grades[subject] = grade
        else:
            print("Invalid subject. Students can only have grades for Math, English, Physics, Chemistry, and Biology.")

    def calculate_letter_grade(self, score):
        if score >= 70:
            return 'A'
        elif score >= 60:
            return 'B'
        elif score >= 50:
            return 'C'
        elif score >= 40:
            return 'D'
        else:
            return 'F'

    def calculate_gpa(self):
        if not self.grades:
            return 0

        grade_points = {
            'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0
        }

        total_grade_points = 0
        for grade in self.grades.values():
            total_grade_points += grade_points.get(grade.upper(), 0)

        return total_grade_points / len(self.grades)

class GradesManagementSystem:
    def __init__(self):
        self.students = {}
        self.create_dummy_data()

    def create_dummy_data(self):
        # Dummy data now initializes all 5 courses with scores of 0
        self.students = {
            "101": Student("Alice", "101"),
            "102": Student("Bob", "102"),
            "103": Student("Charlie", "103")
        }

    def add_student(self):
        while True:
            student_id = input("Enter student ID: ")
            if student_id not in self.students:
                break
            else:
                print("Student ID already exists. Please enter a unique ID.")

        name = input("Enter student name: ")
        self.students[student_id] = Student(name, student_id)
        print("Student added successfully.")

    def record_grades(self):
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            student = self.students[student_id]
            while True:
                subject = input("Enter subject (Math, English, Physics, Chemistry, Biology): ")
                if subject in student.grades:
                    break
                else:
                    print("Invalid subject. Please choose from: Math, English, Physics, Chemistry, Biology.")

            while True:
                try:
                    score = int(input("Enter score (0-100): "))
                    if 0 <= score <= 100:
                        break
                    else:
                        print("Invalid score. Please enter a value between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            student.add_grade(subject, score)
            print("Grade recorded successfully.")
        else:
            print("Student not found.")

    def calculate_gpa(self):
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            student = self.students[student_id]
            gpa = student.calculate_gpa()
            print(f"GPA for {student.name}: {gpa:.2f}")
        else:
            print("Student not found.")

    def find_highest_lowest_grades(self):
        if not self.students:
            print("No students in the system.")
            return

        highest_gpa = -1
        lowest_gpa = 4.1 
        highest_student = None
        lowest_student = None

        for student in self.students.values():
            gpa = student.calculate_gpa()
            if gpa > highest_gpa:
                highest_gpa = gpa
                highest_student = student
            if gpa < lowest_gpa:
                lowest_gpa = gpa
                lowest_student = student

        print(f"Highest GPA: {highest_student.name} - {highest_gpa:.2f}")
        print(f"Lowest GPA: {lowest_student.name} - {lowest_gpa:.2f}")

    def display_records(self):
        if not self.students:
            print("No students in the system.")
            return

        for student in self.students.values():
            print(f"Student ID: {student.student_id}")
            print(f"Name: {student.name}")
            print("Grades:")
            for subject, grade in student.grades.items():
                print(f"  {subject}: {grade}")
            print(f"GPA: {student.calculate_gpa():.2f}")
            print("------------------------")

def main():
    system = GradesManagementSystem()

    while True:
        print("\nStudent Grades Management System")
        print("1. Add Student")
        print("2. Record Grades")
        print("3. Calculate GPA")
        print("4. Find Highest/Lowest GPAs")
        print("5. Display Records")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            system.add_student()
        elif choice == '2':
            system.record_grades()
        elif choice == '3':
            system.calculate_gpa()
        elif choice == '4':
            system.find_highest_lowest_grades()
        elif choice == '5':
            system.display_records()
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
