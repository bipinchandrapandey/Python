def is_prime(n):
    if(n<=1):
        print("not prime")
    if n==2:
        print(n)
    for i in range(3,n+1):
        count =0
        for j in range(2,i):
            if i%j == 0:
               count += 1
        if count==0:
            print(i)

           
        
(is_prime(20))