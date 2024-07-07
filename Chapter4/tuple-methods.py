myTup = ("Deshraj", 12, True, "Deshraj")

# Count the number of occurrences of "Deshraj" in the tuple
no = myTup.count("Deshraj")
print(no)  # Output: 2

# Get the index of the first occurrence of "Deshraj" in the tuple
index = myTup.index("Deshraj")
print(index)  # Output: 0

# len() is not a tuple method but a built-in function to get the length of the tuple
length = len(myTup)
print(length)  # Output: 4

# max() to get the maximum value from the tuple (works only with comparable elements)
# Example with a tuple of numbers
numTup = (1, 2, 3, 4)
maximum = max(numTup)
print(maximum)  # Output: 4

# min() to get the minimum value from the tuple (works only with comparable elements)
minimum = min(numTup)
print(minimum)  # Output: 1

# sorted() returns a sorted list of the elements in the tuple
sortedTup = sorted(numTup)
print(sortedTup)  # Output: [1, 2, 3, 4]

# Check if a value is is a tuple
print(12 in myTup)

# THERE ARE MORE THINGS TO CHECK OUT AND YOU CAN IF YOU WANT