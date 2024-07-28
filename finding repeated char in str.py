str1 = input("str: ")# Get the Input string
str3 = sorted(str1)  # Sort the string
printed = [] # Blank List
for char in str3:  # For each character in the input
	if char not in printed:  # check whether printed or not
		print("'{0}'\t{1}".format(char, str3.count(char))) # print char and count
		printed.append(char) # add to printed list
print(printed)
