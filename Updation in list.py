data=input("Enter data: ")
oldlist=data.split(",")
newlist=oldlist
index=int(input("Enter an index: "))
value=input("Enter value: ")
if index>= len(newlist) or index <=len(newlist):
    print("Invalid")
else:
    newlist(index)==value

print("oldlsit: ",oldlist)
print("newlist: ",newlist)

data = input("data: ")
list1 = data.split(",")
list2 = []
list2 = list1
print("list1 is list2:", list1 is list2)
print("list2 is list1:", list2 is list1)
index = int(input("index: "))
if index < len(list1) and index >= -(len(list1)):
	element = input("element: ")
	list1[index] = element
	print("list1 is list2:", list1 is list2)
	print("list2 is list1:", list2 is list1)
else:
	print("enter valid index")
