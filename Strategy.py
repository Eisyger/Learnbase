from abc import ABCMeta, abstractmethod


class ISortStrategy(metaclass=ABCMeta):
    @abstractmethod
    def algorhyme(self, sort_data):
        pass


class QuickSort(ISortStrategy):
    def algorhyme(self, sort_data):
        return "Hier könnt ein Quick-Sort Algorhytmus laufen"


class BubbleSort(ISortStrategy):
    def algorhyme(self, sort_data):
        return "Hier könnt ein Bubble-Sort Algorhytmus laufen"


class Client:
    @staticmethod
    def sort(sort_data, sort_strategy="quick"):
        if sort_strategy == "quick":
            quick = QuickSort()
            return quick.algorhyme(sort_data)
        elif sort_strategy == "bubble":
            bubble = BubbleSort()
            return bubble.algorhyme(sort_data)
        else:
            return "sort_strategy nicht vorhanden, versuche es mit 'quick' oder 'bubble'."


if __name__ == "__main__":
    client = Client()
    data = ["Iam the data"]
    sorted_data = client.sort(data, "bubble")
    print(sorted_data)
