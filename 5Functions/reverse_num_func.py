def reverse(a):
    reverse =0
    while(a !=0):
        digit = a%10
        reverse = (reverse*10)+ digit
        a = a//10
    return reverse
print(reverse(1023456789))