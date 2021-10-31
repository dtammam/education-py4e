'''
Continuing an Iteration

    - Continue is the opposite of break
    - It allows us to continue back in the loop if we otherwise would have stopped it
'''
while True:
    
    line = input('> ')
    if line[0] == '#' :
            continue
    if line == 'done' :
            break
    print(line)

print('Done!')