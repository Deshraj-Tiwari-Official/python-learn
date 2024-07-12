class Employee:
    def __init__(self, name, age, salary):
        print("Constructor of Employee ran")
        self.name = name
        self.age = age
        self.salary = salary

    def displayEmployeeData(self):
        print(self.name, self.age, self.salary)


class Coder:
    def __init__(self, language):
        print("Constructor of Coder ran")
        self.language = language

    def displayCoderData(self):
        print(self.language)


class Programmer(Coder, Employee):
    def __init__(self, name, age, salary, language, designation):
        print("Constructor of Programmer ran")
        self.designation = designation
        Coder.__init__(self, language)
        Employee.__init__(self, name, age, salary)

    def displayProgrammerData(self):
        print(self.name, self.age, self.salary, self.language, self.designation)

# You can inherit the data from from than one class into a class
