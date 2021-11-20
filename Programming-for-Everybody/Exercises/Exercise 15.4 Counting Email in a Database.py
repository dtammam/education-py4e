'''
Counting Email in a Database

    This application will read the mailbox data (mbox.txt) and count the number of email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.

        CREATE TABLE Counts (org TEXT, count INTEGER)

    When you have run the program on mbox.txt upload the resulting database file above for grading.
    If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.
'''
import sqlite3

conn = sqlite3.connect('exercise15.4.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fhand = open(fname)
for line in fhand:
    if not line.startswith('From: '): continue
    words = line.split()
    email = words[1]
    host = email.split('@')
    org = host[1]
        
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
        VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))
    
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()