import codecs
with codecs.open('file_3.txt', 'r', 'utf-8') as my_f:
    salary = []
    poor = []
    my_list = my_f.read().splitlines()
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        salary.append(i[1])
print(f'Оклад меньше: {poor}')
print(f'Средний доход: {int(sum(map(int, salary)) / len(salary))}')
