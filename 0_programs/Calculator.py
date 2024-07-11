class Calculator:
    """
    A class to perform basic arithmetic operations.

    Attributes:
        n1 (int): The first number.
        n2 (int): The second number.
    """
    def __init__(self, n1, n2):
        """
        Initialize the Calculator object with two numbers.

        Args:
            n1 (int): The first number.
            n2 (int): The second number.
        """
        self.n1 = n1
        self.n2 = n2

    def add(self):
        """
        Add the two numbers and print the result.
        """
        print(self.n1 + self.n2)

    def subtract(self):
        """
        Subtract the second number from the first and print the result.
        """
        print(self.n1 - self.n2)

    def multiply(self):
        """
        Multiply the two numbers and print the result.
        """
        print(self.n1 * self.n2)

    def divide(self):
        """
        Divide the first number by the second and print the result.

        Raises:
            ZeroDivisionError: If the second number is zero.
        """
        if self.n2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        print(self.n1 / self.n2)


num1 = int(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
num2 = int(input("Enter the second number: "))

obj = Calculator(num1, num2)

if operation == "+":
    obj.add()
elif operation == "-":
    obj.subtract()
elif operation == "*":
    obj.multiply()
elif operation == "/":
    try:
        obj.divide()
    except ZeroDivisionError as e:
        print(e)
else:
    print("Invalid operation")