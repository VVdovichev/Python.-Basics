l = float(input('Введите расстояние первого дня: '))
l_max = float(input('Введите максимальное расстояние: '))
counter = 0
while l <= l_max:
    l *= 1.1
    counter += 1
print(f'Номер дня, на который общий результат спортсмена составит {l_max} км: ', counter)
