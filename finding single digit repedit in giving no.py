str1 = (input("str: "))
printed = []
for y in str1:
	if(y not in printed):
		print(y,"\t", (str1.lower()).count(y))
		printed.append(y)
