# Recursions are the functions that re-call themselves. For example, factorial function!
# We need to be careful while using recursions so that we do not create an infinite loop

def factorial(n):
    """
    factorial(n) = n * n-1 * n-2 ......
    factorial(n) = n * factorial(n-1)

    :param n: The number to find factorial
    :return: The factorial
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")
