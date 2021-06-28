import os
import shutil
#print(os.sep)

path="C:\\D\\cmder"
path2="C:\D\cmder"

#print(path,path2)
#print(os.getcwd())

new_dir=os.chdir("c:\D")
#print(os.getcwd())

bin_path="C:\\D\\cmder\\bin"
#print(os.listdir(bin_path))

os.chdir(bin_path)
print(os.getcwd())
fol_name=input("enter foler name: ")
if fol_name not in os.listdir(bin_path):
    os.mkdir(fol_name)
else:
    print("already exist")
conf_usr=input(' are u sure {fol_name} wil be deleted yes or no: ')
if conf_usr=='yes':
    #shutil.copytree(fol_name, 'foo', dirs_exist_ok=True)
    os.rmdir(fol_name)
elif conf_usr=='no':
    print(os.listdir(bin_path))
else:
    print("what are you typing??")
