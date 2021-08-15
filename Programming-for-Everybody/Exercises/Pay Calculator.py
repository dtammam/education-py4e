# The purpose of this script is to determine how much the user will be paid.

# Prompt the user for all relevant inputs.
hours = input("Enter hours:")
rate = input("Enter rate:")

# Do the math and determine what pay will be.
pay = float(hours) * float (rate)

# Convert pay into a string so that it can be printed.
total = str(pay)

# Display to the user.
print("Pay: " + total)