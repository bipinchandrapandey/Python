def count_word(sentences):
    text = sentences.split(" ")
    count = 0
    for i in text :
        count+=1
    return count
print(count_word("hello jee kaise hai aap thik hain"))