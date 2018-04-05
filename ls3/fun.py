def my_func(x, y, my_string='Python'):

    '''
    THIS ID DOC
    '''

    print('My first {} function!'.format(my_string))
    return x +y

print(my_func('Hello', 'Kostya'))




def func(*args):
    #a = args[0]
    #b = args[1]
    #...
    return args

print(func(1,2,4, 'Python'))


l = [1,2,4,5,6,6,7,8]

def even(num):
    return num % 2 == 0

evens = filter(even, l)
print(list(evens))


