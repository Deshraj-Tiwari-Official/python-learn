from functools import reduce

sum = lambda x, y: x + y

print(reduce(sum, [1, 2, 3, 4, 5]))

# It runs for first two, then their sum and next one, and so on....
