a , b, c = map(int, input("Enter the three number: ").split(','))
# print(max(a,b,c))
# print(min(a,b,c))


if a >= b and a >= c:
    print("%d is greatest" % a)

elif b >= a and b >= c:
    print("%d is greatest" % b)

else:
    print("%d is greatest" % c)