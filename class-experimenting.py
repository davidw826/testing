names = ["John","Mike","Sarah","Joe"]
ages = [37,54,37,15]

class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return self.name+' '+str(self.age)
        
    def __eq__(self,other):
        return (self.age==other.age)
    
    def __hash__(self):
        return hash((self.age))
    
    def birthday(self):
        self.age += 1

people = set()

for i in range(4):
    people.add(Person(names[i],ages[i]))

for person in people:
    print(person)