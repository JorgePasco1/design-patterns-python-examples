from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any


class Builder(ABC):
    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def set_seats(self) -> None:
        pass

    @abstractmethod
    def set_engine(self) -> None:
        pass

    @abstractmethod
    def set_trip_computer(self) -> None:
        pass

    @abstractmethod
    def set_gps(self) -> None:
        pass


class CarBuilder(Builder):
    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Car()

    @property
    def product(self) -> Car:
        result = self._product
        self.reset()
        return result

    def set_seats(self, seat_count) -> None:
        self._product.seats = seat_count

    def set_engine(self, engine_name) -> None:
        self._product.engine = engine_name

    def set_trip_computer(self) -> None:
        self._product.trip_computer = True

    def set_gps(self) -> None:
        self._product.gps = True


class CarManualBuilder(Builder):
    def __init__(self) -> None:
        """
        A fresh builder instance should contain a blank product object, which is
        used in further assembly.
        """
        self.reset()

    def reset(self) -> None:
        self._product = CarManual()

    @property
    def product(self) -> CarManual:
        result = self._product
        self.reset()
        return result

    def set_seats(self) -> None:
        self._product.add(f"Seats")

    def set_engine(self) -> None:
        self._product.add('Engine')

    def set_trip_computer(self) -> None:
        self._product.add('Trip Computer')

    def set_gps(self) -> None:
        self._product.add('GPS')


class Car:
    def __init__(self) -> None:
        self.seats = None
        self.engine = None
        self.trip_computer = False
        self.gps = False

    def describe_car(self) -> None:
        print(f"""Car properties:
        - Seats: {self.seats}
        - Engine: {self.engine}
        - Trip Computer: {self.trip_computer}
        - GPS: {self.gps}""")



class CarManual:
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Parts of the manual: {', '.join(self.parts)}")


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_sports_car(self):
        self._builder.reset()
        self._builder.set_seats(2)
        self._builder.set_engine('400 hp engine')
        self._builder.set_trip_computer()
        self._builder.set_gps()

    def build_suv_car(self):
        self._builder.reset()
        self._builder.set_seats(4)
        self._builder.set_engine('200 hp engine')

    def build_car_manual(self):
        self._builder.reset()
        self._builder.set_seats()
        self._builder.set_engine()
        self._builder.set_gps()
        self._builder.set_trip_computer()


def run():
    director = Director()

    car_builder = CarBuilder()
    car_manual_builder = CarManualBuilder()

    director.builder = car_builder
    director.build_sports_car()
    sports_car = car_builder.product
    sports_car.describe_car()

    director.build_suv_car()
    suv_car = car_builder.product
    suv_car.describe_car()

    director.builder = car_manual_builder
    director.build_car_manual()
    car_manual = car_manual_builder.product
    car_manual.list_parts()


if __name__ == "__main__":
    run()