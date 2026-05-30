num = int(input("Enter the Number: "))

new = num
new1 = num
count = 0
armstrong = 0


while(num != 0):
    count += 1
    num = num // 10
    
while(new != 0):
    digit = new % 10
    armstrong += digit ** count
    new = new // 10


if(new1 == armstrong):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")