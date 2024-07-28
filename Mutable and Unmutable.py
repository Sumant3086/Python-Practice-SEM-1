#mubtable can change
#immutable cannot change like tuple

tp=(2,)
print(tp)

a=1
b=4
temp=a
a=b
b=temp
print(a,b)

a=1
b=4
a,b=b,a
print(b,a)