data = input("data: ")
list1 = data.split(",")
tuple1 = tuple(list1)
print("tuple:", tuple1)
val = input("value: ")
if val in tuple1:
	print("True")
else:
	print("False")
