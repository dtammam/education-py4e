'''
Prompt for File Name

    - We can prompt for a name to make the processing much simpler and automated
    - This particular code asks for a file name, opens the file, searches for lines with 'Subject:' and then prints the number of those lines
'''
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject') :
        count = count + 1
print('There were', count, 'subject lines in', fname)