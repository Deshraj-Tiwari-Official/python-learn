myList = ["Deshraj", 15, True, ["Good Boy", 69]]

# You can chang the list itself as they are mutable
myList.append("Added At Last")
print(myList)

l1 = [21,32,23,2,85,43,5,53,64]

# Sort the list of numbers in ascending orger
l1.sort()
print(l1)

# Used to reverse the list
l1.reverse()
print(l1)

# The first property tells what'd be the index where it gets inserted and the other is the value
l1.insert(3, 190)
print(l1)

# Removes the value of the index mentioned
l1.pop(3)
print(l1)

# You can get the popped value as well
print(myList.pop(0))

# There are more methods like remove and such (chatGPT OP)