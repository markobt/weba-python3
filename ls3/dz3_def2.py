print("Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000, и возвращающую True, если оно простое, и False - иначе. ")

def is_prime(x):
    f=True
    for i in range(2,int(x**0.5)):
        if x % i == 0:
            f=False
    return(f)


if __name__ == "__main__":
    print(is_prime(1))
    print(is_prime(5))
    print(is_prime(9))
    print(is_prime(998))
    print(is_prime(8))


prime_n = []
for i in range(1, 1000):
    if is_prime(i) == True:
        prime_n.append(i)
    else:
        continue
print("Простые числа с 0 до 1000")
print(prime_n)

#a=int(input('Введите для проверки число: '))
#print(is_prime(a))