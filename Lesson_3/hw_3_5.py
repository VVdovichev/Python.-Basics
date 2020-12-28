def sum_values():
    summa = 0
    while True:
        number = input('Начать ввод чисел (да/нет)?')
        if number.lower() == 'нет':
            return summa
        else:
            for i in input('Введите строку чисел через пробелы: ').split():
                try:
                    summa += float(i)
                except ValueError:
                    return summa


print(f'Сумма: {sum_values()}')




