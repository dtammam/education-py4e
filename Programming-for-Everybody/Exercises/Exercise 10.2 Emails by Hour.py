'''
Emails by Hour

    Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
    You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
        From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
    Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
'''
fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"

fhand = open(fname)
counts = dict()

for line in fhand :
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    time = words[5]
    hour = time[:2]
    counts[hour] = counts.get(hour,0) + 1

for time,hour in sorted(counts.items()):
    print(time, hour)
    
# Desired Output:
# 04 3
# 06 1
# 07 1
# 09 2
# 10 3
# 11 6
# 14 1
# 15 2
# 16 4
# 17 2
# 18 1
# 19 1