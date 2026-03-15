class Labour:
    lastname = "Anisha"   # class attribute

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):
        print(f"The name of Labour is : {self.name}, age is: {self.age}, and the gender is : {self.gender}")


l1 = Labour("Monisha", 22, "Female")

print(l1.name)        # instance attribute
print(Labour.lastname) # class attribute
print(dir(l1))        # shows all attributes and methods
l1.print_info()