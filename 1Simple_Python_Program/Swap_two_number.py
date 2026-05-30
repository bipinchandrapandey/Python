a,b = map(int, input("Enter two number for swaping: ").split(','))
print("before swaping a=%d and b=%d"%(a,b))
# a,b = b,a
a=a+b
b=a-b
a=a-b
print("after swaping a =%d and b=%d"%(a,b))