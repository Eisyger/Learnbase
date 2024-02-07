import random


class Baum:
    def __init__(self, height, color):
        self.height = height
        self.color = color


class Birke(Baum):
    def __init__(self, height, color):
        super().__init__(height, color)
        self.name = "Birke"


class Ahorn(Baum):
    def __init__(self, height, color):
        super().__init__(height, color)
        self.name = "Ahorn"


class Flyweight:
    def __init__(self):
        self._trees = list()

    def get_tree(self, color: str, height: int, key: str):

        if key == "Birke":
            for tree in self._trees:
                if type(tree) is type(Birke):
                    print("Tree found.")
                    return tree
            new_tree = Birke(height, color)
            self._trees.append(new_tree)
            print("Tree created.")
            return new_tree

        elif key == "Ahorn":
            for tree in self._trees:
                if type(tree) is type(Ahorn):
                    print("Tree found.")
                    return tree
            new_tree = Ahorn(height, color)
            self._trees.append(new_tree)
            print("Tree created.")
            return new_tree

        elif key == "Color":
            for tree in self._trees:
                if tree.color == color:
                    print("Tree found.")
                    return tree
            new_tree = Baum(height, color)
            self._trees.append(new_tree)
            print("Tree created.")
            return new_tree

        elif key == "Height":
            for tree in self._trees:
                if tree.height == height:
                    print("Tree found.")
                    return tree
            new_tree = Baum(height, color)
            self._trees.append(new_tree)
            print("Tree created.")
            return new_tree

        else:
            raise Exception("Key konnte nich verarbeitet werden")


if __name__ == "__main__":
    fw = Flyweight()
    tree1 = fw.get_tree("green", 14, "Height")
    tree2 = fw.get_tree("blue", 14, "Height")
    tree3 = fw.get_tree("blue", 25, "Color")
    tree4 = fw.get_tree("blue", 25, "Color")
    print(tree1.color)
    print(tree2.height)
    print(type(tree3))
