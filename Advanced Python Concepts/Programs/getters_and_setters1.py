class Student:
    def __init__(self, name, marks):
        self._name = name      # protected variable
        self._marks = marks

    # Getter for marks
    def get_marks(self):
        return self._marks

    # Setter for marks
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
        else:
            print("Invalid marks! Must be between 0 and 100.")

# Create object
s1 = Student("Rahul", 85)

# Access using getter
print("Marks:", s1.get_marks())

# Modify using setter
s1.set_marks(92)
print("Updated Marks:", s1.get_marks())

# Try invalid value
s1.set_marks(150)