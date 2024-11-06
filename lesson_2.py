''' База данных '''
''' Система управелия базы данных '''
''' CRUD - CREATE, RETRIVE, UPDATE, DELETE '''

import sqlite3

connect = sqlite3.connect('Itpark.db')
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS itpark(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR (30) NOT NULL,
        age INT DEFAULT NULL,
        diraction TEXT,
        is_have BOOLEAN NOT NULL DEFAULT FALSE,
        rating DOUBLE (4,2) DEFAULT (0.0),
        dirth_date DATE
    )
""")

def register():
    full_name = input('Введите ФИО: ')
    age = int(input('Введите свой возраст: '))
    direction = input('Введите направление: ')
    is_have = bool(input('Наличие ноутбука: '))
    rating = float(input('Введите свой рейтинг: '))
    dirth_date = input('Введите дату рождения: ')

    cursor.execute(f""" INSERT INTO itpark
                   (full_name, age, diraction, is_have, rating, dirth_date)
                   VALUES ('{full_name}', '{age}', '{direction}', {is_have}, {rating}, '
                   {dirth_date}')""")

    connect.commit()

register(   )