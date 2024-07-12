class Employee:
    name = "Deshraj"
    age = 15
    salary = 100000

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    @classmethod  # It has the values that are pre-determined in the class.
    def displayClassValues(cls):
        print(cls.name, cls.age, cls.salary)

    def displayObjectValues(self):
        print(self.name, self.age, self.salary)


myEmp = Employee("Raj", 20, 150000)

# Even if I am calling it on a unique object, it will still print out the default class values because of the class method
myEmp.displayClassValues()

# This will print out the object values
myEmp.displayObjectValues()
