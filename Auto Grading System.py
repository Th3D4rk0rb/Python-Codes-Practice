Attendence = int(input("Of what percentage has this student been present?"))
Grade = int(input("What is the grade this students has recieved in the test?"))
if Attendence < 75:
    print("Error, ineligible for grading due to low attendance") 
else:
     if Grade >= 90 and Grade < 100:
         print("Grade = A")
     elif Grade < 89 and Grade > 70:
         print("Grade = B")
     elif Grade < 69 and Grade >50:
         print("Grade = C")
     else:
         print("Grade = F")
