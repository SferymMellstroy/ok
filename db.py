import sqlite3

def get_strings():

    conn = sqlite3.connect("db.db")

    cursor = conn.cursor()

    sql = "SELECT * FROM instrument WHERE type = 'Струнный инструмент'"

    cursor.execute(sql)

    instrument = cursor.fetchall()

    conn.close()

    return instrument

def get_drums():

    conn = sqlite3.connect("db.db")

    cursor = conn.cursor()

    sql = "SELECT * FROM instrument WHERE type = 'Ударный инструмент'"

    cursor.execute(sql)

    instrument = cursor.fetchall()

    conn.close()

    return instrument

def get_duhovoi():

    conn = sqlite3.connect("db.db")

    cursor = conn.cursor()

    sql = "SELECT * FROM instrument WHERE type = 'Духовой иструмент'"

    cursor.execute(sql)

    instrument = cursor.fetchall()

    conn.close()

    return instrument

def add_user(login, email, password):
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()
    sql = "INSERT INTO user (login, email, password) VALUES (?, ?, ?)"
    cursor.execute(sql, (login, email, password))
    conn.commit()
    conn.close()


print(get_strings())
print(get_drums())
print(get_duhovoi())