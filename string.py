python = 'Python \'3.6.1\'' # не допускается ''
django = "Django \"1.11\"" # не допускает символ  с ""


print(python)

print("Hello\nDjango")

"""
test test for comment 

"""

print("Python" ' 3.6.1')

#Наконец, будучи последовательностями,
#  строки поддерживают операцию конкатенации
# >>> S + ‘xyz’ # Конкатенация



s1 = "Python"
s2 = ' 3.6.1'

print(s1 + s2) #Конкатенация

print(s1 * 2)

print(s1[0])
print(s1[-2]) #отсчитует с конца
print(s1[1:4]) #изличения среза
print(s1[:3])
print(s1[2::2])

print(len(s1))
print(s1.upper())
print(s1.lower())
print(s1.capitalize())

s3 = "Hello Python"

print(s3.split())
print(s3.split('o'))

s4 = "Hello, {a} and {b}".format( a = "Vas", b = "Mar")
print(s4)