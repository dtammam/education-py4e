'''
Counting Email in a Database

    - Connection checks access to the file, creates file if it doesn't exist
    - Cursor is kind of like our file handle
    - DROP TABLE prevents blowup if we don't start with a fresh database, otherwise it does nothing
    - Tuples are used and need to be populated, for example (email,) with the second half being empty on purpose
    - Question mark is a value within a tuple
    - Atomic increment/decrement operations are cool and allow you to safely number things
'''
# Import relevant modules.
import sqlite3

# Open the connection.
conn = sqlite3.connect('emaildb.sqlite')
# Interact with the file using cursor.
cur = conn.cursor()

# Drop table if it exists to start, makes it repeatable/displays fresh data.
cur.execute('''
DROP TABLE IF EXISTS Counts''')

# Create our new table.
cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

# Open a file, looping through for email addresses per line.
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fhand = open(fname)
for line in fhand:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    # Execute by selecting the count column from our Counts table with any email in it to start. Remember to sanitize your inputs!
    # https://imgs.xkcd.com/comics/exploits_of_a_mom.png
    cur.execute('SELECT count FROM Counts WHERE email = ?', (email,))
    # Row is the information we get from the database.
    row = cur.fetchone()
    # If there are no records that meet this, the row is None.
    if row is None:
        # If there's nothing in the row, we need to insert our value based on our tuple. If it's not there, insert it.
        cur.execute('''INSERT INTO Counts (email, count)
        VALUES (?, 1)''', (email,))
    else:
        # If there is something in the row, give it a count. Updating is safer due to it using atomic numbers and that it won't conflict with other code that may be running. If it's there, update it.
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?', (email,))
    # Write to disk.
    conn.commit()

# Read our database, selecting email and count from Counts, order it by the count in descending order, and show the top 10.
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

# Ask for the rows one at a time. They are tuples, row[0] is the email, row[1] is the count.
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

# Close the connection, and away we go!
cur.close()