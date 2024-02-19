class Aggregate:
    def create_iterator(self):
        pass


class Iterator:
    def next(self):
        pass

    def has_next(self):
        pass


class StringAggregator(Aggregate):
    def __init__(self):
        self.content = ""

    def create_iterator(self):
        return StringIterator(self)


class StringIterator(Iterator):
    def __init__(self, aggregator):
        self.aggregator = aggregator
        self.index = 0

    def next(self):
        if self.has_next():
            value = self.aggregator.content[self.index]
            self.index += 1
            return value
        else:
            return None

    def has_next(self):
        return self.index < len(self.aggregator.content)


class StringList:
    def __init__(self, *args):
        self.aggregator = StringAggregator()
        self.aggregator.content = args

    def get_iterator(self):
        return self.aggregator.create_iterator()


if __name__ == '__main__':
    my_list = StringList("Hello", "World")
    my_iterator = my_list.get_iterator()
    while my_iterator.has_next():
        print(my_iterator.next())
