class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Number(self.value + other.value)

    # The str method is used to return the string representation of the object
    def __str__(self):
        return str(self.value)


a = Number(10)
b = Number(5)

result = a + b
print(result)

"""
    If you had not used the operator overloading methods, there would not be the result shown as a and b are objects and you are not supposed to add objects in python. Operator Overloading makes this work using dunder methods for arithmetic calculations.
"""