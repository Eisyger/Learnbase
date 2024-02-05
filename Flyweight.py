import random


class Baum:
    def __init__(self, height, color):
        self.height = height
        self.color = color


class Birke(Baum):
    def __init__(self, height, color):
        super().__init__(height, color)


class Ahorn(Baum):
    def __init__(self, height, color):
        super().__init__(height, color)


class Flyweight:
    def __init__(self):
        self._count = 0
        self._colors = ["green", "red", "yellow"]
        self.height_range = range(5, 20)
        self.birken = list()
        self.ahorne = list()
        self._generate_trees(20)

    def _generate_trees(self, count):
        for _ in range(count):
            self.birken.append(Birke(random.randint(5, 20), random.choice(self._colors)))
            self.ahorne.append(Ahorn(random.randint(5, 20), random.choice(self._colors)))

    def get_tree(self, color, height, tree_type="Ahorn"):
        if tree_type == "Ahorn":
            searched_tree = [t for t in self.ahorne if t.color == color and t.height == height]
            if searched_tree:
                print("Baum gefunden")
                return searched_tree[0]
            else:
                print("Baum erstellt")
                return Ahorn(height, color)
        elif tree_type == "Birke":
            searched_tree = [t for t in self.birken if t.height == height]
            if searched_tree:
                print("Baum gefunden")
                return searched_tree[0]
            else:
                print("Baum erstellt")
                return Ahorn(height, color)


if __name__ == "__main__":
    fw = Flyweight()
    birke = fw.get_tree("green", 14, "Birke")
    ahorn = fw.get_tree("green", 11, "Ahorn")
    print(birke.color)
    print(ahorn.height)
