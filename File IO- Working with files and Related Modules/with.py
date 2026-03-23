with open("sample.txt", "r") as file: # Context Manager
   for line in file:
       print(line)
       # No need to f.close() because file is already closed by default when using with syntax