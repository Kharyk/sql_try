
from Base import Database

db = Database("school.db")

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7): ")

    if choice == "1":
        name = input("Введіть ім'я студента: ")
        age = int(input("Введіть вік студента: "))
        student_id = int(input("Введіть ID студента: "))
        db.students_query('''
        INSERT INTO students (name, age, student_id) VALUES (?, ?, ?)
        ''', (name, age, student_id))
        print(f"Студента {name} додано.")

    elif choice == "2":
        name = input("Введіть назву курсу: ")
        course_id = int(input("Введіть ID курсу: "))
        db.curs_query('''
        INSERT INTO curs (name, course_id) VALUES (?, ?)
        ''', (name, course_id))
        print(f"Курс {name} додано.")

    elif choice == "3":
        students = db.fetchall_students()
        for student in students:
            print(student)

    elif choice == "4":
        courses = db.fetchall_courses()
        for course in courses:
            print(course)

    elif choice == "5":
        student_id = int(input("Введіть ID студента: "))
        course_id = int(input("Введіть ID курсу: "))
        db.register_student(student_id, course_id)
        print(f"Студента з ID {student_id} зареєстровано на курс з ID {course_id}.")

    elif choice == "6":
        course_name = input("Введіть назву курсу: ")
        students_in_course = db.fetch_students_in_course(course_name)
        for student in students_in_course:
            print(student)

    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")
