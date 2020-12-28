from itertools import count, cycle
for el in count(3):
    if el == 10:
        break
    else:
        print(el)

print()

x = 0
for el2 in cycle('ABC'):
    if x == 10:
        break
    else:
        print(el2)
    x += 1
