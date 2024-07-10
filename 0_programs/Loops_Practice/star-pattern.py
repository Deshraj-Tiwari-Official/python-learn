"""
   *
  ***         -> For n = 3, print this
 *****
"""

n = int(input("Enter the number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1), end="")
    print("")

# There are more star patterns that are also pretty hard so a lot of practice is required
