# Закрепим пройденный материал по типам данных,
# которые мы рассмотрели ранее домашним заданием!

############
# Задача 1
############

# У нас есть строка
s = 'python'

# Используя доступ по индексу необходимо вывести:
# 'p'
print(s[0])
# 'o'
print(s[4])
# 'pyth'
print(s[0:4])
# 'yth'
print(s[1:4])
# 'on'
print(s[-2:])
print(s[4:])
# 'nohtyp'
print(s[::-1])
# 'pto'
print(s[::2])
############
# Задача 2
############

# Есть две переменные:
age = 10
name = 'Lisa'

# Необходимо вывести следующий текст, используя форматирование строки:
# 'Hello my cat's name is Lisa and she is 10 years old'

print("Hello my cat's name is {a} and she is {b} years old".format(a = "Lisa", b = 10))

############
# Задача 3
############

# Имеется вложенный список:
l = [21, 2, [3,12,True], [10, 13, 'Hello', False]]

# Надо заменить 'Hello' на 'Goodbye'

l[3][2] = 'Goodbye'

print(l)

############
# Задача 4
############

# Есть три словаря и надо получить значение 'hello' в каждом
d1 = {'key': 'hello'}
print(d1['key'])

d2 = {'k1': {'k2': 'hello'}}
print(d2['k1']['k2'])


d3 = {'k1': [{'nest_key': ['deep', ['hello']]}]}
print(d3['k1'][0]['nest_key'][1][0])


############
# Задача 5
############

# Используйте множество, чтобы найти уникальные значения из списка:
mylist = [1,1,1,1,1,1,2,2,2,2,3,3,3,3]

print(set(mylist))