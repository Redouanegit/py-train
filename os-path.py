import os
path="C:\\D\\cmder\\bin"
path2="C:\\D\\cmder\\bin\\Readme.md"
path3="C:\\red\\rod"
print(os.path.basename(path2))
print(os.path.dirname(path2))
print(os.path.join(path2,path3))
print(os.path.split(path2))
print(os.path.getsize(path2))
print(os.path.exists(path3))
print(os.path.exists(path2))
print(os.path.isfile(path2))
print(os.path.isdir(path))

print(os.path.getmtime(path))
print(os.path.getatime(path))
print(os.path.getctime(path))
