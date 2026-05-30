num = int(input("Enter a number: "))
if(num%11==0 and num %5==0):
    print(" This number is divisible by both 11 and 5")

elif(num%5==0):
    print("This is divisible by only 5")

elif(num%11==0):
    print("This is divisible by 11")
else:
    print(" This is not divisible by both 11 and 5")