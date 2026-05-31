def isArmstrong(num):
    if num == 0:
        return  "Armstrong Number"
    new_num = num
    original = num
    count = 0
    Armstrong = 0
    while(num !=   0):
        num = num//10
        count += 1
    while(new_num !=0):
        digit = new_num%10
        Armstrong += digit**count
        new_num = new_num//10
    if original == Armstrong:
        return "Armstrong Number"
    else:
        return "not an Armstrong number "


print(isArmstrong(3701))