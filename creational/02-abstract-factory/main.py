from __future__ import annotations
from abc import ABC, abstractmethod

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_window(self) -> Window:
        pass

class WindowFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_window(self) -> Window:
        return WindowsWindow()


class MacFactory(GUIFactory):
    def create_button(self) -> Window:
        return MacButton()

    def create_window(self) -> Window:
        return MacWindow()


class Button(ABC):
    @abstractmethod
    def paint(self) -> None:
        pass


class Window(ABC):
    @abstractmethod
    def paint(self) -> None:
        pass

    @abstractmethod
    def alert(self) -> None:
        pass


class WindowsButton(Button):
    def paint(self) -> None:
        print('Painting Windows Button')


class MacButton(Button):
    def paint(self) -> None:
        print('Painting Mac Button')


class WindowsWindow(Window):
    def paint(self) -> None:
        print('Painting Windows Window')

    def alert(self) -> None:
        print("Alert 👓")


class MacWindow(Window):
    def paint(self) -> None:
        print("Painting MacOS Window")

    def alert(self) -> None:
        print("Alert 🍎")


def run(gui_creator: GUIFactory):
    button = gui_creator.create_button()
    window = gui_creator.create_window()

    button.paint()
    window.paint()
    window.alert()


if __name__ == "__main__":
    run(WindowFactory())
    run(MacFactory())