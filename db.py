import sqlite3

def get_strings():

    conn = sqlite3.connect("db.db")

    cursor = conn.cursor()

    sql = "SELECT * FROM instrument"

    cursor.execute(sql)

    instrument = cursor.fetchall()

    conn.close()

    return instrument


print(get_strings())