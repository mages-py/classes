class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self) -> str:
        courses_in_process = 'Курсы в процессе изучения: ' + \
            ', '.join(self.courses_in_progress)
        courses_finish = 'Завершенные курсы: ' + \
            ', '.join(self.finished_courses)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._avg_grade()}\n{courses_in_process}\n{courses_finish}\n"

    def rate_for_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avg_grade(self, course_name=None):
        rates = []
        for course, rate in self.grades.items():
            if not course_name or course == course_name:
                rates += rate
        if len(rates):
            return float("{:.2f}".format(sum(rates) / len(rates)))
        return 0


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._avg_grade()}\n"

    def __eq__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            return 'Ошибка'
        return self._avg_grade() == other_lecturer._avg_grade()

    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            return 'Ошибка'
        return self._avg_grade() < other_lecturer._avg_grade()

    def __le__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            return 'Ошибка'
        return self._avg_grade() <= other_lecturer._avg_grade()

    def _avg_grade(self, course_name=None):
        rates = []
        for course, rate in self.grades.items():
            if not course_name or course == course_name:
                rates += rate
        if len(rates):
            return float("{:.2f}".format(sum(rates) / len(rates)))
        return 0


class Rewiewer(Mentor):
    def __str__(self) -> str:
        return f"Имя: {self.name}\nФамилия:{self.surname}\n"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def students_avg_grade(students, course):
    grades = []
    for student in students:
        if isinstance(student, Student) and course in student.grades:
            grades += student.grades[course]
    if len(grades):
            return float("{:.2f}".format(sum(grades) / len(grades)))

def lectures_avg_grade(lecturers, course):
    grades = []
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer) and course in lecturer.grades:
            grades += lecturer.grades[course]
    if len(grades):
            return float("{:.2f}".format(sum(grades) / len(grades)))

student1 = Student('Ruoy', 'Eman', 'Male')
student1.courses_in_progress += ['Python', 'VB']

student2 = Student('Eva', 'Brown', 'Female')
student2.courses_in_progress += ['Python', 'PHP', 'Java']

lecturer1 = Lecturer('Egor', 'Krid')
lecturer1.courses_attached += ['Python', 'Java', 'Go']

student1.rate_for_lecture(lecturer1, 'Python', 8)
student1.rate_for_lecture(lecturer1, 'Python', 7)
student1.rate_for_lecture(lecturer1, 'Python', 5)
student1.rate_for_lecture(lecturer1, 'Python', 9)
student2.rate_for_lecture(lecturer1, 'Python', 5)
student2.rate_for_lecture(lecturer1, 'Python', 8)
student2.rate_for_lecture(lecturer1, 'Python', 8)
student2.rate_for_lecture(lecturer1, 'Python', 7)


lecturer2 = Lecturer('Anton', 'Holev')
lecturer2.courses_attached += ['Python', 'PHP', 'VB']

student1.rate_for_lecture(lecturer2, 'Python', 8)
student1.rate_for_lecture(lecturer2, 'Python', 6)
student1.rate_for_lecture(lecturer2, 'Python', 9)
student1.rate_for_lecture(lecturer2, 'Python', 5)
student2.rate_for_lecture(lecturer1, 'Python', 7)
student2.rate_for_lecture(lecturer1, 'Python', 8)
student2.rate_for_lecture(lecturer1, 'Python', 6)
student2.rate_for_lecture(lecturer1, 'Python', 9)


reviewer1 = Rewiewer('Frodo', 'Smith')
reviewer1.courses_attached += ['Python', 'PHP', 'Go']

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'VB', 8)
reviewer1.rate_hw(student1, 'VB', 9)

reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student2, 'Java', 8)
reviewer1.rate_hw(student2, 'Java', 7)

reviewer2 = Rewiewer('Mages', 'Lectorov')
reviewer2.courses_attached += ['Java', 'Go', 'Python']

reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'VB', 9)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Java', 9)
print('-----------------Студенты-----------------')
print(student1)
print(student2)

print('-----------------Ревьюеры-----------------')
print(reviewer1)
print(reviewer2)

print('------------------Лекторы------------------')
print(lecturer1)
print(lecturer2)

print('-----------------Сравнение-----------------')
print(lecturer1 == lecturer2)
print(lecturer1 != lecturer2)
print(lecturer1 < lecturer2)
print(lecturer1 > lecturer2)
print(lecturer1 <= lecturer2)
print(lecturer1 >= lecturer2)

print('-----------------Функции-----------------')
course = 'Python'
print('Средняя оценка у студентов по курсу','"' + course + '":',  students_avg_grade([student1, student2], course))
print('Средняя оценка за лекции по курсу', '"' + course + '":',lectures_avg_grade([lecturer1, lecturer2], course))