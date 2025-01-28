# Python - Classes and Objects  

![Project Badge](https://img.shields.io/badge/Progress-94.24%25-brightgreen)

This project immerses you in the fundamental concepts of Object-Oriented Programming (OOP) with Python. You will learn to work with **classes**, **objects**, and their components to develop structured and modular programs.

---

## Table of Contents  

1. [Context](#context)  
2. [Learning Objectives](#learning-objectives)  
3. [Concepts Covered](#concepts-covered)  
4. [Resources](#resources)  
5. [Task Details](#task-details)  
   - [0. My first square](#0-my-first-square)  
   - [1. Square with size](#1-square-with-size)  
   - [2. Size validation](#2-size-validation)  
   - [3. Area of a square](#3-area-of-a-square)  
   - [4. Access and update private attribute](#4-access-and-update-private-attribute)  
   - [5. Printing a square](#5-printing-a-square)  
   - [6. Coordinates of a square](#6-coordinates-of-a-square)  
6. [Technical Requirements](#technical-requirements)  
7. [How to Run Tests](#how-to-run-tests)  
8. [License](#license)  

---

## Context  

Object-Oriented Programming (OOP) is a fundamental pillar of modern software development. In this project, you will explore essential concepts such as **classes**, **objects**, **attributes**, and **methods**, while familiarizing yourself with the principles of abstraction, encapsulation, and information hiding.

---

## Learning Objectives  

By the end of this project, you will be able to:  
- Understand the basics of Object-Oriented Programming (OOP).  
- Create and manipulate **classes** and **objects**.  
- Understand the concepts of public, protected, and private attributes.  
- Implement methods and properties in a class.  
- Validate and manage attribute values using **getters** and **setters**.  
- Apply principles of abstraction and encapsulation in your Python programs.  

---

## Concepts Covered  

- **Class and Instance**: Differences and relationships.  
- **Special Methods**: `__init__`, `__dict__`.  
- **Encapsulation**: Public, protected, private.  
- **Attributes vs Properties**: Pythonic usage.  
- **Dynamic Manipulation**: Adding and managing attributes on the fly.  

---

## Resources  

Before starting, make sure to read or watch the following resources:  
1. [Introduction to OOP](https://realpython.com/python3-object-oriented-programming/)  
2. [Video: Learn to Program 9 - Object Oriented Programming](https://www.youtube.com/watch?v=rfscVS0vtbw&t=112s)  
3. [Python Properties](https://docs.python.org/3/library/functions.html#property)  
4. [Official Python Documentation on Classes](https://docs.python.org/3/tutorial/classes.html)  

---

## Task Details  

### 0. My first square  

Write an empty class `Square` that defines a square.  
- **Code**: File `0-square.py`  
- **Test**: Verify that you can instantiate a `Square` object.  

---

### 1. Square with size  

Add a private attribute `size` to the `Square` class.  
- Instantiation with a `size` attribute (without validation).  
- **Code**: File `1-square.py`.  

---

### 2. Size validation  

Add validation to the `size` attribute:  
- **Conditions**:  
  - `size` must be an integer.  
  - `size` >= 0, otherwise raise an exception.  
- **Code**: File `2-square.py`.  

---

### 3. Area of a square  

Add a public method `area()` that returns the area of the square.  
- **Code**: File `3-square.py`.  
- **Test**: Calculate the area for different sizes.  

---

### 4. Access and update private attribute  

Use **getters** and **setters** to access and update `size`.  
- Add value validation in the setter.  
- **Code**: File `4-square.py`.  

---

### 5. Printing a square  

Add a method `my_print()` that prints the square using the `#` character.  
- If `size` equals 0, print an empty line.  
- **Code**: File `5-square.py`.  

---

### 6. Coordinates of a square  

Add a `position` attribute to the `Square` class:  
- **Conditions**:  
  - `position` must be a tuple of two positive integers.  
  - Use spaces to adjust the printing of the square.  
- **Code**: File `6-square.py`.  

---

## Technical Requirements  

- Python 3.8.5 on Ubuntu 20.04 LTS.  
- Follow PEP 8 style guidelines (`pycodestyle` version 2.7.*).  
- Documentation is mandatory for:  
  - Modules.  
  - Classes.  
  - Methods and functions.  

---

## How to Run Tests  

1. **Run a file**:  
   ```bash
   python3 0-main.py
   ```  
2. **Check PEP 8 style**:  
   ```bash
   pycodestyle 0-square.py
   ```  
3. **Run all tests**:  
   Create tests in the `tests/` folder and use:  
   ```bash
   python3 -m unittest discover tests/
   ```  

---

## License  

This project is licensed under **Holberton School**.  

**Start exploring Python classes and objects now to gain a deep understanding of OOP!** 🚀  