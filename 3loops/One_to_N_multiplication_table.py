num = int(input("Enter The number for multiplication table "))
for i in range(1,num+1):
     print(f"\nTable of {i}", sep=" ")
     for j in range(1,11 ):
        table = i*j
        print(table, end=" ")
     
 