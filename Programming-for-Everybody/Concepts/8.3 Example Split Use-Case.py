'''
Example Split Use-Case

    - We'll get very used to this concept, of opening files, grabbing lines, etc.
    - With split, we actually make the lines useful as we need
    - Maintain good hygiene with our if not 'skip' code
'''
# Example line in email:
# From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])