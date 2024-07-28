data = input("data: ")
list1 = data.split(",")
size = len(list1)
for i in range(size):
	list1[i] = int(list1[i])
max_val = max(list1)
min_val = min(list1)
print("min:", min_val)
print("max:", max_val)
difference = max_val - min_val
print("difference:", difference)
