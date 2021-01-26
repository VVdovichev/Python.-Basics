class ComplexNumber(Exception):
    def __init__(self, arg):
        self.arg = arg
        if not int(arg):
            raise TypeError

    def __add__(self, other):
        return f'Сумма: {self.arg + other.arg}'

    def __mul__(self, other):
        return f'Произведение: {self.arg * other.arg}'


num1 = ComplexNumber('a')
num2 = ComplexNumber(5)
print(num1 + num2)
print(num1 * num2)
