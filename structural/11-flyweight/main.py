# The flyweight class contains a portion of the state of a
# tree. These fields store values that are unique for each
# particular tree. For instance, you won't find here the tree
# coordinates. But the texture and colors shared between many
# trees are here. Since this data is usually BIG, you'd waste a
# lot of memory by keeping it in each tree object. Instead, we
# can extract texture, color and other repeating data into a
# separate object which lots of individual tree objects can
# reference.
from typing import Dict, Tuple


class TreeType:
    name: str
    color: str
    texture: str

    def __init__(self, name: str, color: str, texture: str):
        self.name = name
        self.color = color
        self.texture = texture

    def draw(self, canvas, x, y):
        return f"""Creating bitmap given type color and texture.
        Drawing bitmap on {canvas} at {x} and {y}"""


# Flyweight factory decides whether to
# flyweight or to create a new object.
class TreeFactory:
    _treeTypes: Dict[Tuple[str, str, str], TreeType] = {}

    def getTreeType(self, name, color, texture):
        _type = self._treeTypes.get((name, color, texture))
        if _type is None:
            _type = TreeType(name, color, texture)
            self._treeTypes[(name, color, texture)] = _type


# The contextual object contains the extrinsic part of the tree state. An
# application can create billions of these since they are pretty small: just
# two integer coordinates and one reference field.
class Tree:
    x: int
    y: int
    _type: TreeType

    def __init__(self, x, y, treeType):
        self.x = x
        self.y = y
        self._type = treeType

    def draw(self, canvas):
        return self._type.draw(canvas, self.x, self.y)


class Forest:
    _trees: Dict[Tuple[int, int], Tree] = {}

    def plantTree(self, x, y, name, color, texture):
        _type = TreeFactory().getTreeType(name, color, texture)
        self._trees[(x, y)] = Tree(x, y, _type)

    def draw(self, canvas):
        for tree in self._trees.values():
            tree.draw(canvas)
