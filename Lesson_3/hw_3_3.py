def my_func(arg1=int(input('Введите 1е число: ')), arg2=int(input('Введите 2е число: ')),
            arg3=int(input('Введите 3е число: '))):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg2 < arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3


print(my_func())
