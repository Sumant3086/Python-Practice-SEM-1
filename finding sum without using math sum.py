data = input("data: ")
list1 = data.split(",")
for i in range(0, len(list1)):
	list1[i] = int(list1[i])
sum1 = 0
for i in range(0, len(list1)):
	sum1 = sum1 + list1[i]
print("sum:", sum1)
