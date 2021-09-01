from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

# The handler interface declares a method for building a chain of handlers.
# It also declares a method for executing a request.
class ComponentWithContextualHelp(ABC):
    @abstractmethod
    def show_help(self) -> str:
        pass


# The base class for simple components.
class AbstractComponent(ComponentWithContextualHelp):
    tooltip_text: str = None

    # The component's container acts as the next link in the chain
    _container: AbstractContainer = None

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # The component shows a tooltip if there's help text assigned to it.
    # Otherwise it forwards teh call to the container, if it exists.
    def show_help(self) -> str:
        if (self.tooltip_text):
            return "This is a tooltip"
        return self._container.show_help()


# COntainers can contain both simple components and other containers as children.
# The chain relationships are established here. The class inheriths show_help
# behavior from it parent
class AbstractContainer(AbstractComponent):
    _children: List[AbstractComponent]

    def add(self, child: AbstractComponent) -> None:
        self._children.append(child)
        child._container = self

    def show_help(self) -> str:
        return "This is a container"


# Primitive components may be fine with default help implementation...
class Button(AbstractComponent):
    def __init__(self, x: int, y: int, width: int, height: int, text: str) -> None:
        super().__init__(x, y, width, height)
        self.text = text

    pass


# But complex components may override the default implementation. If the help
# text can't be provided in a new way, the component can always call the base
# implementation (see AbstractComponent class)
class Panel(AbstractContainer):
    modal_help_text: str

    def show_help(self) -> str:
        if self.modal_help_text:
            return f"Showing a modal window at ({self.x}, {self.y}) with a width of {self.width} and a height of {self.height} with the help text"
        else:
            return super().show_help()


class Dialog(AbstractContainer):
    wiki_page_url: str

    def show_help(self) -> str:
        if self.wiki_page_url:
            return "Opening wiki help page"
        else:
            return super().show_help()


class Application:
    def create_ui(self) -> None:
        dialog = Dialog("Budget Reports")
        dialog.wiki_page_url = "https://www.wikipedia.com/example"
        panel = Panel(0, 0, 400, 800)
        panel.modal_help_text = "This panel does something awesome"
        ok = Button(320, 760, 50, 20, "OK")
        ok.tooltip_text = "This is an OK button"
        cancel = Button(320, 730, 50, 20, "Cancel")

        panel.add(ok)
        panel.add(cancel)
        dialog.add(panel)

    def get_component_at_mouse_coord(self, mouse_x: int, mouse_y: int) -> AbstractComponent:
        new_comp = Button(mouse_x, mouse_y, 10, 10, "OK")
        new_comp._container = Dialog(100, 200, 10, 10)
        return new_comp

    def on_f1_key_pressed(self) -> str:
        component = self.get_component_at_mouse_coord(320, 760)
        return component.show_help()


if __name__ == "__main__":
    app = Application()
    app.on_f1_key_pressed()
