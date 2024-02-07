from abc import ABCMeta, abstractmethod


class ICommand:
    @abstractmethod
    def exec(self):
        pass


class ManagerOne(ICommand):
    def exec(self):
        print("Die Managerklasse ManagerOne wurde aufgerufen.")


class ManagerTwo(ICommand):
    def exec(self):
        print("Die Managerklasse ManagerTwo wurde aufgerufen.")


class Invoker:
    @staticmethod
    def run(command: ICommand):
        command.exec()


if __name__ == '__main__':
    m1 = ManagerOne()
    m2 = ManagerTwo()
    Invoker.run(m1)
    Invoker.run(m2)
