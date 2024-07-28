data = input("data: " )
list1 = data.split(",")
print("before updation:", list1)
index = int(input("index: "))
if index < len(list1) and index >= -(len(list1)):
	value = input("element: ")
	list1[index] = value
	print("after updation:", list1)
else:
	print("invalid")
	