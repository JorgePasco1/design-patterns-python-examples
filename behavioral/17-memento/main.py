"""This example uses the Memento pattern alongside the Com- mand pattern for storing snapshots of the complex text editor’s state and restoring an earlier state from these snapshots when needed. The command objects act as caretakers. They fetch the editor’s memento before executing operations related to commands. When a user attempts to undo the most recent command, the editor can use the memento stored in that command to revert itself to the previous state."""
from __future__ import annotations
from abc import ABC, abstractmethod

class Editor:
    """The originator holds some important data that may change over time.
    It also defines a method for saving its state inside a memento and
    another method for restoring the state from it"""
    _text: str
    _cur_x: int
    _cur_y: int
    _selection_width: int

    def set_text(self, text: str) -> None:
        self._text = text

    def set_cursor(self, x: int, y: int) -> None:
        self._cur_x = x
        self._cur_y = y

    def set_selection_widt(self, width: int) -> None:
        self._selection_width = width

    def create_snapshot(self) -> Snapshot:
        """Saves the current state inside a memento"""
        # Memento is an inmutable object; that's why the originator passes
        # its state to the memento's costructor paramenters.
        return Snapshot(self, self._text, self._cur_x, self._cur_y, self._selection_width)


class Snapshot:
    """The memento class stores the past state of the editor"""
    _editor: Editor
    _text: str
    _cur_x: int
    _cur_y: int
    _selection_width: int

    def __init__(self, editor: Editor, text: str, cur_x: int, cur_y: int, selection_width: int) -> None:
        self._editor = editor
        self._text = text
        self._cur_x = cur_x
        self._cur_y = cur_y
        self._selection_width = selection_width

    # At some point, a previous state of the editor can be restored using
    # the memento object.
    def restore(self) -> None:
        self._editor.set_text(self._text)
        self._editor.set_cursor(self._cur_x, self._cur_y)
        self._editor.set_selection_widt(self._selection_width)


class Command:
    """A command object can act as a caretaker. In that case, the command
    gets a memento just before it changes the originator's state. When undo
    is requested, it restores the originator's state from a memento."""
    _backup: Snapshot = None
    _editor: Editor

    def __init__(self, editor: Editor) -> None:
        self._editor = editor
        self.make_backup()

    def make_backup(self) -> None:
        self._backup = self._editor.create_snapshot()

    def undo(self) -> None:
        self._backup and self._backup.restore()
