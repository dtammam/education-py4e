'''
Opening a File

    - Before we can read the contexts of the file, we must tell Python which file we are going to work with and what we will be doing with the file
    - This is done with the open() function
    - open() returns a "file handle" - a variable used to perform operations on the file
    - Similar to "File -> Open" in a Word Processor

	Using open()
		- handle = open(filename, mode)
		- Returns a handle used to manipulate the file
		- Filename is a string
        - Mode is optional and should be 'r' if we are planning to read the file and 'w' if we are going to write to the file
        - fhand = open('mbox-short.txt', 'r'
'''
fhand = open('mbox-short.txt')
print(fhand)