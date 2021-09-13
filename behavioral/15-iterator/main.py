from __future__ import annotations
from abc import ABC, abstractmethod
from collections.abc import Iterable, Iterator
from typing import List


# The collection interface must declare a factory method for creating
# iterators. You can declare several methods if there are differrent kinds of
# iteration available in your program.
class SocialNetwork(ABC):
    @abstractmethod
    def create_friends_iterator(self, profile_id: str) -> Iterator:
        pass

    @abstractmethod
    def create_coworkers_iterator(self, profile_id: str) -> Iterator:
        pass


# Each concrete collection is coupled to a set of concrete iterator classes
# it returns. But the client isn't, since the signature of these methods
# returns iterator interfaces
class Facebook(SocialNetwork):
    ################################################
    # Bulk of the collection's code should go here...
    ################################################
    def social_graph_request(profile_id: str, type: str):
        pass

    def create_friends_iterator(self, profile_id: str) -> FacebookIterator:
        return FacebookIterator(self, profile_id, 'friends')

    def create_coworkers_iterator(self, profile_id: str) -> FacebookIterator:
        return FacebookIterator(self, profile_id, 'coworkers')


class Profile:
    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

    def __str__(self):
        return f'{self.name} ({self.id})'


class ProfileIterator(ABC, Iterator):
    """
    This attribute indicates the traversal direction.
    """
    _reverse: bool = False

    def has_more(self) -> bool:
        return self._position is not None

    @abstractmethod
    def __next__(self) -> Profile:
        pass


# The common interface for all iterators
class FacebookIterator(ProfileIterator):
    _facebook: Facebook
    _profile_id: str
    _type: str

    # An iterator object traverses the collection independently from other
    # iterators. Therefore it has to store the iteration state.
    _current_position: int = 0
    _cache: List[Profile]

    def __init__(self, facebook: Facebook, profile_id: str, type: str) -> None:
        self._facebook = facebook
        self._profile_id = profile_id
        self._type = type


    def lazy_init(self):
        if self._cache is None:
            self._cache = self._facebook.social_graph_request(
                self._profile_id, self._type)


    def __next__(self):
        """
        The __next__() method must return the next item in the sequence. On
        reaching the end, and in subsequent calls, it must raise StopIteration.
        """
        if self.has_more():
            self._current_position += 1
            return self._cache[self._current_position]

    def has_more(self) -> bool:
        self.lazy_init()
        return self._current_position < len(self._cache)


# Here is another useful trick: You can pass an iterator to a client class
# instead of giving it acces to a whole collection. This way, you don't
# expose the collection to the client.

# And there is another benefit: You can change the way the client workds with
# the collection at runtime by passing it a different iterator. This is
# possible because the client code isn't coupled to the concrete iterator classes.
class SocialSpammer:
    def send(self, iterator: ProfileIterator, message: str):
        while iterator.has_more():
            profile = next(iterator)
            print(f'Sending email to {profile}. Message: {message}')


if __name__ == '__main__':
    network =  Facebook()
    spammer = SocialSpammer()

    profile = Profile('John', 'john.doe')

    # Send spam to friends
    iterator = network.create_friends_iterator(profile.id)
    spammer.send(iterator, 'Very important message')

    # Send spam to coworkers
    iterator = network.create_coworkers_iterator(profile.id)
    spammer.send(iterator, 'Important message')
