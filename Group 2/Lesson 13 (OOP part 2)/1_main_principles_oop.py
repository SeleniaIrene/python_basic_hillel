# Створити ієрархію класів для опису академії.
# Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
# Продумати архітектуру: реалізувати принципи ООП

# Клас Person - базовий клас, який представляє особу.
# Має атрибути: ім'я, прізвище, вік.
# Методи для отримання та встановлення значень цих атрибутів.

# Клас Teacher, який наслідується від класу Person - представляє викладача.
# Має додатковий атрибут: список предметів, які викладає.
# Методи для додавання та видалення предметів.

# Клас Student, також наслідується від класу Person - представляє студента.
# Має атрибут: список курсів, які він відвідує.
# Методи для додавання та видалення курсів.

# Клас Academy - представляє академію або університет.
# Має атрибути: список викладачів, список студентів, список предметів.
# Методи для додавання та видалення викладачів, студентів та предметів.

# Клас Subject - представляє окремий предмет, який може викладатися університетом.
# Має атрибути: назва предмету, викладач, студенти.

# Клас Course - представляє окремий курс, який може викладатися університетом.
# Має атрибути: назва курсу, викладач, список студентів, список предметів, аудиторій.

# Клас Classroom - представляє окрему аудиторію, в якій проводяться заняття.
# Має атрибути: номер аудиторії, кількість місць, умови, доступне обладнання.

#########################################################################################
# Словник допустимих курсів
valid_courses = {
     "Computer Science": True
    ,"Applied Mathematics": True
    ,"Software engineering": True
    ,"Psychology": False
}

# Словник допустимих предметів
valid_subjects = {
    "Computer Science": [
        "Programming Basics"
       ,"Algorithms and data structures"
       ,"Operating systems"
       ,"Databases"
       ,"Networks and communications"
    ],
    "Applied Mathematics": [
        "Linear Algebra"
       ,"Differential equations"
       ,"Statistics"
       ,"Numerical methods"
       ,"Optimization"
    ],
    "Software engineering": [
        "Requirements engineering"
       ,"Software design"
       ,"Software development"
       ,"Software testing"
    ]
}

#########################################################################################
class Person:
    __name = "No name"
    __age = 18

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__document = 12345  # (private) -> доступ тільки всередині класу
        self._course = "No info"  # (protected) -> доступ усередині класу та в класах спадкоємців

    @property #getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 2:
            self.__name = name
        else:
            print("Incorrect name")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 18:
            self.__age = age
        else:
            print("Incorrect age")

    @property
    def course(self):
        return self._course

    @course.setter
    def course(self, value):
        # Перевірка, чи є курс у словнику допустимих курсів і чи він доступний (True)
        if valid_courses.get(value, False):
            self._course = value
        else:
            print(f"The course '{value}' is not valid. Please choose a valid course.")

    @property
    def document(self):
        return self.__document

    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

#########################################################################################
class Student(Person):  #Наслідування від Person
    __grade = "No info"

    def __init__(self, name, age, course, grade):
        super().__init__(name, age)
        self.course = course
        self.grade = grade

    @property  # getter
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, grade):
        if grade in ("A","B","C","D","F"):
            self.__grade = grade
        else:
            print("Incorrect grade")

    def show_info(self):
        super().show_info()
        print(f"Course: {self.course}, Grade: {self.grade}")

# Створення екземпляра класу Person та Student
person1 = Person("John Doe", 20)
person1.course = "Computer Science"
student1 = Student(person1.name, person1.age, person1._course, "A")
student1.show_info()
print()

person2 = Person("", -18)
person2.course = "Computer"
student2 = Student(person2.name, person2.age, person2._course, "K")
student2.show_info()
print()

student3 = Student("Erika Pitts", 21, "Applied Mathematics", "B")
student3.show_info()
print()
#########################################################################################
class Teacher(Person): #Наслідування від Person

    def __init__(self, name, age, subjects = None):
        super().__init__(name, age)
        self.subjects = subjects if subjects is not None else []

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)

    def show_info(self):
        super().show_info()
        print(f"Subjects: {', '.join(self.subjects)}")

# Створення екземпляра класу Person та Teacher
person3 = Person("Olha White", 45)
teacher1 = Teacher(person3.name, person3.age)
teacher1.add_subject("Algorithms and data structures")
teacher1.add_subject("Numerical Methods")
teacher1.add_subject("Statistics")
teacher1.remove_subject("Statistics")
teacher1.show_info()
print()

#########################################################################################
class Subject:
    __name = "No info"
    __teacher = "No info"

    def __init__(self, name, teacher = None, students = None):
        self.name = name
        self.teacher = teacher
        self.students = students if students is not None else []

    @property  # getter
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        # Перевірка, чи є предмет у словнику предметів та курсів
        if any(name in subjects for subjects in valid_subjects.values()):
            self.__name = name
        else:
            print("Incorrect subject name")

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, teacher):
        if isinstance(teacher, Teacher):  # Перевірка, чи є об'єкт викладачем
            self.__teacher = teacher
        else:
            print("Incorrect teacher")

    def add_student(self, student):
        if isinstance(student, Student): # Перевірка, чи є об'єкт студентом
            if student not in self.students:
                self.students.append(student)
        else:
            print("Incorrect student or student already added")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def show_info(self):
        print(f"Subject: {self.name}, teacher: {self.teacher.name}, students: {', '.join([student.name for student in self.students])}")

subject1 = Subject("Optimization", teacher1, [student1])
subject1.add_student(student2)
subject1.remove_student(student2)
subject1.show_info()
print()

subject2 = Subject("Software testing", teacher1, [student1,student3])
subject2.show_info()
print()

#########################################################################################
class Academy:
    def __init__(self, teachers=None, students=None, subjects=None):
        self.teachers = teachers if teachers is not None else []
        self.students = students if students is not None else []
        self.subjects = subjects if subjects is not None else []

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)

    def remove_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)

    def remove_subject(self, subject):
        if subject in self.subjects:
            self.subjects.remove(subject)

    def show_info(self):
        print("Academy Information")
        print("Teachers:")
        for teacher in self.teachers:
            print(f"- {teacher.name}")
        print("Students:")
        for student in self.students:
            print(f"- {student.name}")
        print("Subjects:")
        for subject in self.subjects:
            print(f"- {subject.name}")

my_academy = Academy()
my_academy.add_teacher(teacher1)
my_academy.add_student(student1)
my_academy.add_student(student3)
my_academy.add_subject(subject1)
my_academy.add_subject(subject2)
my_academy.show_info()
print()

#########################################################################################
class Course:
    def __init__(self, name, teacher, subjects=None, students=None, classroom=None):
        self.name = name
        self.teacher = teacher
        self.subjects = subjects if subjects is not None else []
        self.students = students if students is not None else []
        self.classroom = classroom

    def show_info(self):
        print(f"Course Name: {self.name}")
        print(f"Teacher: {self.teacher.name if self.teacher else 'No teacher'}")
        print("Subjects:")
        for subject in self.subjects:
            print(f"- {subject.name}")
        print("Students:")
        for student in self.students:
            print(f"- {student.name}")
        if self.classroom:
            print(f"Classroom: {self.classroom.number}, Capacity: {self.classroom.capacity}")
        else:
            print("No classroom assigned")

#########################################################################################
class Classroom:
    def __init__(self, number, capacity, conditions=None, equipment=None):
        self.number = number
        self.capacity = capacity
        self.conditions = conditions if conditions is not None else "Standard"
        self.equipment = equipment if equipment is not None else []

    def show_info(self):
        print(f"Classroom Number: {self.number}")
        print(f"Capacity: {self.capacity}")
        print(f"Conditions: {self.conditions}")
        print("Equipment:")
        for item in self.equipment:
            print(f"- {item}")

classroom101 = Classroom("101", 30, "Good", ["Projector", "Whiteboard"])
programmingCourse = Course("Programming 101", teacher1, [subject1, subject2], [student1, student2], classroom101)

programmingCourse.show_info()
print()
classroom101.show_info()
