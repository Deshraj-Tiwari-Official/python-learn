string = "This is written in the file using python code."

with open("./written.txt", "w") as f:
    f.write(string)
