import os
file=input("enter the file name: ")
path=os.walk("C:\\")
for r,d,f in path:
    for each in f:
        if each==file:
            print(os.path.join(r,each))
