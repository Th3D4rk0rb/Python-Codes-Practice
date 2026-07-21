Year = int(input("Hey, User please enter a 4 digit year"))
if (Year% 100 != 0 and Year % 4 == 0) or (Year % 400 == 0): 
    print("This year is a leap year")
else:
    print ("This is year is not a leap year")
