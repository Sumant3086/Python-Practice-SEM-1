def pyramid(p):
   for m in range(0, p):
      for n in range(0, m+1):
         print("* ",end="")
      print("\r")
p = 10
pyramid(p)

num_rows = int(input("Enter the number of rows: "))
a=1
for i in range(0,num_rows):
    for j in range(0,a):
        print("j+1",end="")
    a=a+1
    print()