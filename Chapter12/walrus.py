# You can use walrus operator to assign a value to a variable within any block of code

if (n := int(input("Enter a number: "))) > 0:
    print(f"{n} is a positive number")
else:
    print(f"{n} is a negative number")
