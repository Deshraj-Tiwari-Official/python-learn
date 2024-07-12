class Employee:
    def __init__(self, name, age, salary):
        print("Constructor of Employee ran")
        self.name = name
        self.age = age
        self.salary = salary


class Programmer(Employee):
    # The below function is the init constructor of this class. It calls the init constructor of the parent class using the super function and passes the name, salary and name attributes from its init to the parent's init. Then it defines the language attribute for itself only.
    def __init__(self, name, age, salary, language):
        print("Constructor of Programmer ran")
        super().__init__(name, age, salary)  # You will also see constructor of Employee ran
        self.language = language


# employ = Employee("Harry", 25, 100000)
prog = Programmer("Deshraj", 15, 150000, "Python")
