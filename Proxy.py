class Add:
    def add(self, a, *b):
        pass


class Calculator(Add):
    def add(self, a, *b):
        return a + sum(b)


class Proxy(Add):
    def add(self, a, *b):
        c = Calculator()
        result = c.add(a, *b)
        return "Die Summe der Eingaben ist: " + str(result)


if __name__ == "__main__":
    calc = Calculator()
    print(calc.add(1, 5, 6, 7))
    prx = Proxy()
    print(prx.add(1, 5, 6, 7))
