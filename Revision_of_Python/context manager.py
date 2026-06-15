with open("sample.txt", "w") as file:
    file.write("Hello World")
file.close()

with open("sample.txt", "r") as file:
    print(file.read())
file.close()