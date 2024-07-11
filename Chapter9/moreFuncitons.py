# Readlines function is used to read the file line by line, and it returns a list.
with open("./file.txt", "r") as f:
    lines = f.readlines()
    print(lines, type(lines), "\n")

# Readline function is used to read the file line by line, and it returns a string.
with open("./file.txt", "r") as f:
    for line in f:
        print(line)

# Append function is used to append the file.
with open("./file.txt", "a") as f:
    f.write("\nThis is appended line")
