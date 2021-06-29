import os

path="C:\\D\\pythonscripts"

path_list=os.walk(path,topdown=False) #topdown to reverse the result

#print(os.system(f'tree {path}'))
#print(path_list)
#print(path_list[1])

for r,d,f in path_list:
    if len(f) != 0:
        print(r)
        for each in f:
            print(os.path.join(r,each))
        print("----------")
