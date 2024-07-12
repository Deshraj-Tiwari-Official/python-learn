class Grandfather:
    def __init__(self, GrandpaName, GrandpaAge):
        self.GrandpaName = GrandpaName
        self.GrandpaAge = GrandpaAge


class Father(Grandfather):
    def __init__(self, FatherName, FatherAge, GrandpaName1, GrandpaAge1):
        self.FatherName = FatherName
        self.FatherAge = FatherAge
        self.GrandpaName1 = GrandpaName1
        self.GrandpaAge1 = GrandpaAge1
        super().__init__(GrandpaName1, GrandpaAge1)


class Child(Father):
    def __init__(self, ChildName, ChildAge, FatherName1, FatherAge1, GrandpaName2, GrandpaAge2):
        self.ChildName = ChildName
        self.ChildAge = ChildAge
        self.FatherAge1 = FatherAge1
        self.FatherName1 = FatherName1
        self.GrandpaName2 = GrandpaName2
        self.GrandpaAge2 = GrandpaAge2
        super().__init__(FatherName1, FatherAge1, GrandpaName2, GrandpaAge2)


deshraj = Child("Deshraj", 15, "Sunil", 45, "Ramashankar", 85)
print(deshraj.GrandpaName)


"""
    Basically, what super is doing is that it is calling the constructor of the parent class with the arguments passed in it. Those arguments are the attributes required by the parent class.
"""