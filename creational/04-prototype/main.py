from __future__ import annotations
from abc import ABC, abstractmethod
import copy


class Shape(ABC):
    def __init__(self) -> None:
        self.x = None
        self.y = None
        self._color = None


    @abstractmethod
    def describe_self(self) -> None:
        pass

    # Python doesn't accept multiple constructors and has a copy library to perform a copy, so we don't need to define a new method.
    def clone(self) -> Shape:
        return copy.copy(self)


class Rectangle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.width = None
        self.height = None

    def describe_self(self) -> None:
        return f"I'm a rectangle with width {self.width} and height {self.height}"


class Circle(Shape):
    def __init__(self) -> None:
        super().__init__()
        self.radius = None

    def describe_self(self) -> None:
        return f"I'm a circle with radius {self.radius}"


def run():
    shapes = []
    circle = Circle()
    circle.x = 10
    circle.y = 15
    circle.radius = 5
    shapes.append(circle)

    anotherCircle = circle.clone()
    shapes.append(anotherCircle)

    rectangle = Rectangle()
    rectangle.x = 1
    rectangle.y = 5
    rectangle.width = 10
    rectangle.height = 20
    shapes.append(rectangle)


    shapes_clone = []
    for shape in shapes:
        new_shape = shape.clone()
        shapes_clone.append(new_shape)

    for shape in shapes_clone:
        print(shape.describe_self())


if __name__ == '__main__':
    run()