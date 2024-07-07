# Also used to store data like lists but in a key value pair.
marks = {
  "Deshraj": 80,
  'Praful': 58,
  "Abhishek": 69
}

print(marks, type(marks))
print(marks["Praful"])

# Dictionaries in python is mutable
marks["Deshraj"] = 100
print(marks["Deshraj"])

# Methods for dictionaries
print(marks.keys())
print(marks.values())
print(marks.items())

# There is another way to change the value of a key in a dictionary
marks.update({"Deshraj": 90})
print(marks["Deshraj"])

# If there is not any key mentioned in the update method then it will create a new key
marks.update({"Harry": 100})
print(marks)

# If you use square brackets, to search for a key which is not present, it will give an error while if you use get method, it will return None
print(marks.get("Rohan"))



# The following are some more methods of dictionaries in python that are used a lot

# To check if a key is present in the dictionary
print("Deshraj" in marks)

# To get the length of the dictionary
print(len(marks))

# To clear the dictionary
marks.clear()
print(marks)

# To delete the dictionary
del marks
print(marks)