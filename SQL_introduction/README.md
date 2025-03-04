# SQL Introduction Project

This project is part of the **Curriculum [C#25] Foundations v2 - Part 2** and focuses on introducing SQL concepts and basic database operations using MySQL. The goal is to familiarize yourself with relational databases, SQL syntax, and common database operations such as creating, querying, and modifying tables.

---

## Project Overview

### Description
This project introduces the basics of SQL and MySQL. You will learn how to create and manage databases, write SQL queries, and perform operations like inserting, updating, and deleting data. The project also covers subqueries, functions, and advanced querying techniques.

### Learning Objectives
By the end of this project, you should be able to:
- Explain what a database and a relational database are.
- Understand what SQL stands for and its role in database management.
- Create and manage databases and tables in MySQL.
- Write SQL queries to retrieve, insert, update, and delete data.
- Use subqueries and MySQL functions effectively.
- Understand the difference between DDL (Data Definition Language) and DML (Data Manipulation Language).

---

## Resources

### Reading Materials
- [What is Database & SQL?](https://example.com)
- [Install MySQL (MySQL Server)](https://example.com)
- [A Basic MySQL Tutorial](https://example.com)
- [Basic SQL statements: DDL and DML](https://example.com)
- [Basic queries: SQL and RA](https://example.com)
- [SQL technique: functions](https://example.com)
- [SQL technique: subqueries](https://example.com)
- [MySQL Cheat Sheet](https://example.com)
- [MySQL 8.0 SQL Statement Syntax](https://example.com)

---

## Requirements

### General
- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be executed on **Ubuntu 20.04 LTS** using **MySQL 8.0**.
- All files should end with a new line.
- All SQL queries should have a comment just before the query.
- All files should start with a comment describing the task.
- SQL keywords should be in uppercase (e.g., `SELECT`, `WHERE`).
- A `README.md` file at the root of the project folder is mandatory.
- The length of your files will be tested using `wc`.

---

## Tasks

### Mandatory Tasks
1. **List databases**  
   Write a script that lists all databases on your MySQL server.  
   File: `0-list_databases.sql`

2. **Create a database**  
   Write a script that creates the database `hbtn_0c_0`. If it already exists, the script should not fail.  
   File: `1-create_database_if_missing.sql`

3. **Delete a database**  
   Write a script that deletes the database `hbtn_0c_0`. If it doesn’t exist, the script should not fail.  
   File: `2-remove_database.sql`

4. **List tables**  
   Write a script that lists all tables in a given database.  
   File: `3-list_tables.sql`

5. **First table**  
   Write a script that creates a table `first_table` with columns `id` (INT) and `name` (VARCHAR(256)).  
   File: `4-first_table.sql`

6. **Full description**  
   Write a script that prints the full description of the table `first_table`.  
   File: `5-full_table.sql`

7. **List all in table**  
   Write a script that lists all rows in the table `first_table`.  
   File: `6-list_values.sql`

8. **First add**  
   Write a script that inserts a new row into `first_table` with `id = 89` and `name = "Best School"`.  
   File: `7-insert_value.sql`

9. **Count 89**  
   Write a script that displays the number of records with `id = 89` in `first_table`.  
   File: `8-count_89.sql`

10. **Full creation**  
    Write a script that creates a table `second_table` and inserts multiple rows.  
    File: `9-full_creation.sql`

11. **List by best**  
    Write a script that lists all records in `second_table` ordered by score (descending).  
    File: `10-top_score.sql`

12. **Select the best**  
    Write a script that lists all records in `second_table` with a score >= 10.  
    File: `11-best_score.sql`

13. **Cheating is bad**  
    Write a script that updates the score of `Bob` to 10 in `second_table`.  
    File: `12-no_cheating.sql`

14. **Score too low**  
    Write a script that removes all records with a score <= 5 in `second_table`.  
    File: `13-change_class.sql`

15. **Average**  
    Write a script that computes the average score of all records in `second_table`.  
    File: `14-average.sql`

16. **Number by score**  
    Write a script that lists the number of records with the same score in `second_table`.  
    File: `15-groups.sql`

17. **Say my name**  
    Write a script that lists all records in `second_table` with a non-null `name` value, ordered by score (descending).  
    File: `16-no_link.sql`

---

## How to Use

### Setting Up MySQL
1. **Install MySQL**  
   Update your package list and install MySQL:
   ```bash
   sudo apt update
   sudo apt install mysql-server
   ```

2. **Start MySQL Service**  
   Start the MySQL service:
   ```bash
   service mysql start
   ```

3. **Connect to MySQL**  
   Connect to the MySQL server using the MySQL CLI:
   ```bash
   mysql -uroot -p
   ```

### Running Scripts
To execute a script, use the following command:
```bash
cat <script_name>.sql | mysql -hlocalhost -uroot -p
```

---

## Example Queries

### List Databases
```sql
-- Lists all databases
SHOW DATABASES;
```

### Create a Table
```sql
-- Creates a table named first_table
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
```

### Insert Data
```sql
-- Inserts a new row into first_table
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
```

---

## Author
- **Guillaume**  
  Project contributor and mentor.

---

## Repository
- GitHub: [holbertonschool-higher_level_programming](https://github.com/holbertonschool/holbertonschool-higher_level_programming)  
- Directory: `SQL_introduction`
