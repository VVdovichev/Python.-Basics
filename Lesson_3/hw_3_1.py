def div(*args):
    try:
        arg1 = float(input('Введите делимое: '))
        arg2 = float(input('Введите делитель: '))
        res = arg1 / arg2
    except ZeroDivisionError:
        return 'Деление на "0" не возможно!'
    return res


print(f'Результат: {div()}')
