mySet = {1, 2, 432, 64, 9, 9, 9, 9, 9}

# If you try to make an empty set using <variableName> = {}, this will create a dictionary.
# To create an empty set, use <variableName> = set()

emptySet = set()

# All the repeated values will be removed. Only one 9 will be there
print(mySet)

# Set funcitons such as remove, len and more

# len
print(len(mySet))

# remove
mySet.remove(9)
print(mySet)

# clear
mySet.clear()
print(mySet)

# discard
mySet.discard(9)
print(mySet)

# pop
mySet.pop()
print(mySet)
