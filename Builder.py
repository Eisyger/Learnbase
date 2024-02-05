from abc import ABC, abstractmethod


class AutoBuilder(ABC):
    @abstractmethod
    def build_reifen(self):
        pass

    @abstractmethod
    def build_lenkrad(self):
        pass

    @abstractmethod
    def build_windschutzscheibe(self):
        pass

    def get_result(self):
        reifen = self.build_reifen()
        lenkrad = self.build_lenkrad()
        scheibe = self.build_windschutzscheibe()

        return Auto(reifen, lenkrad, scheibe)


class Client(AutoBuilder):
    def build_reifen(self):
        return Reifen("Michelin")

    def build_lenkrad(self):
        return Lenkrad("Sport")

    def build_windschutzscheibe(self):
        return Scheibe("Windbreaker")

    def run(self):
        auto = self.get_result()
        print(auto.dump())


class Auto:
    def __init__(self, reifen, lenkrad, scheibe):
        self.reifen = reifen
        self.lenkrad = lenkrad
        self.scheibe = scheibe

    def dump(self):
        return (f"Reifen-Typ: {self.reifen.type}, "
                f"Lenkrad-Typ: {self.lenkrad.type}, "
                f"Windschutzscheiben-Typ: {self.scheibe.type}")


class Reifen:
    def __init__(self, type: str):
        self.type = type


class Lenkrad:
    def __init__(self, type: str):
        self.type = type


class Scheibe:
    def __init__(self, type: str):
        self.type = type


if __name__ == "__main__":
    client = Client()
    client.run()
