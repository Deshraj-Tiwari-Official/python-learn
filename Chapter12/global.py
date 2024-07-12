n = 28


def fun():
    global n
    # Now the global n variable gets changed.
    n = 32
    print(n)


fun()
print(n)
