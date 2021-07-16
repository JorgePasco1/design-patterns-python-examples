from abc import ABC, abstractmethod
from typing import List


# The component interface declares common operations for both simple and complex objects of a composition.
class Graphic(ABC):
    x: int
    y: int

    @abstractmethod
    def move(self, x: int, y: int) -> None:
        pass

    @abstractmethod
    def draw(self) -> None:
        pass


# The leaf class respresents end objects of a composition. A leaf object can't have
# any sub-objects. Usually, it's leaf objects that do actual work, while composite
# objects only delegate to their sub-components.
class Dot(Graphic):
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self, x: int, y: int) -> None:
        self.x += x
        self.y += y

    def draw(self) -> None:
        print(f"Drawing a dot at ({self.x}, {self.y}).")


# All component classes can extend other components
class Circle(Dot):
    def __init__(self, x: int, y: int, radius: int) -> None:
        super().__init__(x, y)
        self.radius = radius

    def draw(self) -> None:
        print(f"Drawing a circle at ({self.x}, {self.y}) with a radius of {self.radius}.")

# The composite class represents complex components that may have children.
# Composite objects usually delegate the actual work to their children and
# then sum up the result
class CompoundGraphic(Graphic):
    children: List[Graphic]

    def __init__(self) -> None:
        self.children = []

    def add(self, child: Graphic) -> None:
        self.children.append(child)

    def remove(self, child: Graphic) -> None:
        self.children = [el for el in self.children if el != child]

    def move(self, x: int, y: int) -> None:
        for child in self.children:
            child.move(x, y)

    # A composite executes its primary logic in a particular way. It traverses
    # recursevely through all its children, collecting and summing up their
    # results. Since the composite's children pass these calls to their own
    # children and so forth, the whole object tree is traversed as a result
    def draw(self):
        for child in self.children:
            child.draw()
            print(f"Updating bounding figure with {child}")
        print(f"Drawing a dashed figure with coordinates: {self.children}")



class ImageEditor:
    _all: CompoundGraphic

    def load(self) -> None:
        self._all = CompoundGraphic()
        self._all.add(Dot(1, 2))
        self._all.add(Circle(5, 3, 10))
        self._all.add(Dot(8, 5))

    # Combine selected components into one complex composite component.
    def group_selected(self, components: List[Graphic]):
        group = CompoundGraphic()
        for comp in components:
            group.add(comp)
            self._all.remove(comp)
        self._all.add(group)
        self._all.draw()


def run():
    editor = ImageEditor()
    editor.load()
    print(editor._all.__dict__)
    editor.group_selected([editor._all.children[0], editor._all.children[1]])
    print(editor._all.__dict__)


if __name__ == "__main__":
    run()
