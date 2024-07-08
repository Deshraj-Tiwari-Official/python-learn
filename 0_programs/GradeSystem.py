# Marks Obtained => Grade
# 90 - 100 => A
# 80 - 89 => B
# 70 - 79 => C
# 60 - 69 => D
# Below 60 => F

# Create a grade system using conditionals. The marks should be entered by the user itself.
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Your grade is A")
elif marks >= 80:
    print("Your grade is B")
elif marks >= 70:
    print("Your grade is C")
elif marks >= 60:
    print("Your grade is D")
else:
    print("Your grade is F")
