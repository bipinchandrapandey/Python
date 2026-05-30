n = int(input("Enter a number: "))
factorial =1
i=1
# while(i<=n):
#     factorial *= i
#     i=i+1
for i in range(1,n+1):
    factorial *= i

print("factorial of %d is %d"%(n,factorial))