revenue = int(input('Введите значение выручки: '))
cost: int =int(input('Введите значение издержек: '))
if revenue > cost:
    print('Фирма приносит прибыль')
    profit = revenue - cost
    profitability = (profit / revenue) * 100
    print('Рентабельность в %: ', int(profitability))
else:
    print('Фирма несёт убыток')
people = int(input('Введите численность сотрудников фирмы: '))
profit = revenue - cost
peopleprofit = profit / people
print('Прибыль в расчёте на сотрудника: ', int(peopleprofit))