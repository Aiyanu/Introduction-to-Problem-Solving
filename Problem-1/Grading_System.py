class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.subjects = {
            "Math": 0,
            "English": 0,
            "Physics": 0,
            "Chemistry": 0,
            "Biology": 0
        }

    def add_grade(self, subject, score):
        if subject in self.subjects:
            self.subjects[subject] = int(score)  # Store the score directly 
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
        if not self.subjects:
            return 0

        grade_points = {
            'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
            'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0
        }

        total_grade_points = 0
        for score in self.subjects.values():
            grade = self.calculate_letter_grade(score)
            total_grade_points += grade_points.get(grade.upper(), 0)

        return total_grade_points / len(self.subjects)

class GradesManagementSystem:
    def __init__(self):
        self.students = {}
        self.create_dummy_data()

    def create_dummy_data(self):
        self.students = {
            "101": Student("Alice", "101"),
            "102": Student("Bob", "102"),
            "103": Student("Charlie", "103")
        }

        self.students["101"].add_grade("Math", 85)
        self.students["101"].add_grade("English", 92)
        self.students["101"].add_grade("Physics", 75)
        self.students["101"].add_grade("Chemistry", 52)
        self.students["101"].add_grade("Biology", 90)

        self.students["102"].add_grade("Math", 60)
        self.students["102"].add_grade("English", 78)
        self.students["102"].add_grade("Physics", 52)
        self.students["102"].add_grade("Chemistry", 45)
        self.students["102"].add_grade("Biology", 65)

        self.students["103"].add_grade("Math", 98)
        self.students["103"].add_grade("English", 88)
        self.students["103"].add_grade("Physics", 95)
        self.students["103"].add_grade("Chemistry", 80)
        self.students["103"].add_grade("Biology", 72)

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

            for subject in student.subjects:
                while True:
                    try:
                        score = int(input(f"Enter score for {subject} (0-100): "))
                        if 0 <= score <= 100:
                            break
                        else:
                            print("Invalid score. Please enter a value between 0 and 100.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

                student.add_grade(subject, score)

            print("Grades recorded successfully.")
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
        student_id = input("Enter student ID: ")
        if student_id in self.students:
            student = self.students[student_id]
            if not student.subjects:
                print(f"{student.name} has no recorded grades.")
            else:
                highest_score = max(student.subjects.values())
                lowest_score = min(student.subjects.values())

                highest_subjects = [subject for subject, score in student.subjects.items() if score == highest_score]
                lowest_subjects = [subject for subject, score in student.subjects.items() if score == lowest_score]

                print(f"\nStudent: {student.name} (ID: {student.student_id})")

                if len(highest_subjects) > 1:
                    print(f"Highest Scores: {highest_score} (Subjects: {', '.join(highest_subjects)})")
                else:
                    print(f"Highest Score: {', '.join([f'{subject} | {highest_score} | {student.calculate_letter_grade(highest_score)}' for subject in highest_subjects])}")

                if len(lowest_subjects) > 1:
                    print(f"Lowest Scores: {lowest_score} (Subjects: {', '.join(lowest_subjects)})")
                else:
                    print(f"Lowest Score: {', '.join([f'{subject} | {lowest_score} | {student.calculate_letter_grade(lowest_score)}' for subject in lowest_subjects])}")
        else:
            print("Student not found.")


    def display_records(self):
        if not self.students:
            print("No students in the system.")
            return

        for student in self.students.values():
            print(f"Student ID: {student.student_id}")
            print(f"Name: {student.name}")
            print("Grades:")
            for subject, score in student.subjects.items():
                print(f"  {subject}: {score} ({student.calculate_letter_grade(score)})")
            print(f"GPA: {student.calculate_gpa():.2f}")
            print("------------------------")

def main():
    system = GradesManagementSystem()

    while True:
        print("\nStudent Grades Management System")
        print("1. Add Student")
        print("2. Record Grades")
        print("3. Calculate GPA")
        print("4. Find Highest/Lowest Scores")
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
    

def calculate_letter_grade(score):
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

def calculate_gpa(student):
    if not student['subjects']:
        return 0

    grade_points = {
        'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0.0
    }

    total_grade_points = 0
    for score in student['subjects'].values():
        grade = calculate_letter_grade(score)
        total_grade_points += grade_points.get(grade.upper(), 0)

    return total_grade_points / len(student['subjects'])

def create_dummy_data():
    students = {
        "101": {
            "name": "Alice",
            "subjects": {
                "Math": 85,
                "English": 92,
                "Physics": 75,
                "Chemistry": 52, 
                "Biology": 90
            }
        },
        "102": {
            "name": "Bob",
            "subjects": {
                "Math": 60,
                "English": 78,
                "Physics": 52,
                "Chemistry": 45,
                "Biology": 65
            }
        },
        "103": {
            "name": "Charlie",
            "subjects": {
                "Math": 98,
                "English": 88,
                "Physics": 95,
                "Chemistry": 80,
                "Biology": 72
            }
        }
    }
    return students

def add_student(students):
    while True:
        student_id = input("Enter student ID: ")
        if student_id not in students:
            break
        else:
            print("Student ID already exists. Please enter a unique ID.")

    name = input("Enter student name: ")
    students[student_id] = {
        "name": name,
        "subjects": {
            "Math": 0,
            "English": 0,
            "Physics": 0,
            "Chemistry": 0,
            "Biology": 0
        }
    }
    print("Student added successfully.")

def record_grades(students):
    student_id = input("Enter student ID: ")
    if student_id in students:
        student = students[student_id]

        for subject in student['subjects']:
            while True:
                try:
                    score = int(input(f"Enter score for {subject} (0-100): "))
                    if 0 <= score <= 100:
                        break
                    else:
                        print("Invalid score. Please enter a value between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

            student['subjects'][subject] = score

        print("Grades recorded successfully.")
    else:
        print("Student not found.")

def calculate_student_gpa(students):
    student_id = input("Enter student ID: ")
    if student_id in students:
        student = students[student_id]
        gpa = calculate_gpa(student)
        print(f"GPA for {student['name']}: {gpa:.2f}")
    else:
        print("Student not found.")

def find_highest_lowest_grades(students):
    student_id = input("Enter student ID: ")
    if student_id in students:
        student = students[student_id]
        if not student['subjects']:
            print(f"{student['name']} has no recorded grades.")
        else:
            # Get a list of all the scores
            scores = list(student['subjects'].values())

            # Find the highest and lowest scores
            highest_score = max(scores)
            lowest_score = min(scores)

            # Find the subjects and grades corresponding to the highest and lowest scores
            highest_subjects = [(subject, calculate_letter_grade(score)) for subject, score in student['subjects'].items() if score == highest_score]
            lowest_subjects = [(subject, calculate_letter_grade(score)) for subject, score in student['subjects'].items() if score == lowest_score]

            print(f"\nStudent: {student['name']} (ID: {student_id})")
            print(f"Highest Score: {', '.join([f'{subject} | {highest_score} | {grade}' for subject, grade in highest_subjects])}")
            print(f"Lowest Score: {', '.join([f'{subject} | {lowest_score} | {grade}' for subject, grade in lowest_subjects])}")

    else:
        print("Student not found.")


def display_records(students):
    if not students:
        print("No students in the system.")
        return

    for student_id, student in students.items():
        print(f"Student ID: {student_id}")
        print(f"Name: {student['name']}")
        print("Grades:")
        for subject, score in student['subjects'].items():
            print(f"  {subject}: {score} ({calculate_letter_grade(score)})")
        print(f"GPA: {calculate_gpa(student):.2f}")
        print("------------------------")

def main():
    students = create_dummy_data()

    while True:
        print("\nStudent Grades Management System")
        print("1. Add Student")
        print("2. Record Grades")
        print("3. Calculate GPA")
        print("4. Find Highest/Lowest Scores")
        print("5. Display Records")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            record_grades(students)
        elif choice == '3':
            calculate_student_gpa(students)
        elif choice == '4':
            find_highest_lowest_grades(students)
        elif choice == '5':
            display_records(students)
        elif choice == '6':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

