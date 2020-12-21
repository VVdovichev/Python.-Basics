my_str = input("введите строку ")
my_list = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_list = my_str.split()
    if len(str(my_list)) <= 10:
        print(f" {num} {my_list[el]}")
        num += 1
    else:
        print(f" {num} {my_list[el] [0:10]}")
        num += 1
