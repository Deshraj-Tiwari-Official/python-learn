def even(n):
    if n % 2 == 0:
        return True
    return False


# filter function
onlyEven = filter(even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(list(onlyEven))
