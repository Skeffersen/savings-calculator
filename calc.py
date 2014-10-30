import sqlite3

def create_account(account_name='saving', initial_deposit=0):
    db = sqlite3.connect('Bank.db')

    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Transactions(id INTEGER PRIMARY KEY, account_id INTEGER, type TEXT, amount INTEGER)')
    cursor.execute('INSERT INTO Transactions(account_id, type, amount)VALUES(1, ?, ?)', ('Deposit', initial_deposit))
    cursor.execute('CREATE TABLE IF NOT EXISTS Accounts(id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO Accounts(name)VALUES(?)', (account_name,))
    db.commit()

    db.close()

def deposit(amount, account):
    db = sqlite3.connect('Bank.db')

    cursor = db.cursor()
    db.commit()

    db.close()

def withdraw():
    pass

def output():
    db = sqlite3.connect('Bank.db')
    cursor = db.cursor()
    db1 = cursor.execute('SELECT name FROM Accounts')
    for row in db1:
        print 'Account: ', row[0]
    db2 = cursor.execute('SELECT amount FROM Transactions')
    for row in db2:
        print 'Amount: ', row[0]
    # cursor.execute('SELECT * FROM Accounts')
    # p = cursor.fetchall()
    # for x in p:
    #     print x
    db.close()
