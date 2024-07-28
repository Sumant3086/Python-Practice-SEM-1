def fun():
    global i
    if i == 10:return
    i=i+1
    if i%2==0:
        print(i)
        fun()
i=0
fun()



start, end = 1, 10
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num % 2 == 0:
        print(num, end = " ")
