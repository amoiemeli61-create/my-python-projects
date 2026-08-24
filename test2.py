temp = float(input("Enter temperature:"))
if temp< 10:
    print("cold")
elif 10<=temp<=25:
    print("Moderatore")
else:
    print("Hote")
unit = input("Enter temperature unit F/C:")
if unit == "F":
    f = (temp* 9 / 5) + 32
    print("Fahrenheit", f)
elif unit == "C":
    c = (temp - 32) * 5 / 9
    print("Celsius", c)
else:
    print("Invalid unit")
