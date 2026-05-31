def isPalindrome_str(a):
    a = a.replace(" ", "")
    s = a[::-1]
    if a==s :
       return "palindrome"
    else:
        return "not palindrome"

print(isPalindrome_str("helehheleh "))