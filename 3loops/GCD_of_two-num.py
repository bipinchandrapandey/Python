num1, num2 = map(int, input("Enter two number: ").split(','))
if(num1>num2):
    for i in range(1, num2+1):
        if(num1%i==0 and num2%i==0):
            GCD = i
    print("GCD is %d"% GCD)
if(num1<num2):
    for i in range(1, num1+1):
        if(num1%i==0 and num2%i==0):
            GCD = i
    print("GCD is %d"% GCD)

# num1, num2 = map(int, input("Enter two numbers: ").split(','))

# small = min(num1, num2)

# for i in range(1, small + 1):
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i

# print("GCD is", gcd)