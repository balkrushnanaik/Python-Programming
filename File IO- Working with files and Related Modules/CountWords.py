file = open("student.txt", "r")

data = file.read()

words = data.split()

print("Total Words:", len(words))

file.close()