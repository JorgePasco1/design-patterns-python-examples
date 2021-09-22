# Strategy

## Concept

_Behavioral Design Pattern that lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable._

### Problem

* On day you decided to create a navigation app for casual travelers.
* One of the most requested features for the app was automatic route planning.
* The first version of the app could only build the routes over roads. Next update, you added option to build walking routes. Then another one for public transport.
* That's only the beginning, then you planed to add route for cyclists, then for through all of city's tourist atractions.

### Solution

* The **Strategy** pattern suggests that you take a class that does something specific in a lot of different ways and extract all of these algorithms into separate classes called *strategies*.
* The original class, called *context*, must have a field for storing a reference to one of the strategies. The context delegates the work to a linked strategy object, instead of executing it on its own.
* The context isn't responsible for selecting an appropiate algorithm for the job. Instead, the client passes the desired stategy to the context. In fact, the context doesn't know much about strategies.
* In out navigation app, each routing algorithm can be extracted to its own class with a single `buildRoute` method.

## Structure

![Strategy Structure](structure.png)

## Pros and Cons

### Pros

### Cons
