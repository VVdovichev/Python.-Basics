"""import argparse
parser = argparse.ArgumentParser(description='Расчёт заработной платы сотрудника')
parser.add_argument('working_out_in_hours', type=int, help='Выроботка в часах')
parser.add_argument('rate_per_hour', type=int, help='Ставка в час')
parser.add_argument('bonus', type=int, help='Премия')
args = # не понимаю, что делать дальше
"""

from sys import argv
name, working_out_in_hours, rate_per_hour, bonus = argv
working_out_in_hours = int(working_out_in_hours)
rate_per_hour = int(rate_per_hour)
bonus = int(bonus)


def my_calc():
    return working_out_in_hours * rate_per_hour + bonus


print('Имя скрипта: ', name)
print('Выплата в часах: ', working_out_in_hours)
print('Ставка в час: ', rate_per_hour)
print('Премия: ', bonus)
print('Заработная плата: ', my_calc())
