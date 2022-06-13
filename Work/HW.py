import sqlite3 as sq

all_clients = [
    ('Алексей', 34, 'alex@yandex.ru'),
    ('Ирина', 18, 'ira2004@yandex.ru'),
    ('Евгений', 44, 'jenya@mail.ru'),
    ('Михаил', 41, 'miha@gmail.com'),
    ('Елена', 26, 'lena26@mail.ru'),
    ('Светлана', 30, 'sveta13@gmail.com'),
    ('Виктор', 36, 'vik132@yandex.ru'),
    ('Валентина', 54, 'valya2@mail.ru'),
    ('Артем', 33, 'artem@gmail.com')
]

with sq.connect('Clients.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS clients(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL CHECK(age > 0 AND age < 65),
    email TEXT UNIQUE
    )''')

    cur.executemany('INSERT INTO clients VALUES(NULL, ?, ?, ?)', all_clients)