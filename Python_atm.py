print("Welcome to the Python ATM")
Password = int(input("Please enter your Bank Password"))
if Password == 436875534533:
    print("Account Logged in")
    Balance = 100
    Withdraw = float(input("How much money do you want to withdraw?"))
    if Withdraw <= 100:
        NewBalance = (100 - Withdraw)
        print(f"New Balance = {NewBalance}")
    else:
        print("Withdraw failed")
else:
    print("Login Failed")
