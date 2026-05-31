


def count_consonants(text):
    count =0

    vowels = "aeiou"
    
    for i in text.lower() :
        if(i not in vowels and i.isalpha()):
            count +=1
    return count


print(count_consonants("ates123@%oioQu"))