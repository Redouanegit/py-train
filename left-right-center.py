
import os

give=input("give something: ")
TER_SIZE=os.get_terminal_size().columns
print(give)


if False: # can be True
    print(give.center(TER_SIZE).title())
    print(give.ljust(TER_SIZE).title())
    print(give.rjust(TER_SIZE).title())

usr_cnf=input(" ok ? : ")
if usr_cnf=="yes":
    print(give.center(TER_SIZE).title())
    print(give.ljust(TER_SIZE).title())
    print(give.rjust(TER_SIZE).title())
