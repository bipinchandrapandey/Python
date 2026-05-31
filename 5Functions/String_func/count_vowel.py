def count_vowel(text):
    count =0
    lower = text.lower() 
    
    for i in lower:
        if(i == "a" or i=="e" or i=="i"  or i=="o"  or i=="u" ):
            count +=1
        
    return count


print(count_vowel("atesoioQu"))