#Program to illustrate Global and Local Variables
a = int(input("a: "))
def changeglobal():
	global a
	a = 200
def changelocal():
	a = 500
	print("local a value:", a)
print("global a before function call:", a)
changeglobal()
changelocal()
print("global a after function call:", a)
