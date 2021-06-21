from __future__ import annotations
from abc import ABC, abstractmethod


class TextDisplayer(ABC):
    """ Creator class """

    @abstractmethod
    def create_display_screen(self):
        """ Factory method """
        pass

    def show_text(self) -> str:
        """ Core logic """
        display_screen = self.create_display_screen()

        print(f"Displaying text from {display_screen.mention()}")


class WebDisplayer(TextDisplayer):
    def create_display_screen(self) -> Screen:
        return WebScreen()


class WindowsDisplayer(TextDisplayer):
    def create_display_screen(self) -> Screen:
        return WindowsScreen()



class Screen(ABC):
    """ Interface """

    @abstractmethod
    def mention(self) -> str:
        pass


class WebScreen(Screen):
    def mention(self) -> str:
        return "Web Screen"


class WindowsScreen(Screen):
    def mention(self) -> str:
        return "Windows Screen"


def run(text_displayer: TextDisplayer) -> None:
    text_displayer.show_text()


if __name__ == "__main__":
    run(WebDisplayer())
    run(WindowsDisplayer())