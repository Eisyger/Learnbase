class MyList:
    class Node:
        def __init__(self):
            self.content = None
            self.next = None

    def __init__(self):
        self._head = None
        self._current = None
        self.count = None

    def add(self, content):
        node = self.Node()
        node.content = content

        if self._head is None:
            self._head = node
            self.count = 1
        else:
            self._current = self._head
            while self._current.next is not None:
                self._current = self._current.next
            self._current.next = node
            self.count += 1

    def remove(self, index):
        if index < 0 or index > self.count - 1:
            raise IndexError()

        if index == 0:
            self._head = self._head.next

        else:
            self._current = self._head.next
            current_index = 1
            before = self._head
            while current_index < index:
                before = self._current
                self._current = self._current.next
                current_index += 1
            before.next = self._current.next
            self.count -= 1

    def get_index(self, index):
        if index < 0 or index > self.count - 1:
            raise IndexError()

        if index == 0:
            return self._head.content

        else:
            i = 1
            self._current = self._head.next
            while i < index:
                self._current = self._current.next
                i += 1
            return self._current.content

    def dump(self):
        index = 0
        self._current = self._head
        while index < self.count:
            print(self._current.content)
            self._current = self._current.next
            index += 1


class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def next(self):
        if self.has_next():
            value = self.collection.get_index(self.index)
            self.index += 1
            return value
        else:
            raise StopIteration

    def has_next(self):
        return self.index < self.collection.count


if __name__ == '__main__':
    my_list = MyList()
    my_list.add("Hallo")
    my_list.add("wie")
    my_list.add("läufts")
    my_list.add("gehts")
    my_list.add("den so?")
    my_list.remove(2)
    my_list.dump()
    print(my_list.get_index(2))

    my_iterator = Iterator(my_list)
    while my_iterator.has_next():
        print(my_iterator.next())
