import time
t = time.strftime('%H:%M:%S')
hour= int(time.strftime('%H'))
print(hour)
if(hour>=0 and hour<12):
    print("Good morning time is %d" %hour)
elif(hour>=12 and hour<16):
    print("Good after noon time is %d" %hour)
elif(hour>=16 and hour<20):
    print("Good evening time is %d" %hour)
else:
    print("Good night time is %d" %hour)
