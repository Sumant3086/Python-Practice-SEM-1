def compose (*functions):  
	def inner(arg):
		for f in reversed(functions):
			arg = f(arg)
		return arg
	return inner
#Define three functions
def square (x):
	return x ** 2
def increment (x):
	return x + 1
def half (x):
	return x / 2
# call with 3 functions
composed = compose(square, increment, half) # square(increment(half(x)))
print(composed(5)) # square(increment(half(5))) = square(increment(2.5)) = square(3.5) = 12.25# call with 2 functions
composed = compose(square, increment) #square(increment(5)) = square(6) = 36
print(composed(5))



def return(num):
    return num
def retdouble(num):
    return num*2
def retthrice(num):
    return num*3
def retfourtime(num):
    return num*4

def printfunction(*num):
    for i in num:
        print("the final number is",i)

printfunction(retnum(2),retdouble(2))
print("After the first function call")
printfunction(retnum(2),retdouble(2),retthrice(2),retfourtime(2))
    