# Challenge: MAKE THIS USING A WHILE LOOP
names = ["Deshraj Tiwari", "Dhruv Rathee", "Akshit Yadav", "Praful Ranjan", "Digraj Singh Rajput"]

i = 0
while i < len(names):
    if names[i].startswith("D"):
        print("Hello " + names[i])
    i += 1
