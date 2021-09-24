from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, Tuple

class GameAI(ABC):
    """The abstract class defines a template method that contains a skeleton
    of some algorithm composed of calls, usually to abstract primitive
    operations. Concrete subclasses implement these operations, but leave
    the template method itself intact."""
    built_structures: List[Structure]
    map_: Map
    resources: List[Resource]

    def turn(self) -> None:
        """The template method defines the skeleton of an algorithm."""

        self.collect_resources()
        self.build_structures()
        self.build_units()
        self.attack()

    def collect_resources(self) -> None:
        """Some of the steps may be implemented right in a base class."""
        for s in self.built_structures:
            s.collect()

    def closes_enemy(self) -> Enemy:
        """Finds and returns the closes enemy"""

    @abstractmethod
    def build_structures(self) -> None:
        pass

    @abstractmethod
    def build_units(self) -> None:
        pass

    """A class can have several template methods"""
    def attack(self):
        enemy: Enemy = self.closest_enemy()
        if not enemy:
            self.send_scouts(self.map_.center)
        else:
            self.send_warriors(enemy.position)

    @abstractmethod
    def send_scouts(self, position: Tuple[int, int]) -> None:
        pass

    @abstractmethod
    def send_warriors(self, position: Tuple[int, int]) -> None:
        pass


"""Concrete classes have to implement all abstract operations of the base class
but they must not override the template method itself."""
class OrcsAI(GameAI):
    def build_structures(self) -> None:
        if self.resources:
            """Build farms, then barracks, then stronghold"""

    def build_units(self) -> None:
        if self.resources.length > 100:
            if not self.resources.has_scouts():
                """Build peon, add it to scouts group"""
            else:
                """Build grunt, add it to warriors group"""

    def send_scouts(self, position: Tuple[int, int]) -> None:
        if self.resources.has_scouts():
            """Send scouts to position"""

    def send_warriors(self, position: Tuple[int, int]) -> None:
        if self.resources.has_warriors():
            """Send warriors to position"""


class MonstersAI(GameAI):
    def collect_resources(self) -> None:
        """Monsters don't collect resources"""

    def build_units(self) -> None:
        """Monsters don't build units"""

    def build_structures(self) -> None:
        """Monsters don't build structures"""


class Structure:
    """Base structure of the game"""
    def collect(self):
        """Collect resources"""


class Enemy:
    """Base enemy"""
    position: Tuple[int, int]


class Map:
    """Base map"""
    center: Tuple[int, int]


class Resource:
    """Base resource"""
    position: Tuple[int, int]
