# Project Title: Python - Object-Relational Mapping

## Description  
This project explores the integration of **relational databases** with **Python** by using **MySQLdb** and **SQLAlchemy**. The first part focuses on executing **raw SQL queries** through MySQLdb, while the second part introduces **Object-Relational Mapping (ORM)** with SQLAlchemy, eliminating the need for direct SQL queries.

The key difference between both approaches is that ORM abstracts the database structure, allowing developers to interact with **Python objects** instead of writing SQL queries.

## Learning Objectives  
By completing this project, you will learn:
- How to connect to a MySQL database from a Python script.
- How to **SELECT, INSERT** rows in a MySQL table using Python.
- The concept of ORM and its advantages.
- How to map a **Python class** to a MySQL table using SQLAlchemy.

## Requirements  
- Ubuntu 20.04 LTS  
- Python 3.8.5  
- MySQL 8.0  
- MySQLdb module (version 2.0.x)  
- SQLAlchemy module (version 1.4.x)  
- Follow **Pycodestyle** (version 2.7.\*)  

## Installation  
### Install MySQL 8.0  
```bash
sudo apt update
sudo apt install mysql-server
mysql --version
```
### Install MySQLdb Module  
```bash
sudo apt-get install python3-dev libmysqlclient-dev zlib1g-dev
sudo pip3 install mysqlclient
```
### Install SQLAlchemy  
```bash
sudo pip3 install SQLAlchemy
```

## Usage  
The project contains scripts that perform various database operations using **both raw SQL and ORM**.

### Example: Fetching Data Without ORM  
```python
import MySQLdb

conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()
```

### Example: Fetching Data Using SQLAlchemy ORM  
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

engine = create_engine('mysql+mysqldb://root:root@localhost/my_db', pool_pre_ping=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
for state in session.query(State).order_by(State.id).all():
    print(f"{state.id}: {state.name}")
session.close()
```

## Tasks Overview  
### **Mandatory Tasks**
1. **Get all states** – Fetch all states from a database using MySQLdb.  
2. **Filter states** – Retrieve states whose name starts with "N".  
3. **Filter states by user input** – Accept a state name as an argument and retrieve matching results.  
4. **SQL Injection Protection** – Prevent SQL injection attacks.  
5. **Cities by states** – Fetch cities with state names.  
6. **First state model** – Define a SQLAlchemy model for the "states" table.  
7. **All states via SQLAlchemy** – Fetch all states using SQLAlchemy.  
8. **First state** – Retrieve the first state from the database.  
9. **Contains 'a'** – Fetch states that contain the letter "a".  
10. **Get a state by name** – Find a state based on user input.  
11. **Add a new state** – Insert a new state into the database.  
12. **Update a state** – Modify an existing state name.  
13. **Delete states** – Remove states that contain the letter "a".  
14. **Cities in a state** – Define a "City" model and retrieve city-state relationships.

## Repository Structure  
- **`model_state.py`** – SQLAlchemy model for the `states` table.  
- **`model_city.py`** – SQLAlchemy model for the `cities` table.  
- **Python scripts** – Each task is implemented in a separate script.  

## Author  
- **Holberton School**  
- **Project by Guillaume**  
- **Weight: 1**  

This project provides a hands-on approach to mastering MySQL integration with Python, improving database management skills for future applications.
