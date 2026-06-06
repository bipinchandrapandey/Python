f = open('poem.txt', "r")
text = f.read()
if("twinkle" in text):
    print("Twinkle is present in the poem.")
else:
    print("Twinkle is not present in the poem.")

