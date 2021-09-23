from abc import ABC, abstractmethod


class Strategy(ABC):
    """The strategy interface declares operations common to all supported
    versions of some algorithm. The context uses this interface to call the
    algorithm defined by the concrete strategies."""

    @abstractmethod
    def execute(self, a: int, b: int) -> int:
        pass

"""Concrete Strategies implement the algorithm while following the base
Strategy interface. The interface makes them interchangeable in the context."""

class ConcreteStrategyAdd(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a + b


class ConcretStrategySubstract(Strategy):
    def execute(self, a: int, b: int) -> int:
        return a - b

"""The Context defines the interface of interest to clients."""

class Context:
    """The context maintains a reference to one of the strategy objects. The
    context doesn't know the concrete class of a strategy. It should work with
    all strategies via the interface."""
    _strategy: Strategy

    def set_strategy(self, strategy: Strategy) -> None:
        """Usually the contesxt accepts a strategy through the constructor, and
        also provides a setter so that the strategy can be switched at runtime."""
        self._strategy = strategy

    def execute_strategy(self, a: int, b: int) -> int:
        """The Context delegates some work to the Strategy object instead of
        implementing multiple versions of the algorithm on its own."""
        return self._strategy.execute(a, b)


if __name__ == "__main__":
    """The client code picks a concrete strategy and passes it to the context. The client should be aware of the differences between strategies in order to make
    the right choice."""
    context = Context()

    print("Enter first number")
    a = int(input())

    print("Enter second number")
    b = int(input())

    print("Enter operation (addition/subtraction)")
    operation = input()

    if operation == "addition":
        context.set_strategy(ConcreteStrategyAdd())
    elif operation == "subtraction":
        context.set_strategy(ConcretStrategySubstract())
    else:
        print("Operation not supported")
        exit()

    result = context.execute_strategy(a, b)
    print(f"Result: {result}")
