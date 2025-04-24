students = [
    {"name": "Иван", "age": 20, "grades": {"математика": 4, "физика": 5, "химия": 3}},
    {"name": "Мария", "age": 19, "grades": {"математика": 5, "физика": 5, "химия": 5}},
    {"name": "Пётр", "age": 21, "grades": {"математика": 3, "физика": 4, "химия": 2}},
    {"name": "Анна", "age": 22, "grades": {"математика": 5, "физика": 4, "химия": 4}},
]


"""Функция возвращает самого младшего студента """
def get_min_age(students):
    min_age = (1000, "")
    for student in students:
        if student["age"] < min_age[0]:
            min_age = student["age"], student["name"]
    print(f"Самый младший студент: {min_age[1]}, возраст: {min_age[0]}")
    return min_age


"""Функция возвращает имя студента с самой высокой средней оценкой"""
def get_rating_is_high(students):
    grades = students[0]["grades"]
    average_grade = float(sum(grade for grade in grades.values()) / len(grades))
    for student in students:
        grade_student = float(sum(grade for grade in student["grades"].values()) / len(student["grades"]))
        if grade_student > average_grade:
            average_grade = grade_student
            name = student["name"]

    print(f"Студент с самой высокой средней оценкой: {name}, средний балл: {average_grade:.2f}")
    return name, average_grade



"""Функция возвращает предмет по которому самый высокий средний балл среди всех студентов"""
def get_item_with_high_score(students):
    math, phisic, him = [], [], []
    max = ("", 0)
    for student in students:
        math.append(student["grades"]["математика"])
        phisic.append(student["grades"]["физика"])
        him.append(student["grades"]["химия"])

    objects = {"математика": float(sum(math) / len(math)),
               "физика": float(sum(phisic) / len(phisic)),
               "химия": float(sum(him) / len(him))}

    for key, value in objects.items():
        if value > max[1]:
            max = (key, value)

    print(f"Предмет с самым высоким средним баллом: {max[0]}, средний балл: {max[1]:.2f}")
    return max



"""Функция возвращает студентов со средним балом больше или равному 3"""
def get_student_with_grade_above_three(students):
    filtered_students = [
        student for student in students
        if sum(student["grades"].values()) / len(student["grades"]) >= 3.0
    ]
    print("Студенты с баллом выше или равному 3.0:")
    for student in filtered_students:
        print(f"{student['name']}: средний балл = {sum(student['grades'].values())/len(student['grades']):.2f}")


get_min_age(students)
get_rating_is_high(students)
get_item_with_high_score(students)
get_student_with_grade_above_three(students)