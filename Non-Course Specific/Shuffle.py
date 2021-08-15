import time

# Prompt user and set variables about the number of chips
numchips = int(input("Enter the number of chips in each stack: "))
numchips2 = numchips * 9
doublenumchips = numchips * 2

# start timer
start = time.time()

# Initialize variables
stack1 = []
stack2 = []
stack3 = []
counter = 1
newstack1 = []
newstack2 = []
finished = False
totalnum = 0

# Create two stacks of chips where each stack is equal to what the user entered
for index in range(0, numchips):
    stack1.append(1)
for index in range(0, numchips):
    stack2.append(9)

# Execute the first shuffle to combine our 2 stacks into 1 shuffled stack
for index in range(0, numchips):
    stack3.append(stack2[index])
    stack3.append(stack1[index])

# Here is where the shuffling gets done along with checking to see if we are sorted again.
while finished == False:
    if totalnum == numchips or totalnum == numchips2:
        print("\n")
        print(
            "Shuffling 2 stacks of",
            numchips,
            "chips took",
            counter,
            "times to get sorted again.",
        )
        finished = True
        print("It took", round(time.time() - start, 2), "seconds to calculate this.")
        print("\n")
    else:
        stack4 = stack3.copy()
        stack3 = []
        for index in range(0, numchips):
            newstack1.append(stack4[index])
        for index in range(numchips, doublenumchips):
            newstack2.append(stack4[index])
        for index in range(0, numchips):
            stack3.append(newstack2[index])
            stack3.append(newstack1[index])

        newstack1 = []
        newstack2 = []
        stack4 = []
        counter = counter + 1

        totalnum = 0
        for index in range(0, numchips):
            totalnum = totalnum + stack3[index]
