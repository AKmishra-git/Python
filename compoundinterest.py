
principle = float(input("Enter your principle: "))
rate = int(input("Enter your rate: "))
time = int(input("Enter your time in years: "))

while principle<=0:
    float(input("Enter your principle: "))
    if principle<=0:
        print("principle cant be less than 0")

while rate <=0:
     int(input("Enter your rate of interest: "))
     if rate <=0:
         print("Invalid rate")

while time<=0:
      int(input("Enter the time in years: "))
      if time<=0:
          print("Enter correct time")

CI = principle* pow((1+rate/100), time)
print(f"The compound interest is: RS {CI}")




