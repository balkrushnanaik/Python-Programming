student = {"name": "John", "age": 20, "grade": "A"}
print(student)

print(student.get("name"))

student["grade"] = "A+"
print(student)

student.update({"city":"Delhi"})
print(student)

print(student.keys())
print(student.values())
print(student.items())