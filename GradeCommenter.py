def GradeAPlus():
    print("That's the best grade!")
def GradeA():
    print("That's Great!")
def GradeB():
    print("Mid")
def GradeC():
    print("Not bad")
def GradeD():
    print("Below Average")
def GradeF():
    print("You Suck")
Grade = str(input("What grade did they get?"))
if Grade == "A+":
    GradeAPlus()
elif Grade == "A":
    GradeA()
elif Grade == "B":
    GradeB()
elif Grade == "C":
    GradeC()
elif Grade == "D":
    GradeD()
elif Grade == "F":
    GradeF()
