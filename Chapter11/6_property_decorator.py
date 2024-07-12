class Student:
    def __init__(self):
        # This is a good practice to do, but it can work without doing this. So, do not be confused.
        self.firstName = None
        self.lastName = None

    @property
    def name(self):
        return f"{self.firstName} {self.lastName}"

    @name.setter
    def name(self, value):
        self.firstName = value.split(" ")[0]
        self.lastName = value.split(" ")[1]


deshraj = Student()
# name is the NAME of the function (property wala) but actually, it is setting up firstName and lastName using the setter function that is running on the property decorator.
deshraj.name = "Deshraj Tiwari"

print(deshraj.firstName)
print(deshraj.lastName)

# __init__ is used for initializing instance attributes during object creation, whereas property with a setter method allows for customizing attribute access and behavior beyond simple assignment.
