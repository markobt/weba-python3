True
False
1
0

#операторы сравнения
#Больше чем
2 > 3 - False

#Мень чем
2 < 3 - True

#больше чем или равно
2 >= 2 - True

#меньше чем или равно
1 <= 4 - True

#Равно

2 ==2 - True
2 == '2' - False
'hi' == 'bye' - False

#не равно
2 != 2 - False
1 != '1' - True


# x  in list
2 in [2,3,4] - True
1 in [2,3,4] - False

# x not in list

2 not in [2,3,4] - False
1 not in [2,3,4] - True

#and
(1>2) and (2<3) - False

# or - логический оператор или
(1>2) and (2<3) - True


# not - логический оператор not
not 2>=1 - False

#множество

x = set ()
x.add(1)
x.add(2)
x.add(4)
x.add(3.14)

print(x)


words = ['hello', 'Kostya', 'hello', 'Anna']

set(words)
print(set(words))