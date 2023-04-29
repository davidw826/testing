names = ["John","Mike","Sarah","Joe"]
ages = [37,54,37,15]

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print(name,age)