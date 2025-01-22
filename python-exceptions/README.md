# Python - Exceptions

![Project Badge](https://img.shields.io/badge/Project-95.31%25-success)

This project is part of the **[C#25] Foundations v2 - Part 2** curriculum and introduces the concept of **exception handling** in Python. You will learn to identify, handle, and raise exceptions to create robust and resilient programs.

---

## Table of Contents
1. [Project Description](#project-description)
2. [Learning Objectives](#learning-objectives)
3. [Prerequisites and Requirements](#prerequisites-and-requirements)
4. [Task List](#task-list)
5. [Resources](#resources)
6. [License](#license)
7. [Project Status](#project-status)
8. [Credits](#credits)

---

## Project Description

This project focuses on **exception handling** in Python, a critical aspect of developing robust software. You will learn to:
- Differentiate between errors and exceptions.
- Use `try`, `except`, and `finally` blocks to handle exceptions.
- Raise custom exceptions.
- Manage unexpected runtime scenarios while maintaining program stability.

---

## Learning Objectives

By the end of this project, you will be able to:
- Explain the difference between **errors** and **exceptions**.
- Use Python’s built-in exceptions.
- Decide when and how to use exceptions.
- Use the `finally` block to execute cleanup actions after an exception.
- Raise built-in exceptions using `raise`.
- Handle exceptions to improve program reliability.

---

## Prerequisites and Requirements

### Prerequisites
- Basic knowledge of control structures (`if`, `for`, `while`) in Python.
- Familiarity with list manipulation.

### Technical Requirements
- **Operating System**: Ubuntu 20.04 LTS.
- **Python Version**: Python 3.8.5.
- **Allowed Editors**: `vi`, `vim`, `emacs`.
- **Code Style**: Adhere to **pycodestyle** (version 2.7.*).

### Constraints
- All files must be **executable**.
- Each file must start with the shebang line:  
  ```bash
  #!/usr/bin/python3
  ```
- A `README.md` file must be present in the project root.
- File length will be tested using `wc`.

---

## Task List

### 0. Safe list printing
Create a function that prints the first `x` elements of a list, handling exceptions if `x` exceeds the list size.  
**File**: `0-safe_print_list.py`

---

### 1. Safe printing of an integers list
Create a function that prints an integer using `"{:d}".format()`. The function returns `True` if the value is an integer, otherwise `False`.  
**File**: `1-safe_print_integer.py`

---

### 2. Print and count integers
Create a function that prints the first `x` elements of a list, but only integers, silently ignoring other types.  
**File**: `2-safe_print_list_integers.py`

---

### 3. Integers division with debug
Create a function that divides two integers and displays the result in a `finally` block. The function returns the division result or `None` in case of an error.  
**File**: `3-safe_print_division.py`

---

### 4. Divide a list
Create a function that divides two lists element by element and returns a new list with the results. Handle errors such as `wrong type`, `division by 0`, and `out of range`.  
**File**: `4-list_division.py`

---

### 5. Raise exception
Create a function that raises a `TypeError` exception.  
**File**: `5-raise_exception.py`

---

### 6. Raise a message
Create a function that raises a `NameError` exception with a custom message.  
**File**: `6-raise_exception_msg.py`

---

## Resources

- [Python Documentation: Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Video Tutorial: Exceptions and Error Handling](https://www.youtube.com/watch?v=NMZGLzHBxT8)

---

## License

This project follows the **Holberton School Curriculum License**. Refer to your institutional documentation for more details.

---

## Project Status

The project is **95.31% complete**.

---

## Credits

Created by **Guillaume** as part of the **Holberton School Foundations v2** curriculum.