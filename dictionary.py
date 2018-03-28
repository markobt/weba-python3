
#mydict = {}

mydict = {'key1': 'value1', 'key2': 'value2'}
print(mydict['key1'])

mydict['key2'] = 123
mydict['key3'] = 'value3'
print(mydict)

d2 = {'key1': 123, 'key2': 'value4', 'key3': {'key123': [1,2,'Findme']}}
d2['key3']['key123'][2]
print(d2['key3']['key123'][2].upper())


