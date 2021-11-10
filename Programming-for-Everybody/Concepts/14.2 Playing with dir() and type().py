'''
Playing with dir() and type()

	- The dir() command lists capabilities (or methods)
	- Ignore the ones with underscores, these are used by Python itself
	- The rest are real operations that the object can perform
    - It is like type(), it tells us something *about* a variable
'''
y = list()
print(type(y))
print(dir(y))