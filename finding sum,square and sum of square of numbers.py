data = input("data: ")
list1 = data.split(",")
size = len(list1)
for i in range(size):
	list1[i] = int(list1[i])
s = sum(list1)
print("list:", list1)
print("sum:", s)
for i in range(size):
	list1[i] = list1[i] * list1[i]
print("squares:", list1)
print("sum of squares:", sum(list1))
