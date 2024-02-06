from abc import ABCMeta, abstractmethod


class IUpdate(metaclass=ABCMeta):
    @abstractmethod
    def update(self, game_score: tuple):
        pass


class FootballMatch:
    def __init__(self):
        self.observers = list()

    def attach(self, observer: IUpdate):
        self.observers.append(observer)

    def detach(self, observer: IUpdate):
        self.observers.remove(observer)

    def notify(self, game_score: tuple):
        for observer in self.observers:
            observer.update(game_score)


class LiveTicker(IUpdate):
    def update(self, game_score):
        team_left, team_right, score = game_score
        print(f"Es steht {score} im Spiel {team_left} gegen {team_right}.")


class FootballFan(IUpdate):
    def update(self, game_score: tuple):
        print("Tooooor!")


if __name__ == "__main__":
    match = FootballMatch()
    ticker = LiveTicker()
    fan = FootballFan()

    match.attach(ticker)
    match.attach(fan)

    match.notify(("Frankreich", "Deutschland", "0:1"))
    match.notify(("Frankreich", "Deutschland", "1:1"))
    match.notify(("Frankreich", "Deutschland", "1:2"))

    match.detach(ticker)

    match.notify(("Frankreich", "Deutschland", "1:3"))

    match.detach(fan)
