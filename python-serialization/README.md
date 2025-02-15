# Python Serialization Project

## Description
This project focuses on the concepts of marshaling and serialization in Python. It covers various techniques to serialize and deserialize data using different formats such as JSON, Pickle, CSV, and XML. The project is designed to enhance your understanding of data handling, storage, and transmission in real-world applications.

## Learning Objectives
- Understand the differences and similarities between marshaling and serialization.
- Implement serialization in practical programming tasks.
- Use serialized data in web applications, databases, and network communications.
- Evaluate the performance implications of different serialization formats (JSON, XML, binary).

## Tasks

### 0. Basic Serialization
**Objective:** Create a basic serialization module that serializes a Python dictionary to a JSON file and deserializes the JSON file to recreate the Python dictionary.

**Instructions:**
- Write a Python module named `task_00_basic_serialization.py` with the following functions:
  - `serialize_and_save_to_file(data, filename)`: Serializes the dictionary `data` and saves it to the specified JSON file.
  - `load_and_deserialize(filename)`: Loads and deserializes the JSON file to return a Python dictionary.

**Example:**
```python
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data_to_serialize, 'data.json')
deserialized_data = load_and_deserialize('data.json')
print(deserialized_data)
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-serialization`
- File: `task_00_basic_serialization.py`

---

### 1. Pickling Custom Classes
**Objective:** Learn how to serialize and deserialize custom Python objects using the `pickle` module.

**Instructions:**
- Create a custom Python class named `CustomObject` with attributes: `name`, `age`, and `is_student`.
- Implement a `display` method to print the object's attributes.
- Implement two methods:
  - `serialize(self, filename)`: Serializes the object and saves it to the specified file.
  - `@classmethod deserialize(cls, filename)`: Deserializes the object from the specified file and returns an instance of `CustomObject`.

**Example:**
```python
from task_01_pickle import CustomObject

obj = CustomObject(name="John", age=25, is_student=True)
obj.serialize("object.pkl")
new_obj = CustomObject.deserialize("object.pkl")
new_obj.display()
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-serialization`
- File: `task_01_pickle.py`

---

### 2. Converting CSV Data to JSON Format
**Objective:** Convert data from CSV format to JSON format using serialization techniques.

**Instructions:**
- Write a function `convert_csv_to_json(csv_filename)` that reads a CSV file, converts it to a list of dictionaries, and serializes it to a JSON file named `data.json`.
- Handle exceptions such as file not found.

**Example:**
```python
from task_02_csv import convert_csv_to_json

csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-serialization`
- File: `task_02_csv.py`

---

### 3. Serializing and Deserializing with XML
**Objective:** Serialize and deserialize data using XML as an alternative format to JSON.

**Instructions:**
- Write two functions:
  - `serialize_to_xml(dictionary, filename)`: Serializes a Python dictionary to an XML file.
  - `deserialize_from_xml(filename)`: Deserializes an XML file and returns a Python dictionary.

**Example:**
```python
from task_03_xml import serialize_to_xml, deserialize_from_xml

sample_dict = {
    'name': 'John',
    'age': '28',
    'city': 'New York'
}

xml_file = "data.xml"
serialize_to_xml(sample_dict, xml_file)
deserialized_data = deserialize_from_xml(xml_file)
print(deserialized_data)
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-serialization`
- File: `task_03_xml.py`

---

## Resources
- [Real Python Serialization](https://realpython.com/python-serialization/)
- [Real Python: Working With JSON Data in Python](https://realpython.com/python-json/)
- [Python’s pickle documentation](https://docs.python.org/3/library/pickle.html)
- [Corey Schafer on Pickle](https://www.youtube.com/watch?v=2Tw39kZIbhs)
- [CSV to JSON in Python](https://realpython.com/python-csv/)
- [Python XML ElementTree Guide](https://docs.python.org/3/library/xml.etree.elementtree.html)
- [Socket Programming Guide](https://realpython.com/python-sockets/)

---

## Score
- **Project Badge:** 0%
- **Your score will be updated as you progress.**

---

## Tasks List
### Mandatory
- [ ] 0. Basic Serialization
- [ ] 1. Pickling Custom Classes
- [ ] 2. Converting CSV Data to JSON Format
- [ ] 3. Serializing and Deserializing with XML

---

**Note:** Please review all the tasks before starting the peer review.
