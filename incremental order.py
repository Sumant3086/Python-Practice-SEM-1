#Program to print the given string in incremental order
str = input("str: ")
length = len(str)
result = ""
for s in range(0, length+1):
	result = result + str[:s]
print("incremental order:", result)
