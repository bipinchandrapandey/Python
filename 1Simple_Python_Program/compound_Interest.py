P = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time period: "))
n = float(input("Enter the number of times interest is compounded per year: "))

A = P * (1 + (r / (100 * n))) ** (n * t)

print("The total amount is %.2f:" % A)

I = A - P

print("The compound interest is %.2f:" % I)