def no_of_argu(*args):
    return(len(args))
a=1
b=5
n=no_of_argu(1,2,3,4,5,6,7)
print("The number of arguments are: ",n)



def printEvenNumbers(*nums):
    for num in nums:
        if num % 2 == 0 :
            print(num)

printEvenNumbers(20,15,5,14)
print("After the first function call:")
printEvenNumbers(20,15,5,14,30,25)
print("After the second function is called:")