# Python - Abstract Classes and Interfaces

## Project Overview

This project is part of the **Curriculum [C#25] Foundations v2 - Part 2** and focuses on **Object-Oriented Programming (OOP)** concepts in Python, specifically **Abstract Classes**, **Interfaces**, **Duck Typing**, and **Subclassing**. The goal is to deepen your understanding of these concepts through practical exercises and challenges.

### Project Details
- **Average Score**: 95.11%
- **Deadline**: 2025-02-09 (in 2 days)
- **Weight**: 1
- **Level**: Amateur
- **Author**: Javier Valenzani

---

## Learning Objectives

By completing this project, you will:
- **Understand and apply abstract classes** to define common interfaces while enforcing certain levels of class completeness.
- **Grasp the concept of interfaces and duck typing** to ensure that objects adhere to a specific contract or protocol.
- **Learn to extend standard base classes** like lists, dictionaries, and iterators to create custom data structures with specialized behavior.
- **Employ method overriding** to alter or enhance the behavior of base class methods.
- **Understand and apply multiple inheritance** to form complex relationships between classes.
- **Utilize mixins** to compose behavior across unrelated classes.

---

## Resources

To help you succeed in this project, here are some recommended resources:
- **Books**:
  - [Python 3 Object-Oriented Programming](https://www.amazon.com/Python-3-Object-Oriented-Programming/dp/1849511268)
- **Documentation**:
  - [ABC — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- **Tutorials**:
  - [Real Python - Object-Oriented Programming (OOP) in Python 3](https://realpython.com/python3-object-oriented-programming/)
  - [Corey Schafer - OOP Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)
  - [sentdex - Python OOP Tutorial](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfju7ADVp5W1GF9jVhjbX-_)

---

## Tasks

### 0. Abstract Animal Class and its Subclasses
- **Objective**: Create an abstract class `Animal` with an abstract method `sound`. Implement two subclasses, `Dog` and `Cat`, that override the `sound` method.
- **File**: `task_00_abc.py`
- **Instructions**:
  - Use the `abc` module to define the abstract class.
  - Implement `Dog` and `Cat` subclasses with their respective sounds.
  - Test the implementation by instantiating objects of `Dog` and `Cat`.

### 1. Shapes, Interfaces, and Duck Typing
- **Objective**: Create an abstract class `Shape` with abstract methods `area` and `perimeter`. Implement `Circle` and `Rectangle` classes. Write a function `shape_info` that uses duck typing to print the area and perimeter of any shape.
- **File**: `task_01_duck_typing.py`
- **Instructions**:
  - Define the `Shape` abstract class.
  - Implement `Circle` and `Rectangle` with their respective area and perimeter calculations.
  - Write the `shape_info` function to handle any shape object.

### 2. Extending the Python List with Notifications
- **Objective**: Create a `VerboseList` class that extends Python's built-in `list` class. Override methods like `append`, `extend`, `remove`, and `pop` to print notifications when items are added or removed.
- **File**: `task_02_verboselist.py`
- **Instructions**:
  - Extend the `list` class and override the specified methods.
  - Print notifications for each operation.
  - Test the class by performing list operations.

### 3. CountedIterator - Keeping Track of Iteration
- **Objective**: Create a `CountedIterator` class that extends the built-in iterator and keeps track of the number of items iterated over.
- **File**: `task_03_countediterator.py`
- **Instructions**:
  - Override the `__next__` method to increment a counter.
  - Provide a `get_count` method to retrieve the counter value.
  - Test the iterator with a loop or manual calls to `__next__`.

### 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance
- **Objective**: Create a `FlyingFish` class that inherits from both `Fish` and `Bird` classes. Override methods to demonstrate multiple inheritance and method resolution order (MRO).
- **File**: `task_04_flyingfish.py`
- **Instructions**:
  - Define `Fish` and `Bird` classes with appropriate methods.
  - Implement `FlyingFish` with overridden methods.
  - Test the class and explore the MRO using `mro()`.

### 5. The Mystical Dragon - Mastering Mixins
- **Objective**: Create mixin classes `SwimMixin` and `FlyMixin`, and then implement a `Dragon` class that inherits from both mixins.
- **File**: `task_05_dragon.py`
- **Instructions**:
  - Define `SwimMixin` and `FlyMixin` with `swim` and `fly` methods.
  - Implement `Dragon` with additional methods like `roar`.
  - Test the `Dragon` class by calling its methods.

---

## Repository Structure

```
holbertonschool-higher_level_programming/
└── python-abc/
    ├── task_00_abc.py
    ├── task_01_duck_typing.py
    ├── task_02_verboselist.py
    ├── task_03_countediterator.py
    ├── task_04_flyingfish.py
    └── task_05_dragon.py
```

---

## How to Run the Code

Each task has a corresponding `main_XX.py` file for testing. For example, to test Task 0, run:

```bash
./main_00_abc.py
```

---

## Scoring

Your score will be updated as you progress through the tasks. Ensure you complete all mandatory tasks before the deadline.

---

## Peer Review

Before submitting, review your work and ensure all tasks are completed correctly. Good luck! 🚀
