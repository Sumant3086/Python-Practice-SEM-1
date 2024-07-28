data1 = input("data1: ")
list1 = data1.split(",")
data2 = input("data2: ")
list2 = data2.split(",")
if list1[0] == list2[0] or list1[-1] == list2[-1]:
	print("True")
else:
	print("False")
