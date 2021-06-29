#lists are mutable
'''
x=[1,2,3,'pyhton',4,5]
y=[]

print(bool(x))
print(bool(y))

print(x,'\t',type(x))
print(x[3][1])
print(x[-3])
print(x[:])
print(x[2:])
print(x[2:4])

x[0]=56
print(x)
'''
'''
x=[1,2,3,4,3,78,4,3,908,21,3]
print(x.index(3,5))
print(x.count(3))
#x.clear()
#print(x)
y=x
z=x.copy()

print(id(x),id(y))
print(id(z))
'''

x=[6,45,9,1,76,34]
print(x[3])
#bool(x)
#dir(x)
'''
x.append(32)
print(x)
x.insert(3,24673)
print(x)
y=[99,88]
x.append(y)
print(x)
x.extend(y)
print(x)
x.remove([99,88])
print(x)
x.pop(3)
print(x)
x.pop()  #by default it removes the last value
print(x)
print(x.pop())
print(x)
'''
print(x)
x.reverse()
print(x)
x.sort()
print(x)
x.reverse()
print(x)
x.sort(reverse=True)
print(x)
