import copy
import abc

class Factory:
    def create_shoe(self):
        pass
    def create_merch(self):
        pass

class FactoryPremium(Factory):
    def create_shoe(self):
        return Sneaker("", -1, 0)
    def create_merch(self):
        return TShirt("", -1)

class FactoryNormal(Factory):
    def create_shoe(self):
        return Boots("", -1, 0)
    def create_merch(self):
        return Poster("", -1)


class Merch:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def dump(self):
        return f"Name: {self.name}, Preis: {self.price}"

class Poster(Merch):
    def __init__(self, name, price):
        super().__init__(name, price)

class TShirt(Merch):
    def __init__(self, name, price):
        super().__init__(name, price)


class Shoes:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def dump(self):
        return f"Name: {self.name}, Preis: {self.price}, Größe: {self.size}"

class Sneaker(Shoes):
    def __init__(self, name, price, size):
        super().__init__(name, price, size)

class Boots(Shoes):
    def __init__(self, name, price, size):
        super().__init__(name, price, size)

class Client:
    def __init__(self):
        self.factory_normal = FactoryNormal()
        self.factory_premium = FactoryPremium()

        self.normal_shoes = []
        self.premium_merch = []

    def run(self):
        self.normal_shoes.append(self.factory_normal.create_shoe())
        self.premium_merch.append((self.factory_premium.create_merch()))

        print([s.dump() for s in self.normal_shoes])
        print([m.dump() for m in self.premium_merch])


if __name__ == "__main__":
    client = Client()
    client.run()