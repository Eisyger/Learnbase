class Moveable:
    def __init__(self):
        self.speed = "langsam"
        self.implemetor_speed = Fast()

    def update_speed(self):
        self.speed = self.implemetor_speed.speed()

class Player(Moveable):
    def get_speed(self):
        self.update_speed()
        return f"Du läufst {self.speed}"

class ImplementorSpeed:
    def speed(self):
        pass

class Fast(ImplementorSpeed):
    def speed(self):
        return "schnell"

class Sprint(ImplementorSpeed):
    def speed(self):
        return "im sprint"


if __name__ == "__main__":
    player = Player()
    print(player.get_speed())