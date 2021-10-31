'''
Counting in a Loop

    - The example below shows how to count on our variable
    - We continually loop through, checking to see if we satisfy the condition
    - After 7, we're done
'''
plumbus = 0
print('This is the magic counting machine. It breaks after 7 plumbuses, so avoid doing this.')
print('Before', plumbus)
for bibbitybop in [9, 41, 12, 3, 74, 15, 95, 2] :
    plumbus = plumbus + 1
    if plumbus >= 7 :
        print('Um, did you not read the instructions? The machine is now broken...')
        break
    print(plumbus, bibbitybop)

print('After', plumbus)