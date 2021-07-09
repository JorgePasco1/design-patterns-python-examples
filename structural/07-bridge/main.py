from __future__ import annotations
from abc import ABC, abstractmethod


class RemoteControl:
    _device: Device
    def __init__(self, device: Device) -> None:
        self._device = device

    def toggle_power(self) -> None:
        self._device.disable() if self._device.is_enabled() else self._device.enable()

    def volume_down(self) -> None:
        self._device.set_volume(self._device.get_volume() - 10)

    def volume_up(self) -> None:
        self._device.set_volume(self._device.get_volume() + 10)

    def channel_down(self) -> None:
        self._device.set_channel(self._device.get_channel() - 1)

    def channel_up(self) -> None:
        self._device.set_channel(self._device.get_channel() + 1)


# We can extend classes from the abstraction hierarchy independently from the device class
class AdvancedRemoteControl(RemoteControl):
    def mute(self) -> None:
        print(f"Muting {self._device._device_name}")
        self._device.set_volume(0)


class Device(ABC):
    _max_channel: int
    _max_volume: int
    _device_name: str
    def __init__(self, volume=None, channel=None) -> None:
        self.volume = volume or 10
        self.channel = channel or 1
        self.enabled = False

    def is_enabled(self) -> bool:
        return self.enabled

    def get_volume(self) -> int:
        return self.volume

    def get_channel(self) -> int:
        return self.channel

    @abstractmethod
    def enable(self) -> None:
        pass

    @abstractmethod
    def disable(self) -> None:
        pass

    @abstractmethod
    def set_volume(self, volume: int) -> None:
        pass

    @abstractmethod
    def set_channel(self, channel: int) -> None:
        pass


class Tv(Device):
    def __init__(self, volume, channel) -> None:
        super().__init__(volume=volume, channel=channel)
        self._max_channel = 200
        self._max_volume = 100
        self._device_name = "Tv"

    def enable(self) -> None:
        if not self.enabled:
            print("Turning on TV")
        self.enabled = True

    def disable(self) -> None:
        if self.enabled:
            print("Turning off TV")
        self.enabled = False

    def set_volume(self, volume: int) -> None:
        if volume > self._max_volume:
            return print("Max Volume reached")
        self.volume = volume

    def set_channel(self, channel) -> None:
        if channel > self._max_channel:
            if self.channel == self._max_channel:
                self.channel = 1
            return print("Max channel reached")
        self.channel = channel


class Radio(Device):
    def __init__(self, volume, channel) -> None:
        super().__init__(volume=volume, channel=channel)
        self._max_channel = 50
        self._max_volume = 50
        self._device_name = "Radio"

    def enable(self) -> None:
        if not self.enabled:
            print("Turning on Radio")
        self.enabled = True

    def disable(self) -> None:
        if self.enabled:
            print("Turning off Radio")
        self.enabled = False

    def set_volume(self, volume: int) -> None:
        if volume > self._max_volume:
            return print("Max Volume reached")
        self.volume = volume

    def set_channel(self, channel) -> None:
        if channel > self._max_channel:
            if self.channel == self._max_channel:
                self.channel = 1
            return print("Max channel reached")
        self.channel = channel


def run():
    tv = Tv(20, 199)
    remote = RemoteControl(tv)
    remote.toggle_power()
    remote.toggle_power()
    print(tv.get_channel())
    remote.channel_up()
    print(tv.get_channel())
    remote.channel_up()
    print(tv.get_channel())

    radio = Radio(50, 1)
    remote = AdvancedRemoteControl(radio)
    remote.mute()


if __name__ == "__main__":
    run()
