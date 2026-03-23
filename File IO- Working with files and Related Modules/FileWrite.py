file = open("file.txt","w")
file.write("Hello Everyone, Today I am writing this file using python file writing method \n")
file.write("Thank you Python for giving these features \n")
file.close()

file = open("file.txt","r")
print(file.read())
file.close()
