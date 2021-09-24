# Template Method

## Concept

_Behavioral Design Pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm withouth changing its structure._

### Problem

* You're creating a data mining application that analyzes corporate documents. Users feed the app documents in various formats (PDF, DOC, CSV), and it tries to extract meaningful data from these docs in a uniform format.
* The first version could only work with DOC files. In the following version, it was able to support CSV, then you "taught" it to extract data from PDF files.
* At some point, you noticed that all three classes have a lot of similar code.

### Solution

* The **Template Method** pattern suggests that you break down an algorithm into a series of steps, turn these steps into a methods, and put a series of calls to these methods inside a single *template method*. These methods may either be `abstract` or have some default implementation.
* To use this algorithm, the client is supposed to provide its own subclass, implement all abstract steps, and override some of the optional ones if needed (but not the template method itself).

[Example Template Method](./example.png)

* *Abstract steps* must be implemented by every subclass.
* *Optional steps* already have some default implementation, but still can be overriden if needed.
* There's another type of step, called *hooks*, which is optional and has an empty body. A template method should work even if a hook isn't overriden.

## Structure

![Strategy Structure](structure.png)

1. The **Abstract Class** declares methods that act as steps of an algorithm, as well as the actual template method which calls these methods in specific order. The steps may either be declared abstract or have some default implementation.
2. **Concrete Classes** can override all of the steps, but not the template method itself.

## Pros and Cons

### Pros

* You can swap algorithms used inside an object at runtime.
* You can isolate the implementation details of an algorithm from the code that uses it.
* You can replace inheritance with composition.
* *Open/Closed Principle*.

### Cons

* If you only have a couple of algorithms and they rarely change, there's no real reason to overcomplicate the code.
* Clients must be aware of the differences between the strategies to be able to select a proper one.
* A lot of modern programming languages have functional type support that lets you implement different versions of an algorithm inside a set of anonymous functions. Then you could use these functions exactly as you'd have user the strategy objects, but withouth bloating the code.
