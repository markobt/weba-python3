# if <условие 1>:
#     <блок 1>
# elif <условие 2>:
#     <блок 2>
#     ...
# else:
#     <блок else>

#number = int(input('Enter a number'))

#if number > 5:
#    print('Block IF')
#elif 10 == 10:
#    print('Hello')
#    print('Block ELIF')
#else:
#    print('Block ELSE')

#print(number)

l = []
i = 2
while i <= 1024:
    l = l + [i]
    i = i * 2
print(l)

seq = [1,2,3,4,5,6]
for l in seq:
    print(l)

mydict = {"Kostya": 1, "Anna": 2, "Alex": 3}
for key in mydict:
    print(key)
    print(mydict[key])

pairs = [(1,2),(3,4),(5,6)]
for item in pairs:
    print(item)

for (t1, t2) in pairs:
    print('T1: ',t1)
    print(t2)

x = [1,2,3,4]
out = [(num ** 2 for num in x)]
print(out)

for i in 'Hello world!':
    if i == 'o':
        continue
    print(i * 2, end='')
print(i)

for i in 'Hello world!':
    if i == 'o':
        break
    print(i * 2, end='')
print(i)

