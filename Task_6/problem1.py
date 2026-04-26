

class DOG:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        print(f"Woof! My name is {self.name}")

myDog = DOG("Max","Husky")
myDog.bark()