a = float(input("Enter a:"))
ch = input("Enter a char:")
b = float(input("Enter b:"))
result = None
if ch == "+":
    result = a + b
elif ch == "-":
    result = a - b
elif ch == "*":
    result = a * b
elif ch == "^":
    result = a**b
elif ch == "/":
    if b == 0:
        print("Error❌")
    else:
        result = a / b
elif ch == "%":
    if b == 0:
        print("Error❌")
    else:
        result = a % b
elif ch == "//":
    if b == 0:
        print("Error❌")
    else:
        result = a // b
elif ch == ">":
    result = a > b
elif ch == "<":
    result = a < b
elif ch == ">=":
    result = a >= b
elif ch == "<=":
    result = a <= b
elif ch == "==":
    result = a == b
elif ch == "!=":
    result = a != b
else:
    print("Invalid operator!")
if result is not None:
    print(a, ch, b, "=", result)
