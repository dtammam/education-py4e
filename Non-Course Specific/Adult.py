# Adult.py

fname = 'deantammam.txt'
fhand = open(fname)

print("Let's get a move on!")
counts = {}
skills = 'Not enough'

for line in fhand:
    line = line.rstrip()
    if not line.startswith('I can do ') : continue
    words = line.split()
    skill = words[3]
    counts[skill] = counts.get(skill, 0) + 1

for skill,count in sorted(counts.items()):
    print("Not enough!")

fhand.close(fname)