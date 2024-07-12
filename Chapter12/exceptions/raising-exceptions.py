n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

if n2 == 0:
    raise ZeroDivisionError("Cannot divide by zero")
else:
    print(n1 / n2)
