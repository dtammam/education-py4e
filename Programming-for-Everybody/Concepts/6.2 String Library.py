'''
String Library

	- Python has a number of string functions which are in the string library
	- These functions are already built into every string - we invoke them by appending the function to the string variable
	- These functions do not modify the original string, instead they return a new string that has been altered
	- Methods, such as .lower() can be found by using dir()
    - https://docs.python.org/3/library/stdtypes.html#string-methods
'''
greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print('Hi There'.lower())