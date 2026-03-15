class Animal:

    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} sounds good ")

class Dog(Animal):
    def speak(self):
        # super().sound()
        print(f"{self.name} speaks woof! ")
class Cat(Animal):
    def speak(self):
        super().sound()
        print(f"{self.name} speaks Meww ")

# a1 = Animal("Dog")
# a1.sound()

d1 = Dog("Dog")
d1.speak()

c1 = Cat("Cat")
c1.speak()


