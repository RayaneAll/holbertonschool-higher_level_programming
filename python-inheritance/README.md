# Python - Inheritance

![Project Badge](https://img.shields.io/badge/Python-Inheritance-blue)

## Description

This project is part of the **Curriculum [C#25] Foundations v2 - Part 2** and focuses on understanding and implementing inheritance in Python. The project covers various concepts related to inheritance, including superclasses, subclasses, multiple inheritance, method overriding, and the use of built-in functions like `isinstance`, `issubclass`, `type`, and `super`.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts without the help of Google:

- **General**
  - What is a superclass, baseclass, or parentclass
  - What is a subclass
  - How to list all attributes and methods of a class or instance
  - When can an instance have new attributes
  - How to inherit a class from another
  - How to define a class with multiple base classes
  - What is the default class every class inherits from
  - How to override a method or attribute inherited from the base class
  - Which attributes or methods are available by heritage to subclasses
  - What is the purpose of inheritance
  - What are, when and how to use `isinstance`, `issubclass`, `type`, and `super` built-in functions

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use `pycodestyle` (version 2.7.*)
- All files must be executable
- The length of your files will be tested using `wc`

### Python Test Cases
- Allowed editors: `vi`, `vim`, `emacs`
- All files should end with a new line
- All test files should be inside a folder `tests`
- All test files should be text files (extension: `.txt`)
- All tests should be executed using the command: `python3 -m doctest ./tests/*`
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation should be meaningful and not just a simple word
- Do not use the words `import` or `from` inside your comments

## Tasks

### 0. Lookup
Write a function `lookup(obj)` that returns the list of available attributes and methods of an object.

**File:** `0-lookup.py`

### 1. My list
Write a class `MyList` that inherits from `list` and includes a method `print_sorted(self)` that prints the list in ascending order.

**File:** `1-my_list.py`, `tests/1-my_list.txt`

### 2. Exact same object
Write a function `is_same_class(obj, a_class)` that returns `True` if the object is exactly an instance of the specified class; otherwise `False`.

**File:** `2-is_same_class.py`

### 3. Same class or inherit from
Write a function `is_kind_of_class(obj, a_class)` that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise `False`.

**File:** `3-is_kind_of_class.py`

### 4. Only sub class of
Write a function `inherits_from(obj, a_class)` that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise `False`.

**File:** `4-inherits_from.py`

### 5. Geometry module
Write an empty class `BaseGeometry`.

**File:** `5-base_geometry.py`

### 6. Improve Geometry
Write a class `BaseGeometry` with a public instance method `area(self)` that raises an `Exception` with the message `area() is not implemented`.

**File:** `6-base_geometry.py`

### 7. Integer validator
Write a class `BaseGeometry` with a public instance method `integer_validator(self, name, value)` that validates the value.

**File:** `7-base_geometry.py`, `tests/7-base_geometry.txt`

### 8. Rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` and includes instantiation with `width` and `height`.

**File:** `8-rectangle.py`

### 9. Full rectangle
Write a class `Rectangle` that inherits from `BaseGeometry` and includes the `area()` method and a custom `__str__` method.

**File:** `9-rectangle.py`

### 10. Square #1
Write a class `Square` that inherits from `Rectangle` and includes instantiation with `size`.

**File:** `10-square.py`

### 11. Square #2
Write a class `Square` that inherits from `Rectangle` and includes a custom `__str__` method.

**File:** `11-square.py`

## Score

Your score will be updated as you progress through the tasks.

---

**Note:** Please review all the tasks before starting the peer review.