import sqlite3

def create_database():
    db = sqlite3.connect('savings.db')

    cursor = db.cursor()
    cursor.execute('CREATE TABLE savings(total INTEGER)')
    db.commit()

    db.close()

def deposit():
    db = sqlite3.connect('savings.db')

    cursor = db.cursor()
    cursor.execute('INSERT INTO savings(total)VALUES(365)')
    db.commit()

    db.close()

def withdraw():
    pass
