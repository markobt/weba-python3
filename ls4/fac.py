import sys


def counter():
    num = 4
    def incrementer():
        nonlocal num
        num += 1
        return num
    return incrementer

c = counter()

print(c)
c()
c()

