x={'fruit':'aple','color':'red',1:'one','tow':2}

print(x)
print(x[1])
print(x['color'])
print(x.get('color'))
print(x.get('walou'))
print(x)

x['walou']=0
print(x)

'''
print(x.keys())
print(x.values())
print(x.items())
y=x.copy()
print(id(x),id(y))
print(y)
'''
'''
y={'four':4,'five':5}
x.update(y)
print(x)
x.pop('four')
print(x)
removed_item=x.popitem() #remove ramdom item
print(x)
print(removed_item)
'''

keys=['name','address','something',] #age hided

h=dict.fromkeys(keys)
h.setdefault('age','15')
print(h)
h['name']='red'
#h['age']='39'
h['address']='temmakinate'

print(h)
h.clear()
h.setdefault('key','value')

print(h)








'''
x.clear()
print(x)
'''
