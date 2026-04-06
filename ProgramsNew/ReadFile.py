# Read content from file

file = open("sample.txt", "r")

data = file.read()

print("File Content:")
print(data)

file.close()