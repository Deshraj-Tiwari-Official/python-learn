class Employee:
    def __init__(self, name, age, salary):
        print("Constructor of Employee ran")
        self.name = name
        self.age = age
        self.salary = salary

    def displayEmployeeData(self):
        print(self.name, self.age, self.salary)


class Coder(Employee):
    def __init__(self, language):
        print("Constructor of Coder ran")
        self.language = language

    def displayCoderData(self):
        print(self.language)


class MlEngineer(Employee):
    def __init__(self, tools):
        print("Constructor of MlEngineer ran")
        self.tools = tools

    def displayMlEngineerData(self):
        print(self.tools)


# You can make an inherited class from a class and then another inherited class from the inherited class
