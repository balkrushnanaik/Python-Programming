# try:
#     f = open("sample.txt","r")
#
#     content = f.read()
#     print(content)
#     f.close()
# except FileNotFoundError:
#     print("File Not Found")

# file = open('sample.txt','w')
# file.write('I have stopped to watch cwh solution videos')
# file.close()
#
# file1 = open('sample.txt','r')
# content = file1.read()
# print(content)
# file1.close()

with open('sample.txt','w') as file:
    file.write('I have learned this new syntax')
    file.close()
with open('sample.txt','r') as file1:
    content = file1.read()
    print(content)
    file.close()