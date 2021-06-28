'''
import module,sys,os #not good practice
#import math
#from math import *
from math import pi,pow
import platform as pt
print(pt.system())
print(module.x)
print(pi)
print(pow(3,2))
'''
import platform as pt
print(f"This is {pt.system()} os")
print(f"Python version is {pt.python_version()} ")
print(pt.python_version_tuple())
print(pt.machine())
print(pt.platform())
print(pt.release())
print(pt.architecture())
print(pt.processor())
print(pt.node())
print(pt.uname())
