
#mydict = {}

mydict = {'key1': 'value1', 'key2': 'value2'}
print(mydict['key1'])

mydict['key2'] = 123
mydict['key3'] = 'value3'
print(mydict)

d2 = {'key1': 123, 'key2': 'value4', 'key3': {'key123': [1,2,'Findme']}}
d2['key3']['key123'][2]
print(d2['key3']['key123'][2].upper())


#>>> rec[‘name’] # ‘Name’ – это вложенный словарь
#{‘last’: ‘Smith’, ‘first’: ‘Bob’}
#>>> rec[‘name’][‘last’] # Обращение к элементу вложенного словаря
#‘Smith’
#>>> rec[‘job’] # ‘Job’ – это вложенный список
#[‘dev’, ‘mgr’]
#>>> rec[‘job’][-1] # Обращение к элементу вложенного списка
#‘mgr’
#>>> rec[‘job’].append(‘janitor’) # Расширение списка должностей Боба (Bob)
#>>> rec
#{‘age’: 40.5, ‘job’: [‘dev’, ‘mgr’, ‘janitor’], ‘name’: {‘last’: ‘Smith’,
#‘first’: ‘Bob’}}
