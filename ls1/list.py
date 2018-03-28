
mylist1 = [1,2,3,4,5] # списки
mylist2 = []
mylist3 = ['z']

l3 = ['test', 324, True, [1,2,3]]

print(l3)
print(list('Lists'))
print(len(l3))  # функция len


print(l3[1])

l4 = ['a', 'b', 'c', 'd', 'i']

print(l4[:3])

#замена элемента

l4[0] = 'New Item'

print(l4)

# добавлеяем элемент в конец списка

l4.append(['x', 'y', 'z']) #вложенный список
print(l4)

l5 = ['x', 'y', 'z']
l4.extend(l5)
print(l4)

#l5.pop(0)
l5.reverse()
print(l5)

l6 = [10,1,5,11]
l6.sort()
print(l6)


l7 = [1,2,['x', 'y', 'z']]
print(l7[2][1])

matrix = [[1,2,3], [4,5,6], [7,8,9]]
# 123
# 456
# 789
second_col = [row[1] for row in matrix] #генератор списка
print(second_col)
