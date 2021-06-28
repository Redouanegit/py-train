#usr_str=input("enter:")
#usr_action=input("enter your action on your string, 'l' for lower, 'u' for upper, 't' for title:  ")

import sys

if len(sys.argv)!=3:
    print("usage: ")
    print(f'{sys.argv[0]} <your_req_string> <l|u|t>' )
    sys.exit()

usr_str=sys.argv[1]
usr_action=sys.argv[2]
if usr_action=="l":
    print(usr_str.lower())
elif usr_action=="u":
    print(usr_str.upper())
elif usr_action=="t":
    print(usr_str.title())
else:
    print("lla")
