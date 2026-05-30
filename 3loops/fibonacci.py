num = int(input("Enter the number of terms: "))
n=0
m=1
print(n)
print(m)
for i in range(2,num):
    fibo = n+m
    print(fibo)
    n =m
    m = fibo
