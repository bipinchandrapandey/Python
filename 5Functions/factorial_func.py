def factorial(a):
    factorial = 1
    if a==0:
        return 1
    else:
        for i in range(1,a+1):
            factorial *=i
    return factorial
        
print(factorial(5))