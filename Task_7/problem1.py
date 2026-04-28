

class Animal: 
    def speak(self):
        print("Nothing")

class Dog(Animal):
    def speak(self):
        print("Woof!")

a = Animal()
b = Dog()
a.speak()
b.speak()