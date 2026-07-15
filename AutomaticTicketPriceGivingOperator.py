Age = int(input("How old are you?"))
if Age <= 12:
    print("The ticket price is $10")
elif Age > 12 and Age <= 65:
    print("The ticket price is $15")
else:
    print("The ticket price is $12")
