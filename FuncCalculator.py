Num1 = float(input("Input your first Number"))
Num2 = float(input("Input your second Number"))
Operation = str(input("What Operation do you want to do with these numbers"))
def Add():
    Addition = Num1 + Num2
    print(f"The sum is: {Addition}")

def Sub():
    Subtraction = Num1 - Num2
    print(f"The difference is: {Subtraction}")

def Mul():
    Multipucation = Num1 * Num2
    print(f"The product is: {Multipucation}")

def Div():
    Division = Num1 / Num2
    print(f"The quotient is: {Division}")

def Pow():
    Power = Num1 ** Num2
    print(f"The exponentiation is: {Power}")

def Mod():
    Modulus = Num1 % Num2
    print(f"The modulus is: {Modulus}")

if Operation == "+":
    Add()
elif Operation == "-":
    Sub()
elif Operation == "*":
    Mul()
elif Operation == "/":
    Div()
elif Operation == "**":
    Pow()
elif Operation == "%":
    Mod()
