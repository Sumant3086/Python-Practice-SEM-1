data = input("data: ")
list1 = data.split(",")
list2 = []
for i in range(len(list1)):
	if list1[i] not in list2:
		list2.append(list1[i])
print(list1)
print("after removing duplicates:", list2)
