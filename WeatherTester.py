Celsius = float(input("Hey, user input a temperature in celsius"))
Kelvin = Celsius + 273
print(f"{Kelvin}K")
if Celsius >= 30:
    print("It Burns!!!")
elif Celsius <= 20:
    print("It's Freezing")
else:
    print("Nice weather")
