'''
Musical Track Database

    This application will read an iTunes export file in XML and produce a properly normalized database with this structure:

        CREATE TABLE Artist (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name    TEXT UNIQUE
        );

        CREATE TABLE Genre (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name    TEXT UNIQUE
        );

        CREATE TABLE Album (
            id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            artist_id  INTEGER,
            title   TEXT UNIQUE
        );

        CREATE TABLE Track (
            id  INTEGER NOT NULL PRIMARY KEY 
                AUTOINCREMENT UNIQUE,
            title TEXT  UNIQUE,
            album_id  INTEGER,
            genre_id  INTEGER,
            len INTEGER, rating INTEGER, count INTEGER
        );

    If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

    You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip. 
    The ZIP file contains the Library.xml file to be used for this assignment. 
    You can export your own tracks from iTunes and create a database, but only use the Library.xml data that is provided to turn in your assignment.

    To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:

        SELECT Track.title, Artist.name, Album.title, Genre.name 
        FROM Track JOIN Genre JOIN Album JOIN Artist ON Track.genre_id = Genre.ID and Track.album_id = Album.id AND Album.artist_id = Artist.id
        ORDER BY Artist.name LIMIT 3

    The expected result of the modified query on your database is: (shown here as a simple HTML table with titles)

        Track   Artist  Album	Genre
        Chase the Ace   AC/DC   Who Made Who    Rock
        D.T.    AC/DC   Who Made Who    Rock
        For Those About To Rock (We Salute You) AC/DC   Who Made Who    Rock
'''
# Import our relevant modules
import xml.etree.ElementTree as ET
import sqlite3

# Connect and open our database connection
conn = sqlite3.connect('exercise15.8.sqlite')
cur = conn.cursor()

# Make some fresh tables as required using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, 
    rating INTEGER, 
    count INTEGER
);
''')

# Open our XML file
fname = input('Enter file name: ')
if ( len(fname) < 1 ) : fname = 'Library.xml'

# Some reference data of what the XML nodes look like
    # <key>Track ID</key><integer>369</integer>
    # <key>Name</key><string>Another One Bites The Dust</string>
    # <key>Artist</key><string>Queen</string>

# Define a function to lookup an item in a node via loop
def lookup(node, key):
    found = False
    for child in node:
        if found : return child.text
        if child.tag == 'key' and child.text == key :
            found = True
    return None

# Parsing out the XML file for relevant information into a dictionary
stuff = ET.parse(fname)
all = stuff.findall('dict/dict/dict')
print('Dict count:', len(all))

# For loop to lookup within nodes of XML for our relevant data
for entry in all:
    if ( lookup(entry, 'Track ID') is None ) : continue
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    genre = lookup(entry, 'Genre')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')

    # Keep going if nodes are empty
    if name is None or artist is None or album is None or genre is None : continue

    # Print out the results in a terminal as we process each line
    print(name, artist, album, genre, count, rating, length)

    # Insert the name of the artist into the artist table
    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )

    # Select the id (primary key) of the artist and fetch the foreign key of track (artist_id)
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    # Insert the title of the album and the artist_id into the Album table
    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )

    # Select the id (primary key) of the album and fetch the foreign key of track (album_id)
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]
   
    # Insert the name of the genre into the Genre table
    cur.execute('''INSERT OR IGNORE INTO Genre (name) 
        VALUES ( ? )''', ( genre, ) )

    # Select the id (primary key) of the genre and fetch the foreign key of track (genre_id)
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
    genre_id = cur.fetchone()[0]

    # Insert the title, album_id, len, rating, count and genre_id of the track
    cur.execute('''INSERT OR REPLACE INTO Track
        (title, album_id, len, rating, count, genre_id) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, length, rating, count, genre_id ) )

    # Write all changes to the database
    conn.commit()

    # Similar query that the database will be checked against for grading:
    cur.execute('''SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3''')