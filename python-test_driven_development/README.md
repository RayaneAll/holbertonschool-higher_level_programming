# Python - Test-Driven Development

![Project Badge](https://img.shields.io/badge/Project-95.98%25-success)

This project is part of the **[C#25] Foundations v2 - Part 2** curriculum and focuses on **Test-Driven Development (TDD)** in Python. You will learn to write tests before implementing code to ensure your programs function correctly and handle all possible cases, including edge cases.

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

**Test-Driven Development (TDD)** is a programming methodology that emphasizes writing tests before code. This approach improves the reliability, robustness, and readability of programs. This project will guide you in:
- Writing interactive tests using docstrings.
- Using the `unittest` module for unit testing.
- Documenting modules and functions in detail.
- Identifying and handling edge cases effectively.

---

## Learning Objectives

By the end of this project, you will be able to:
- Explain why testing is essential.
- Write interactive tests using docstrings and doctest.
- Use `unittest` for basic unit testing.
- Identify and test edge cases.
- Clearly document modules, functions, and tests.

---

## Prerequisites and Requirements

### Prerequisites
- Familiarity with functions and exceptions in Python.
- Experience with documentation and coding best practices.

### Technical Requirements

#### Python Scripts
- **Operating System**: Ubuntu 20.04 LTS.
- **Python Version**: Python 3.8.5.
- **Code Style**: Adhere to **pycodestyle** (version 2.7.*).
- All files must be **executable** and start with the shebang line:  
  ```bash
  #!/usr/bin/python3
  ```

#### Python Tests
- All test files must be located in a `tests/` folder.
- Tests must be executed with:  
  ```bash
  python3 -m doctest ./tests/*
  ```
- Unit tests must use `unittest` and be executed with:  
  ```bash
  python3 -m unittest tests.6-max_integer_test
  ```

---

## Task List

### 0. Integers addition
Create a function `add_integer(a, b=98)` that returns the sum of two integers. Raise an exception if the inputs are not integers or floats.  
**Files**: `0-add_integer.py`, `tests/0-add_integer.txt`

---

### 1. Divide a matrix
Create a function `matrix_divided(matrix, div)` that divides each element of a matrix by `div`. Handle exceptions for invalid data types and division by zero.  
**Files**: `2-matrix_divided.py`, `tests/2-matrix_divided.txt`

---

### 2. Say my name
Create a function `say_my_name(first_name, last_name="")` that prints the message:  
```text
My name is <first name> <last name>
```
Raise an exception if the arguments are not strings.  
**Files**: `3-say_my_name.py`, `tests/3-say_my_name.txt`

---

### 3. Print square
Create a function `print_square(size)` that prints a square of size `size` using the `#` character. Raise exceptions if `size` is not an integer or is negative.  
**Files**: `4-print_square.py`, `tests/4-print_square.txt`

---

### 4. Text indentation
Create a function `text_indentation(text)` that adds two new lines after each of the characters `.`, `?`, and `:`. Raise an error if `text` is not a string.  
**Files**: `5-text_indentation.py`, `tests/5-text_indentation.txt`

---

### 5. Max integer - Unittest
Write unit tests for the function `max_integer(list=[])`. Cover all possible cases, including empty lists and edge cases, using `unittest`.  
**File**: `tests/6-max_integer_test.py`

---

## Resources

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [Unit Tests in Python](https://realpython.com/python-testing/)
- [Video Tutorial: doctest and unittest](https://www.youtube.com/watch?v=6tNS--WetLI)

---

## License

This project follows the **Holberton School Curriculum License**. Refer to your institutional documentation for more details.

---

## Project Status

The project is **95.98% complete**. Keep working on the tasks to achieve a perfect score!

---

## Credits

Created by **Guillaume** as part of the **Holberton School Foundations v2** curriculum.