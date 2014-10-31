import sqlite3

def create_account(account_name='saving'):
    db = sqlite3.connect('Bank.db')

    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Transactions(transactionID INTEGER PRIMARY KEY, accountID INTEGER, type TEXT, amount INTEGER)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Accounts(accountID INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('INSERT INTO Accounts(name)VALUES(?)', (account_name,))
    db.commit()

    db.close()

def deposit(amount, account):
    db = sqlite3.connect('Bank.db')

    cursor = db.cursor()
    cursor.execute('SELECT accountID FROM Accounts WHERE Accounts.name = (?)', (account,))
    ACCOUNT = cursor.fetchone()[0]
    cursor.execute('INSERT INTO Transactions(accountID, type, amount)VALUES(?, ?, ?)', (ACCOUNT, 'Deposit', amount))
    db.commit()

    db.close()

def withdraw():
    db = sqlite3.connect('Bank.db')

    cursor = db.cursor()
    db.commit()

    db.close()

def output():
    db = sqlite3.connect('Bank.db')
    cursor = db.cursor()
    db1 = cursor.execute('SELECT name, accountID FROM Accounts')
    for row in db1:
        print 'Account: ', row[0]
        print 'accountID: ', row[1]
        print '---------------'
    db2 = cursor.execute('SELECT amount, transactionID, accountID FROM Transactions')
    for row in db2:
        print 'Amount: ', row[0]
        print 'transactionID: ', row[1]
        print 'accountID: ', row[2]
    # cursor.execute('SELECT * FROM Accounts')
    # p = cursor.fetchall()
    # for x in p:
    #     print x
    db.close()

def transaction_receipt():
    db = sqlite3.connect('Bank.db')

    cursor = db.cursor()
    transaction_history = cursor.execute('SELECT amount, transactionID, accountID FROM Transactions')
    for row in transaction_history:
        print 'Amount: ', row[0]
        print 'transactionID: ', row[1]
        print 'accountID: ', row[2]

    db.close()
