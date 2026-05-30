Hindi = int(input("Enter the marks obtained by the student In Hndi: "))
English = int(input("Enter the marks obtained by the student In English: "))
Math = int(input("Enter the marks obtained by the student In Math  : "))
socialScience = int(input("Enter the marks obtained by the student In SocialScience: "))
Science = int(input("Enter the marks obtained by the student In Science: "))
total_marks =  int(input("Enter the  total marks all subject : "))
total_Obtained_marks = Hindi+English+Math+socialScience+Science
print("Total obtained marks is %d "%total_Obtained_marks)
percentage_of_marks = float(total_Obtained_marks * (100/total_marks))
print("percentage marks of student is %.2f"%percentage_of_marks)
if(percentage_of_marks<=100 and percentage_of_marks>=90):
    print("Grade is A+")
elif(percentage_of_marks<90 and percentage_of_marks>=80):
    print("Grade is A")
elif(percentage_of_marks<80 and percentage_of_marks>=70):
    print("Grade is B")
elif(percentage_of_marks<70 and percentage_of_marks>=60):
    print("Grade is C")
elif(percentage_of_marks<60 and percentage_of_marks>=50):
    print("Grade is D")
elif(percentage_of_marks<50 and percentage_of_marks>=0):
    print("Grade is Fail")
else :
    print("invalid number")