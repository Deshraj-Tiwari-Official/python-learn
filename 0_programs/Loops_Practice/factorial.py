num = int(input("Enter a number: "))

fact = 1
for i in range(1, num + 1):
    if num == 0 or num == 1:
        fact = 1
        break
    fact *= i
print(fact)
