for i in range(10):
    if i == 5:
        # Skips the whole loop if the statement gets satisfied
        break
    print(i)

for i in range(10):
    if i == 5:
        # Skips the current iteration if the statement gets satisfied
        continue
    print(i)

for i in range(10):
    # Does nothing. You can skip some function/loop or something to work on something else
    pass
