num1,num2=map(int,input("Enter two numbers: ").split(','))
bigger = max(num1,num2)
for i in range (bigger, num1*num2+1):
    if(i%num1==0 and i%num2==0):
        LCM = i
        print("The LCM is %d "%LCM)
        break

