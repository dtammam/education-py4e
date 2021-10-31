'''
Fine-Tuning Your Match

    - Depending on how "clean" your data is and the purpose of your application, you may want to narrow your search down a bit
'''
# I'm looking for lines that start with X followed by any number of characters followed by a colon.

# ^X.*:
    # X-Sieve: CMU Sieve 2.3
    # X-DSPAM-Result: Innocent
    # X-Plane is behind schedule: two weeks

# I'm looking for lines that start with X followed by a dash followed by any non-whitespace character at least one time followed by a colon.

# ^X-\S+:
    # X-Sieve: CMU Sieve 2.3
    # X-DSPAM-Result: Innocent