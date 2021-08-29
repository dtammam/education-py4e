'''
Counting Lines in a File
    - Open a file read-only
    - Use a for loop to read each line
    - Count the lines and print out the number of lines
'''

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line count:', count)