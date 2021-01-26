class Warehouse:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {'Модель': name, 'Цена': price, 'Количество': quantity}


class Technic(Warehouse):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)


class Printer(Technic):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        pass


class Scanner(Technic):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        pass


class Xerox(Technic):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        pass


