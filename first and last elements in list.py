data = input("data: ")
list1 = data.split(",")
for i in range(0, len(list1)):
	list1[i] = int(list1[i])
if (list1[0] == 3) or (list1[-1] == 3):
	print("True")
else:
	print("False")
