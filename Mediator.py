from abc import ABCMeta, abstractmethod


class IMediator(metaclass=ABCMeta):
    @abstractmethod
    def mediate(self, sender, msg):
        pass


class User:
    def __init__(self, mediator: IMediator, name: str):
        self.mediator = mediator
        self.name = name

    def get_state(self, sender, msg):
        pass

    def send_message(self, msg):
        self.mediator.mediate(sender=self, msg=msg)


class Stefan(User):
    def get_state(self, sender, msg):
        print(f"{sender}: {msg}")


class Susi(User):
    def get_state(self, sender, msg):
        print(f"{sender}: {msg}")


class Chatroom(IMediator):
    def __init__(self):
        self.clients = list()

    def attach(self, user: User):
        self.clients.append(user)

    def detach(self, user: User):
        self.clients.remove(user)

    def mediate(self, sender, msg):
        for client in self.clients:
            if client != sender:
                client.get_state(sender.name, msg)

    def run(self):
        for client in self.clients:
            client.get_state()


if __name__ == "__main__":
    chatroom = Chatroom()
    stefan = Stefan(chatroom, "Stefan")
    susi = Susi(chatroom, "Susi")
    chatroom.attach(stefan)
    chatroom.attach(susi)
    stefan.send_message("Hello Susi!")
