from __future__ import annotations
from abc import ABC, abstractmethod

# The mediator interface declares a method used by components to notify the
# mediator about various events. The Mediator may react to these events and
# pass the execution to other components.
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender: Component, event: str) -> None:
        """
        Send a notification to interested components. The notification can be
        an update of the components state, or a request for component
        information.
        """
        pass


# The concrete mediator class. The intertwined web of connections between
# individual components has been untangled and moved to the mediator
class AuthenticationDialog(Mediator):
    _title: str
    _login_or_register_chekbox: Checkbox
    _login_username: TextBox
    _login_password: TextBox
    _registration_username: TextBox
    _registration_password: TextBox
    _registration_email: TextBox
    _ok_button: Button
    _cancel_button: Button

    def __init__(self, title: str, login_or_register_checkbox: Checkbox, login_username: TextBox, login_password: TextBox, registration_username: TextBox, registration_password: TextBox, registration_email: TextBox, ok_button: Button, cancel_button: Button) -> None:
        self._title = title
        self._login_or_register_chekbox = login_or_register_checkbox
        self._login_username = login_username
        self._login_password = login_password
        self._registration_username = registration_username
        self._registration_password = registration_password
        self._registration_email = registration_email
        self._ok_button = ok_button
        self._cancel_button = cancel_button

        self._login_or_register_chekbox.mediator = self
        self._login_username.mediator = self
        self._login_password.mediator = self
        self._registration_username.mediator = self
        self._registration_password.mediator = self
        self._registration_email.mediator = self
        self._ok_button.mediator = self
        self._cancel_button.mediator = self
        """Create all component objects and pass the current mediator
        into their constructors to establish links.

        When somehting happens with a component, it notifies the mediator.
        Upon receiving a notification, the mediator may do something on its
        own or pass the event to the appropriate component.
        """

    def notify(self, sender: Component, event: str) -> None:
        """
        The Mediator's notify method is called when one of the components
        sends a notification. The mediator may react to the event and pass
        execution to other components.
        """
        if sender == self._login_or_register_chekbox and event == 'check':
            if self._login_or_register_chekbox.checked:
                title = "Log in"
                # Show login form components
            else:
                title = "Register"
                # Show registration form components
                # Hide login form components

        if sender == self._ok_button and event == 'click':
            if self._login_or_register_chekbox.checked:
                # Try to find a user with the given username and password
                found = True
                if not found:
                    print("error message above the login field")
            else:
                # Create user account with the given username and password
                # Log user in
                pass


# Components communicate with a mediator using the mediator interface. Thanks
# to that, you can use the same components in other contexts by linking them
# with different mediator objects.
class Component:
    """
    The base component class declares an interface for all concrete
    components.
    """
    dialog: Mediator

    def __init__(self, dialog: Mediator) -> None:
        self.dialog = dialog

    def click(self) -> None:
        """
        Simulate a user clicking on this component.
        """
        self.dialog.notify(self, 'click')

    def keypress(self) -> None:
        """
        Simulate a user entering data into this component.
        """
        self.dialog.notify(self, 'keypress')


class Button(Component):
    """
    Concrete Components provide default implementations for the operations
    they support. There might be several variations of these classes.
    """
    def click(self) -> None:
        print("Button was clicked")

    def keypress(self) -> None:
        print("Button was keypressed")


class TextBox(Component):
    """
    Concrete Components provide default implementations for the operations
    they support. There might be several variations of these classes.
    """
    def click(self) -> None:
        print("TextBox was clicked")

    def keypress(self) -> None:
        print("TextBox was keypressed")


class Checkbox(Component):
    """
    Concrete Components provide default implementations for the operations
    they support. There might be several variations of these classes.
    """
    def click(self) -> None:
        print("Checkbox was clicked")

    def keypress(self) -> None:
        print("Checkbox was keypressed")
