revenue = int(input('Введите значение выручки: '))
cost: int = int(input('Введите значение издержек: '))
profit = revenue - cost
if revenue > cost:
    print('Фирма приносит прибыль')
    profitability = (profit / revenue) * 100
    print('Рентабельность в %: ', int(profitability))
    people = int(input('Введите численность сотрудников фирмы: '))
    people_profit = profit / people
    print('Прибыль в расчёте на сотрудника: ', int(people_profit))
else:
    print('Фирма несёт убыток')
