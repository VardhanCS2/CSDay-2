unit=input("Enter the unit (C/F): ") .upper()
temp=float(input("Enter the temperature: "))
if unit == "C":
    print("Temperature in Fahrenheit:", (temp * 9/5) + 32)
elif unit == "F":
    print("Temperature in Celsius:", (temp - 32) * 5/9)
else:
    print("Invalid unit")