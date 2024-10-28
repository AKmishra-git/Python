unit = input("ENTER THE TEMP IN CELSIUS OR FARHENHEIT (C/F): ")

temp = float(input("ENTER THE VALUE: "))

if unit == "C":
    temp = (1.8*temp) + 32
    print(f"The Temperature is {temp} degree farhenheit ")
elif unit == "F":
    temp = 0.55*(temp-32)
    print(f"The temperature is {temp} degree celsius")

else:
    print("INVALID RESPONSE")
