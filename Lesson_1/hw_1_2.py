x = int(input('Введите время в секундах: '))
hours = x // 3600
minutes = (x // 60) % 60
seconds = x % 60
print(f'Время {hours:02d}:{minutes}:{seconds}')