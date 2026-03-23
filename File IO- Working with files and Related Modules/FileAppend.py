file = open("file.txt", "a")
file.write("Hello World")
file.close()

readFile = open("file.txt", "r")
print(readFile.read())

file.close()
