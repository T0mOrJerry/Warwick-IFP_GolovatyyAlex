class Bakery:
    def __init__(self):
        self.baked_goods = []

    def add_good(self, good):
        self.baked_goods.append(good)

    def print_goods(self):
        return ' '.join(self.baked_goods)


class BakedGood:
    def __init__(self, nm, pc):
        self.name = nm
        self.price = pc

    def __str__(self):
        return f'This is {self.name} it costs £{self.price}'


class Cake(BakedGood):
    def __init__(self, nm, pc, lr):
        super().__init__(nm, pc)
        self.layers = lr

    def __str__(self):
        return f'This is {self.name} with {self.layers} layers it costs £{self.price}'


class Cookie(BakedGood):
    def __init__(self, nm, pc, cpp):
        super().__init__(nm, pc)
        self.cookies_per_pack = cpp

    def __str__(self):
        return f'This is {self.name} - {self.cookies_per_pack} cookies in pack it costs £{self.price}'


class ChocolateCake(Cake):
    def __init__(self, nm, pc, lr, ch):
        super().__init__(nm, pc, lr)
        self.chocolate_type = ch

    def __str__(self):
        return f'This is {self.name} with {self.layers} layers and {self.chocolate_type} chocolate, costs £{self.price}'
