def addavg(a,b):
    sum=a+b
    avg=sum/2
    sub=a-b
    mul=a*b
    print(sub,mul,end="\n")
    return (sum,avg)
a=int(input("Enter the first number: "))
b=int(input("Enter the second number"))
print(addavg(a,b))