def LCM(a, b):
    a = abs(a)
    b = abs(b)

    if a == 0 or b == 0:
     return 0
    large = max(a,b)
    lcm =0
    for i in range(large,(a*b)+1):
        if i%a==0 and i%b==0:
            lcm = i
            break
    return lcm
    
print(LCM(8,12))