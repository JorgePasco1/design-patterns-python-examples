from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Shape(ABC):
    """The element interface declares an `accept` method that takes the base
    visitor interface as an argument"""

    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class Dot(Shape):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(f"Dot at ({self.x}, {self.y})")

    def accept(self, visitor: Visitor) -> None:
        """Note that we're using `visit_dot`, which matches the current class name.
        This way we let the visitor know the class of element it works with."""
        visitor.visit_dot(self)


class Circle(Shape):
    def __init__(self, x: int, y: int, radius: int) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(f"Circle at ({self.x}, {self.y}) with radius {self.radius}")

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(f"Rectangle at ({self.x}, {self.y}) with width {self.width} and height {self.height}")

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_rectangle(self)


class CompoundShape(Shape):
    def __init__(self) -> None:
        self.shapes = []

    def accept(self, visitor: Visitor) -> None:
        visitor.visit_compound_shape(self)


class Visitor(ABC):
    @abstractmethod
    def visit_dot(self, dot: Dot) -> None:
        pass

    @abstractmethod
    def visit_circle(self, circle: Circle) -> None:
        pass

    @abstractmethod
    def visit_rectangle(self, rectangle: Rectangle) -> None:
        pass

    @abstractmethod
    def visit_compound_shape(self, compound_shape: CompoundShape) -> None:
        pass


"""Concrete visitors implement several versions of the same algorithm, which can
work with all concrete element classes.

You can experience the biggest benefit of the Visitor pattern when using it with
a complex object structure, such as a Composite tree. In this case, it might be
helpful to store some intermediate state of the algorithm while executing the
visitor's method over various objects of the structure"""

class XMLExportVisitor(Visitor):
    def visit_dot(self, dot: Dot) -> None:
        """Export the dot's ID and center coordinates"""

    def visit_circle(self, circle: Circle) -> None:
        """Export the circle's ID, center coordinates and radius"""

    def visit_rectangle(self, rectangle: Rectangle) -> None:
        """Export the rectangle's ID, left-top coordinates and dimensions"""

    def visit_compound_shape(self, compound_shape: CompoundShape) -> None:
        """Export the compound shape's ID and all its child shapes"""


def main():
    all_shapes: List[Shape] = [
        Dot(10, 20),
        Circle(30, 40, 50),
        Rectangle(60, 70, 80, 90)
    ]

    compound_shape = CompoundShape()
    compound_shape.shapes = all_shapes

    export_visitor = XMLExportVisitor()

    for shape in all_shapes:
        shape.accept(export_visitor)


if __name__ == "__main__":
    main()
