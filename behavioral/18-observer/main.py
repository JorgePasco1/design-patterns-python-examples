from abc import ABC, abstractmethod


class EventManager:
    """Base publisher class. Includes subscription management code and
    notification methods"""
    _listeners: dict # Hash map of event types and listeners

    def subscribe(self, event_type: str, listener: callable) -> None:
        """Add a listener for a given event type"""
        self._listeners[event_type].append(listener)

    def unsubscribe(self, event_type: str, listener: callable) -> None:
        """Remove a listener for a given event type"""
        self._listeners[event_type].remove(listener)

    def notify(self, event_type: str, data) -> None:
        """Notify all listeners of a given event type"""
        for listener in self._listeners[event_type]:
            listener.update(data)


class Editor:
    """The concrete publisher contains real business logic that's
    interesting for some subscribers. We could derive this class from the
    base publisher, but that isn't always possible in real life, because
    the concrete publisher might already be a subclass. In this case, you
    can patch the subscription logic in with composition."""
    events: EventManager
    _file: bytes

    def __init__(self) -> None:
        self.events = EventManager()

    # Methods of business logic can notify subscribers about changes
    def open_file(self, path: str):
        self._file = open(path, 'rb').read()
        self.events.notify('open', self._file)

    def save_file(self):
        self._file.write()
        self.events.notify('save', self._file)


class EventListener(ABC):
    """Subscriber interface"""

    @abstractmethod
    def update(self, filename: str) -> None:
        pass


class LoggingListener(EventListener):
    """Concrete subscriber that logs events"""
    _log: bytes
    _message: str

    def __init__(self, log_filename, message) -> None:
        self._log = open(log_filename, 'wb')
        self._message = message

    def update(self, filename: str) -> None:
        self._log.write(self._message.encode())


class EmailAlertsListener(EventListener):
    _email: str
    _message: str

    def __init__(self, email: str, message) -> None:
        self._email = email
        self._message = message

    def update(self, filename: str) -> None:
        # Send email
        pass


if __name__ == "__main__":
    # Create a concrete publisher
    editor = Editor()

    logger = LoggingListener('log.txt', 'Someone has oppened the file')
    editor.events.subscribe('open', logger)

    email_alerts = EmailAlertsListener(
        "admin@example.com",
        "Someone has changed the file"
    )
    editor.events.subscribe('save', email_alerts)
