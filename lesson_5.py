import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS grades (
    student_id INTEGER,
    subject TEXT NOT NULL,
    grade INTEGER NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
)
''')

conn.commit()

def add_student(name, age):
    cursor.execute('INSERT INTO students (name, age) VALUES (?, ?)', (name, age))
    conn.commit()
    print(f"Студент {name} добавлен.")

def add_grade(student_id, subject, grade):
    cursor.execute('INSERT INTO grades (student_id, subject, grade) VALUES (?, ?, ?)', (student_id, subject, grade))
    conn.commit()
    print(f"Оценка {grade} по предмету {subject} добавлена студенту с ID {student_id}.")

def get_student_grades(student_id):
    cursor.execute('SELECT subject, grade FROM grades WHERE student_id = ?', (student_id,))
    grades = cursor.fetchall()
    
    if grades:
        print(f"Оценки студента с ID {student_id}:")
        for subject, grade in grades:
            print(f"Предмет: {subject}, Оценка: {grade}")
    else:
        print(f"Оценок для студента с ID {student_id} не найдено.")

def average_grade(student_id):
    cursor.execute('SELECT AVG(grade) FROM grades WHERE student_id = ?', (student_id,))
    average = cursor.fetchone()[0]
    
    if average is not None:
        print(f"Средняя оценка студента с ID {student_id}: {round(average, 2)}")
    else:
        print(f"Нет оценок для студента с ID {student_id}.")

if __name__ == "__main__":
    add_student("Содик", 20)
    add_student("Сарик", 22)

    add_grade(1, "Математика", 5)
    add_grade(1, "Физика", 4)
    add_grade(2, "Химия", 3)
    add_grade(2, "История", 5)

    get_student_grades(1)
    get_student_grades(2)

    average_grade(1)
    average_grade(2)

conn.close()








# Задание: Управление списком студентов и их оценками

# Создайте базу данных students.db и подключитесь к ней.

# Создайте таблицу students со следующими полями:

# id (INTEGER) — идентификатор студента, автоинкремент.
# name (TEXT) — имя студента.
# age (INTEGER) — возраст студента.
# Создайте таблицу grades для хранения оценок, со следующими полями:

# student_id (INTEGER) — идентификатор студента (внешний ключ, связанный с students.id).
# subject (TEXT) — предмет.
# grade (INTEGER) — оценка по предмету.
# Напишите функции для выполнения следующих действий:

# add_student(name, age): добавляет нового студента в таблицу students.
# add_grade(student_id, subject, grade): добавляет оценку студенту по конкретному предмету.
# get_student_grades(student_id): выводит список всех предметов и оценок для конкретного студента.
# Дополнительно:

# Напишите функцию average_grade(student_id), которая возвращает среднюю оценку студента по всем предметам.
# Пример выполнения:

# Добавьте несколько студентов.
# Назначьте каждому студенту по несколько оценок.
# Используйте get_student_grades() и average_grade() для вывода оценок и среднего балла студентов.