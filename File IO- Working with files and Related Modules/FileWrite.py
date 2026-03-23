
try:
    file = open("file.txt", "w") # By default python assume you are writing text
    file.write("Hello Everyone, Today I am writing this file using python file writing method \n")
    file.write("Thank you Python for giving these features \n")
    file.close()
except FileExistsError:
    print("File Already Exists")

finally:
    file = open("file.txt", "r")
    print(file.read())
    file.close()

