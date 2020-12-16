x = int(input('Введите число от 0 до 9 включительно: '))
if x >= 0 and x < 10:
    summa = x + (x * 11) + (x * 111)
    print(summa)
else:
    print('Укажите другое число')
