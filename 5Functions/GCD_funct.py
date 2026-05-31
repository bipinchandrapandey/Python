def HCF(a, b):
    a= abs(a)
    b= abs(b)
    if a==0 and b==0 :
        return "Undefined"
    if a==0:
        return b
    if b==0:
        return a
    smaller = min(a,b)
    value =0
    for i in range (1,smaller+1):
        if(a%i ==0 and b%i==0):
            value =i
    return value       
        

print(HCF(0,24))