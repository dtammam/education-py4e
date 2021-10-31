'''
Searching Through a File

    - We can put an if statement in our for loop to only print lines that meet some criteria
    - You'll notice blank lines
    - Each line from the file has a newline at the end
    - The print statement adds a newline to each line
'''
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:') :
        print(line)