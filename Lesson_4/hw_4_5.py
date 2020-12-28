from functools import reduce


def my_func(arg1, arg2):
    return arg1 * arg2


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f'Список: {my_list}')
print(f'Результат: {reduce(my_func, my_list)}')
