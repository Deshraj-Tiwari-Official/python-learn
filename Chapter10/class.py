class Employee:
    """
    This class is used to create an employee.
    The attributes are name, name and salary.
    """

    # __<method>__ are called dunder methods.
    # __init__ is called automatically when a class is created. Thus, we define the attributes in this constructor
    def __init__(self, name, age, salary):
        # The self attribute is used to access the attributes and methods of the class
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(self.name, self.age, self.salary)

    @staticmethod  # Static method means that it does not need an instance of the class to be called
    def greet():
        print("Hello")


# Deshraj is an object of the class Employee
deshraj = Employee("Deshraj", 15, 100000)  # You can set the attributes like this
deshraj.salary = 150000  # Or like this
deshraj.email = "deshrajtiwari690@gmail.com"  # You can also set new attributes that would be set only for the object you create it for

deshraj.display()
Employee.greet()
