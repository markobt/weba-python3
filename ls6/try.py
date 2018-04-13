f = open('1.txt', 'r')
ints = []
try:
    for line in f:
        ints.append(int(line))
except ValueError:
    print('Это не число, выходим.')
except Exception:
    print('Это что еще такое?')
else:
    print('Все хорошо!')

finally:
    f.close()
    print('Я закрыл файл')
