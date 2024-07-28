#Using the slicing technique 
#Using the extend() method 
#List copy using =(assignment operator)
#Using the method of Shallow Copy 
#Using list comprehension 
#Using the append() method 
#Using the copy() method 
#Using the method of Deep Copy
#Using the map method 

def Cloning(li1):
    li_copy = li1[:]
    return li_copy
 
 
# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)