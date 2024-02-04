import copy
import abc

class Creator:
    @abc.abstractmethod
    def factory_method(self):
        pass

class Prototype:
    def clone(self):
        pass

class Produkt:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def dump(self):
        return f"Name: {self.name}, Preis: {self.price}"

class Poster(Produkt, Prototype):
    def __init__(self, name, price):
        super().__init__(name, price)
    def clone(self):
        return copy.deepcopy(self)

class PosterCreator(Creator):
    def __init__(self, name, price):
        self.product = Poster(name, price)
    def factory_method(self):
       return self.product


if __name__ == "__main__":
    merch = [PosterCreator("Shakira", 19).factory_method(),
             PosterCreator("ABBA", 12).factory_method()]

    merch.append(merch[0].clone())
    merch[0].name = "Rammstein"
    print([m.dump() for m in merch])
