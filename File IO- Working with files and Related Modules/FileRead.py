try:
    f = open("sample.txt","r")

    content = f.read()
    print(content)
    f.close()
except FileNotFoundError:
    print("File Not Found")