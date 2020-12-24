"""
def my_func(x=float(input('Введите действительное положительное число: ')),
            y=int(input('Введите целое отрицательное число: '))):
    if y < 0 < x:
        res = x ** y
        return res
    else:
        return 'Введите другие числа!'


print(f'Результат: {my_func()}')

"""


def my_func(x=float(input('Введите действительное положительное число: ')),
            y=int(input('Введите целое отрицательное число: '))):
    if y < 0 < x:
        exponent = 1
        for i in range(-y):
            exponent *= 1 / x
        x *= exponent
    else:
        return 'Введите другие числа!'
    return exponent


print(f'Результат: {my_func()}')
