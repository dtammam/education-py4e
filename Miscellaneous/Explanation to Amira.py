""" 3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly 
rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a 
rate of 15 per hour to test the program (the pay should be 712.50). You should use input to read a string and 
float() to convert the string to a number. Do not worry about error checking the user input - assume the user 
types numbers properly. """

# # Determine hours, rate and overtime rate.
# hours = float(input("How many hours have been worked?"))
# rate = float(input("What is your hourly rate?"))
# otrate = rate * 1.5

# # Deal with any OT hours, if they exist. If not, just deal with regular hours.
# if hours > 40 :
#     othours = hours - 40
#     hours = 40

# elif hours <= 40 : 
#     othours = 0
#     hours = hours

# # Do the math to figure out how much to pay!

# regpay = hours * rate
# otpay = othours * otrate
# grosspay = str(regpay + otpay)

# print('Total pay is ' + grosspay)

x = 123

print(type(x))

print(type(float(x)))
