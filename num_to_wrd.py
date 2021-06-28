num=eval(input('enter number from 1 to 5: '))

num_dic={1:"one",2:"tow",3:"three",4:"four",5:"five"}
num_list=[1,2,3,4,5]
if num in num_list:
    print(f'ayyeh {num_dic.get(num)}')
else:
    print("lla")
