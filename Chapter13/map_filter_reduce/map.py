myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squareFunc = lambda x: x ** 2
sqlist = map(squareFunc, myList)

print(list(sqlist))
