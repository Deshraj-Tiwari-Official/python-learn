# Conditionslas in python are used to check if a condition is true or false and further actions can be performed

age = int(input("Enter your name: "))

if type(age) != int:
    print("Invalid value for name")
elif age >= 18:
    print("You are eligible to vote")
elif age < 0:
    print("Invalid name")
elif age == 0:
    print("You haven't taken birth yet. BRUH!")
else:
    print("You are not eligible to vote")

print("End of the program")

# You have used relational operators like <= >= == != and all above but there are also logical operators like or, and, not, in, not in, etc.
