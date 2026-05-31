def sum_of_digit(a):
    sum =0
    while(a!=0):
        digit = a%10
        sum += digit
        a = a//10
    return sum
print(sum_of_digit(11))



