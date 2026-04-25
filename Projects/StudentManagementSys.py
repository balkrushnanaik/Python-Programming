# ── Parent class ──────────────────────────────────
class Person:
    def __init__(self, name, age):
        self.name = name        # public
        self.age  = age

    def __str__(self):
        return f"{self.name} (age {self.age})"


# ── Child class 1 ─────────────────────────────────
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)          # reuse Person's __init__
        self.student_id = student_id
        self.grades = []                     # own attribute

    def add_grade(self, subject, marks):
        self.grades.append({"subject": subject, "marks": marks})
        print(f"  Grade added: {subject} → {marks}")

    def average(self):
        if not self.grades:
            return 0
        return sum(g["marks"] for g in self.grades) / len(self.grades)

    def report(self):
        print(f"\n  Student : {self}")        # calls __str__ from Person
        print(f"  ID      : {self.student_id}")
        for g in self.grades:
            print(f"    {g['subject']:<15} {g['marks']}")
        print(f"  Average : {self.average():.1f}")


# ──