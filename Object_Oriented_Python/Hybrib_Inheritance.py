
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(self, name, age)
        self.student_id = student_id

class Teacher(Person):
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject

class TeachingAssistant(Student, Teacher):
    def __init__(self, name, age, student_id, subject, study_time):
        Student.__init__(self, name, age, student_id)
        Teacher.__init__(self, name, age, subject)
        self.study_time = study_time

    def display_info(self):
        print("\n--- Teaching Assistant Info ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Student ID: {self.student_id}")
        print(f"Subject: {self.subject}")
        print(f"Study Time: {self.study_time} Hours/Week")

ta = TeachingAssistant("Alice", 17, "S04597", "Mechanics", 7)
ta.display_info()
