'''
Bad File Names

    - If a user were to input a bad file name… it would blow up
    - We can build in mechanisms to deal with that using a try/except block
'''
fname = input('Enter the file name:   ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

count = 0
for line in fhand:
    count = count + 1
print('There were', count, 'subject lines in', fname)