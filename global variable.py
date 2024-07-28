#Program to illustrate Global variable access
globvar = "Hello"
def test1():
	global globvar
	globvar = "Good Morning" 
def test2():
	# Here this is a local variable
	globvar = "Night Night"
print(globvar) # The first value "Hello" is printed
test1()
test2()
print(globvar) # The updated value of test1 is printed
