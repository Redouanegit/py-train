
import os

give=input("give something: ")
TER_SIZE=os.get_terminal_size().columns
print(give.upper())


if False: # can be True
    print(give.center(TER_SIZE).title())
    print(give.ljust(TER_SIZE).upper())
    print(give.rjust(TER_SIZE).title())

usr_cnf=input(" ok ?! type yes or no : ")
if usr_cnf=="yes":
    print(give.center(TER_SIZE).title())
    print(give.ljust(TER_SIZE).upper())
    print(give.rjust(TER_SIZE).title())

### list conditions

my_list=[1,7,89,0,54,6,3]

usr_num=eval(input(" type your number :"))

if usr_num in my_list:
    print(f" you number is {usr_num}")
else:
    print("lla")
