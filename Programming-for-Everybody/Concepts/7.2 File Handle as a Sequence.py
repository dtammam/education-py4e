'''
File Handle as a Sequence

    - A file handle open for read can be treated as a sequence of strings where each line in the file is a string in the sequence
    - We can use the for statement to iterate through a sequence
    - Remember - a sequence is an ordered set
'''
xfile = open *('mbox.txt')
for cheese in xfile:
    print(cheese)