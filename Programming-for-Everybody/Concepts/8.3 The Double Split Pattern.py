'''
The Double Split Pattern

    - Sometimes we split a line one way, and then grab one of the pieces.
    - We then split that piece again.
'''
# Example line
# From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    print(pieces[1])
    # This prints out the actual email domain for each line!