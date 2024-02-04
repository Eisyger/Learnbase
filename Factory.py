import abc

class Creator:
    @abc.abstractmethod
    def factory_method(self):
        pass

class Produkt:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def dump(self):
        return f"Name: {self.name}, Preis: {self.price}"

class Poster(Produkt):
    def __init__(self, name, price):
        super().__init__(name, price)

class TShirt(Produkt):
    def __init__(self, name, price):
        super().__init__(name, price)

class PosterCreator(Creator):
    def __init__(self, name, price):
        self.product = Poster(name, price)
    def factory_method(self):
       return self.product

class TShirtCreator(Creator):
    def __init__(self, name, price):
        self.product = TShirt(name, price)
    def factory_method(self):
       return self.product


if __name__ == "__main__":
    ware = [PosterCreator("Migos", 99).factory_method(),
            TShirtCreator("AC/DC", 39).factory_method()]

    print([w.dump() for w in ware])