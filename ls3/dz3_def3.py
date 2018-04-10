
#Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа,
#  третий - операция, которая должна быть произведена над ними.
#Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
#В остальных случаях вернуть строку "Неизвестная операция".

def arithmetic(a, b, c):
    if c == "+":
        #print(a + b)
        return a + b

    elif c == "-":
        #print(a - b)
        return a - b

    elif c == "*":
        #print(a * b)
        return a * b

    elif c == "/":
        #print(a / b)
        return a / b

    else:
        print("Неизвестная операция")


if __name__ == "__main__":
    print(arithmetic(1, 2, "+"))
    print(arithmetic(5, 7, "-"))
    print(arithmetic(9, 3, "*"))
    print(arithmetic(5, 1, "/"))
    print(arithmetic(4, 6, "test"))
