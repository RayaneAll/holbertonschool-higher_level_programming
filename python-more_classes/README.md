# Python - More Classes and Objects

## Description
This project is part of the **Curriculum [C#25] Foundations v2 - Part 2** and focuses on deepening the understanding of **Object-Oriented Programming (OOP)** in Python. The project explores advanced concepts such as classes, objects, attributes, methods, properties, and special methods like `__init__`, `__str__`, and `__repr__`. It also covers class attributes, instance attributes, class methods, static methods, and dynamic attribute creation.

The project consists of several tasks, each building on the previous one, to create a `Rectangle` class with increasing functionality. By the end of the project, you will have a solid understanding of how to work with classes and objects in Python.

---

## Learning Objectives
By the end of this project, you will be able to explain the following concepts without the help of Google:

- **General**
  - Why Python programming is awesome.
  - What is OOP and "first-class everything."
  - The difference between a class, an object, and an instance.
  - What are attributes, methods, and properties.
  - The difference between public, protected, and private attributes.
  - The purpose of `self`, `__init__`, `__str__`, and `__repr__`.
  - Data Abstraction, Data Encapsulation, and Information Hiding.
  - The difference between class attributes and instance attributes.
  - How to use class methods and static methods.
  - How to dynamically create attributes and bind them to objects or classes.
  - How Python finds attributes of an object or class.
  - How to use the `getattr` function.

---

## Resources
### Read or Watch:
- [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (Read everything until the paragraph “Inheritance” (excluded)).
- [Object-Oriented Programming in Python](https://python-course.eu/oop/properties-vs-getters-and-setters.php) (Focus on specific sections as outlined in the project description).
- [Class and Instance Attributes](https://python-course.eu/oop/class-instance-attributes.php).
- [Classmethods and Staticmethods](https://python-course.eu/oop/classmethods-and-staticmethods.php).
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php).
- [str vs repr](https://python-course.eu/oop/str-vs-repr.php).

---

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **python3 (version 3.8.5)**.
- All files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/python3`.
- A `README.md` file, at the root of the project folder, is mandatory.
- Your code should use the `pycodestyle` (version 2.7.*).
- All files must be executable.
- The length of your files will be tested using `wc`.

---

## Tasks
### Mandatory
1. **Simple Rectangle**  
   - Write an empty class `Rectangle` that defines a rectangle.

2. **Real Definition of a Rectangle**  
   - Define a `Rectangle` class with private attributes `width` and `height`, along with getters and setters.

3. **Area and Perimeter**  
   - Add methods to calculate the area and perimeter of the rectangle.

4. **String Representation**  
   - Implement `__str__` and `__repr__` methods to provide string representations of the rectangle.

5. **Eval is Magic**  
   - Modify `__repr__` to allow recreating a new instance using `eval()`.

6. **Detect Instance Deletion**  
   - Print a message when an instance of `Rectangle` is deleted.

7. **How Many Instances**  
   - Add a class attribute to track the number of instances created and deleted.

8. **Change Representation**  
   - Add a class attribute `print_symbol` to customize the string representation of the rectangle.

9. **Compare Rectangles**  
   - Implement a static method to compare two rectangles based on their area.

10. **A Square is a Rectangle**  
    - Add a class method to create a square (a rectangle with equal width and height).

---

## Advanced
- Dynamically create new attributes for existing instances.
- Bind attributes to objects and classes.
- Understand how Python finds attributes using `__dict__`.
- Use the `getattr` function to retrieve attributes dynamically.

---

## Repository
- **GitHub Repository:** [holbertonschool-higher_level_programming](https://github.com/holbertonschool/higher_level_programming)
- **Directory:** `python-more_classes`

---

## Score
- **Average Score:** 94.88%
- **Project Badge:** Earned upon completion.

---

## Author
- **Guillaume**  
  Weight: 1  
  Your score will be updated as you progress.

---

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/holbertonschool/higher_level_programming.git
   ```
2. Navigate to the project directory:
   ```bash
   cd higher_level_programming/python-more_classes
   ```
3. Run the scripts:
   ```bash
   ./<task-number>-main.py
   ```

---

## Example Usage
### Task 0: Simple Rectangle
```python
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
```

### Task 1: Real Definition of a Rectangle
```python
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
```

---

## Conclusion
This project is designed to help you master the concepts of classes and objects in Python. By completing the tasks, you will gain a deeper understanding of OOP principles and how to apply them in real-world scenarios. Good luck!