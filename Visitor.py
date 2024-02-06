from abc import ABCMeta, abstractmethod


class IVisitor(metaclass=ABCMeta):
    @abstractmethod
    def visit_circle(self, circle):
        pass

    @abstractmethod
    def visit_triangle(self, triangle):
        pass


class IShape(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass


class Circle(IShape):
    def accept(self, visitor):
        visitor.visit_circle(self)


class Triangle(IShape):
    def accept(self, visitor: IVisitor):
        visitor.visit_triangle(self)


class AreaVisitor(IVisitor):
    def visit_circle(self, circle: Circle):
        print(f"Berechne die Fläche des Kreises mit Radius.")

    def visit_triangle(self, triangle: Triangle):
        print("Berechne die Fläche des Dreiecks.")


class PerimeterVisitor(IVisitor):
    def visit_circle(self, circle: Circle):
        print(f"Berechne den Umfang des Kreises mit Radius.")

    def visit_triangle(self, triangle: Triangle):
        print("Berechne den Umfang des Dreiecks.")


if __name__ == "__main__":
    circle = Circle()
    triangle = Triangle()

    area_visitor = AreaVisitor()
    perimeter_visitor = PerimeterVisitor()

    circle.accept(area_visitor)
    circle.accept(perimeter_visitor)

    triangle.accept(area_visitor)
    triangle.accept(perimeter_visitor)
