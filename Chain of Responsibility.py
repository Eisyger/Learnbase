from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    def __init__(self, next_handler=None):
        self.next = next_handler

    @abstractmethod
    def handle(self, screen: list):
        pass


class Background(Handler):
    def handle(self, screen):
        drawing = "Draw background."
        screen.append(drawing)
        if self.next:
            self.next.handle(screen)


class Lines(Handler):
    def handle(self, screen):
        drawing = "Draw lines and shapes."
        screen.append(drawing)
        if self.next:
            self.next.handle(screen)


class Font(Handler):
    def handle(self, screen):
        drawing = "Draw text."
        screen.append(drawing)
        if self.next:
            self.next.handle(screen)


class AfterEffects(Handler):
    def handle(self, screen):
        drawing = "Apply After Effects and show the result on screen."
        screen.append(drawing)


class Draw(Handler):
    def handle(self, screen):
        drawing = "Start drawing."
        screen.append(drawing)
        if self.next:
            self.next.handle(screen)


class Client:
    @staticmethod
    def update():
        # Initi the chain
        after_effects = AfterEffects()
        font = Font(after_effects)
        lines = Lines(font)
        background = Background(lines)
        draw = Draw(background)

        # Start the chain
        screen = []
        draw.handle(screen)
        return screen


if __name__ == "__main__":
    result = Client.update()
    print("Draw Log: ", result)
