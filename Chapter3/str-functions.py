name = "deshraj Tiwari"

# Calculates the length of the string
print(len(name))

# Checks if the string ends with the specified suffix
print(name.endswith("ari"))

# Checks if the string starts with the specified prefix (case sensitive)
print(name.startswith("De"))

# Capitalizes the first character of the string and converts all other characters to lowercase
print(name.capitalize())

# Convert the entire string to uppercase
print(name.upper())

# Convert the entire string to lowercase
print(name.lower())

# Count occurrences of a substring within the string
print(name.count("i"))

# Find the index of the first occurrence of a substring
print(name.find("raj"))

# Replace occurrences of a substring with another substring
print(name.replace("raj", " Kumar"))

# Split the string into a list of substrings using a delimiter (default is whitespace)
print(name.split())

# Join elements of a list into a single string with a specified delimiter
words = ["deshraj", "Tiwari"]
print(" ".join(words))