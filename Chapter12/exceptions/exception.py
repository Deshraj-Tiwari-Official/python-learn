try:
    number: int = int(input("Enter a number: "))
    print(number)

except ValueError as v:
    print(v)

except Exception as e:
    print(e)
