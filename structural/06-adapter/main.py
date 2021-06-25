from __future__ import annotations
import math


class RoundHole:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius

    def fits(self, peg: RoundPeg) -> bool:
        return self.get_radius() >= peg.get_radius()


class RoundPeg:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def get_radius(self) -> float:
        return self.radius


# Incompatible class (Service)
class SquarePeg:
    def __init__(self, width: float) -> None:
        self.width = width

    def get_width(self) -> float:
        return self.width


class SquarePegAdapter(RoundPeg):
    def __init__(self, peg: SquarePeg) -> None:
        self.peg = peg

    # Adapts the Square Peg to be usable by the Round Hole fits method
    def get_radius(self) -> float:
        return self.peg.width * math.sqrt(2) / 2


def run() -> None:
    hole = RoundHole(5)
    round_peg = RoundPeg(5)
    print(f"Round peg fits hole: {hole.fits(round_peg)}")

    small_sqpeg = SquarePeg(5)
    large_sqpeg = SquarePeg(10)
    # print(hole.fits(small_sqpeg)) # AttributeError: 'SquarePeg' object has no attribute 'get_radius'

    small_sqpeg_adapter = SquarePegAdapter(small_sqpeg)
    large_sqpeg_adapter = SquarePegAdapter(large_sqpeg)

    print(hole.fits(small_sqpeg_adapter)) # True
    print(hole.fits(large_sqpeg_adapter)) # False


if __name__ == "__main__":
    run()
