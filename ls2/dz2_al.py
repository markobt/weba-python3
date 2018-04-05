list_1 = [1, 5, 8, 13, 13, 2, 9]
max = 1
min = 0

result = 0
# Найдите сумму четных чисел массива. (for, in, %)
print("Найдите сумму четных чисел массива. (for, in, %)")
for i in list_1:
    if i % 2 == 0:
        result += i

print(list_1)
print(result)

# Найдите сумму наибольшего и наименьшего элементов массива. (min,max, sum, sort)
print("Найдите сумму наибольшего и наименьшего элементов массива. (min,max, sum, sort)")
for i in list_1:
    if i > max:
        max = i
    if i < min:
        min = i
print("min")
print(min)
print("max")
print(max)
print("sum")
print(max + min)
print("sort")
list_1.sort()
print(list_1)

# Проверьте, является ли данный массив возрастающим или убывающим. (if-else)
print("Проверьте, является ли данный массив возрастающим или убывающим. (if-else)")
for i in range(20):
    if i < i+1:
        continue
    else:
        print('The array is decreasing')
        break
print ('The array is increasing')

# Найдите количество различных элементов данного массива. (in)
print("Найдите количество различных элементов данного массива. (in)")
for i in range(len(list_1)):
    if not list_1[i] in list_1[0:i]:
        result += 1
print(result)


# Определите, есть ли в массиве повторяющиеся элементы. (in)
print("Определите, есть ли в массиве повторяющиеся элементы. (in)")
for i in set(list_1):
    if list_1.count(i) > 1:
        print(i)

# Удалить в массиве первый и последний элементы.
print('Удалить в массиве первый и последний элементы.')
list_1.pop(0)
list_1.pop(len(list_1)-1)
for i in list_1:
    print(i)
# Переставить элементы массива в обратном порядке. (reverse)

print("Переставить элементы массива в обратном порядке. (reverse)")

print(list_1)
list_1.reverse()
print(list_1)

#Дано 2 строки. Вернуть результат их конкатенации за исключением первой буквы первого слова.
s1 = "Python"
s2 = "Django"

print(s1[1:])
print(s2[1:])
print(s1[1:] + s2[1:])
