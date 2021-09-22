from __future__ import annotations
from abc import ABC
from typing import List


class AudioPlayer:
    """This class acts as a context. It also mantains a reference to an
    instance of one of the state classes that represents the current
    state of the audio player."""
    state: State
    ui: UserInterface
    volumne: int
    playlist: List[str]
    current_song: str
    is_playing: bool

    def __init__(self):
        self.state = ReadyState(self)

        """Context delegates hadling user input to a state object. Naturally,
        the outcome depends on what state is currently active, since each
        state can handle the input differently"""
        self.ui = UserInterface()
        self.ui.lock_button.on_click(self.click_lock)
        self.ui.play_button.on_click(self.click_play)
        self.ui.next_button.on_click(self.click_next)
        self.ui.prev_button.on_click(self.click_prev)

    def change_state(state: State) -> None:
        self.state = state

    """UI methods delegate execution to the active state"""
    def click_lock(self) -> None:
        self.state.click_lock()

    def click_play(self) -> None:
        self.state.click_play()

    def click_next(self) -> None:
        self.state.click_next()

    def click_previous(self) -> None:
        self.state.click_previous()

    """A state may call some service methods on the context"""
    def start_playback(self) -> None:
        pass

    def stop_playback(self) -> None:
        pass

    def next_song(self) -> None:
        pass

    def prev_song(self) -> None:
        pass

    def fast_forward(time: str) -> None:
        pass

    def rewind(time: str) -> None:
        pass


class State(ABC):
    _player: AudioPlayer

    def __init__(self, player: AudioPlayer) -> None:
        """Context passes itself through the state constructor. This may
        help a state fetch some useful context data if it's needed."""
        self._player = player


class LockedState(State):
    """Concrete states implement various behaviors associated with a state
    of the context."""

    def click_lock(self) -> None:
        """When you unlock a locked player, it may assume one of two
        states."""
        if self._player.is_playing:
            self._player.change_state(PlayingState(self._player))
        else:
            self._player.change_state(ReadyState(self._player))

    def click_play(self) -> None:
        """Locked. Do nothing"""

    def click_next(self) -> None:
        """Locked. Do nothing"""

    def click_previous(self) -> None:
        """Locked. Do nothing"""


class ReadyState(State):
    """They can also trigger state transitions in the context"""
    def click_lock(self) -> None:
        self._player.change_state(LockedState(self._player))

    def click_play(self) -> None:
        self._player.start_playback()
        self._player.change_state(PlayingState(self._player))

    def click_next(self) -> None:
        self._player.next_song()

    def click_previous(self) -> None:
        self._player.prev_song()


class PlayingState(State):
    def click_lock(self) -> None:
        self._player.change_state(LockedState(self._player))

    def click_play(self) -> None:
        self._player.stop_playback()
        self._player.change_state(ReadyState(self._player))

    def click_next(self, event) -> None:
        if event.double_click:
            self._player.next_song()
        else:
            self._player.fast_forward(5)

    def click_previous(self, event) -> None:
        if event.double_click:
            self._player.prev_song()
        else:
            self._player.rewind(5)
