def ispalindrome(num):
    new_num = num 
    reverse =0 
    while(num !=0):
        digit = num%10
        reverse = (reverse*10)+digit
        num =num//10
    if reverse == new_num:
        return "Palindrome number"
    else:
        return " Not Palindrome"

print(ispalindrome(12345654321))