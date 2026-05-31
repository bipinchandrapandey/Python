def isprime(a):
    if a<2:
        return "Neither prime nor composite"
    count =0
    for i in range(2,a-1):
        if a%i==0:
            return "composite number"
    return "prime number"

print(isprime(1))