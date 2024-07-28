data = input("data: ")
list1 = data.split(",")
tuple1 = tuple(list1)
print("tuple:", tuple1)
element = input("element: ")
if element in tuple1:
	index = tuple1.index(element)
	print("index:", index)
else:
	print("enter an element that exists in tuple")
