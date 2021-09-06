from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Callable


class Button():
    _command: Command

    def set_command(self, command: Command):
        self._command = command


class Shortcuts():
    mapper: Dict[str, Command]

    def on_key_press(self, key: str, fun: Callable) -> None:
        self.mapper[key] = fun


class Command(ABC):
    _app: Application
    _editor: Editor
    _backup: str

    def __init__(self, app: Application, editor: Editor) -> None:
        self._app = app
        self._editor = editor

    def save_backup(self) -> None:
        """Make a backup of the editor's state"""
        self._backup = self._editor.text

    def undo(self) -> None:
        """Restore the editor's state"""
        self._editor.text = self._backup

    @abstractmethod
    def execute(self) -> bool:
        """The execution method is declared abstract to force all concrete
        commands to provide their own implementations. The method must
        return true or false depending on wether the command changes the
        editor's state"""


class CopyCommand(Command):
    """The copy command isn't saved to the history since it doesn't change the
    editor's state."""
    def execute(self) -> bool:
        self._app.clipboard = self._editor.get_selection()
        return False


class CutCommand(Command):
    """Does change the editor's state, therefore it must be save to the history.
    And it'll be saved as long as the method returns true."""
    def execute(self) -> bool:
        self.save_backup()
        self._editor.replace_selection(self._app.clipboard)
        return True


class UndoCommand(Command):
    def execute(self) -> bool:
        self._app.undo()
        return False


class CommandHistory:
    """Just a stack"""
    _history: List[Command]

    def push(self, c: Command) -> None:
        """Push the command to the end of the history array"""
        self._history.append(c)

    def pop(self) -> Optional[Command]:
        return len(self._history) > 0 and self._history[-1]


class Editor:
    """Holds actual text editing operations. It plays the role of a receiver:
    all commands end up delegating execution to the editor's methods."""
    text: str

    def get_selection() -> str:
        """Returns selected text"""

    def delete_selection() -> None:
        """Deletes selected text"""

    def replace_selection(text: str) -> None:
        """Insert the clipboard's contents at the current position"""


class Application:
    _clipboard: str
    _editors: List[Editor]
    _history: CommandHistory
    _current_editor: Editor
    copy_button = Button()
    cut_button = Button()
    undo_button = Button()
    shortcuts = Shortcuts()

    def execute_command(self, c: Command) -> None:
        if (c.execute()):
            self._history.push(c)

    def undo(self) -> None:
        """Take the most recent command from the history and run its undo method.
        Note that we don't know the class of that command. But we don't have to,
        since the command knows how to undo its own action"""
        command = self._history.pop()
        if (command):
            command.undo()

    def create_ui(self) -> None:
        """Creates the application's UI"""
        def copy() -> None:
            self.execute_command(CopyCommand(self, self._current_editor))

        def cut() -> None:
            self.execute_command(CutCommand(self, self._current_editor))

        def undo() -> None:
            self.execute_command(UndoCommand(self, self._current_editor))


        self.copy_button.set_command(copy)
        self.shortcuts.on_key_press("Ctrl+C", copy)

        self.cut_button.set_command(cut)
        self.shortcuts.on_key_press("Ctrl+X", cut)

        self.undo_button.set_command(undo)
        self.shortcuts.on_key_press("Ctrl+Z", undo)
