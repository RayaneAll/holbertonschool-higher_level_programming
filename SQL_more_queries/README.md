# SQL - More Queries

## Description

This project focuses on expanding SQL skills by working with more advanced queries, user management, and database constraints. The main objectives include managing user privileges, handling primary and foreign keys, using constraints like `NOT NULL` and `UNIQUE`, and performing advanced SQL queries such as `JOIN`, `UNION`, and subqueries.

## Learning Objectives

By the end of this project, you should be able to:

- Create and manage MySQL users.
- Assign and manage privileges for users on databases and tables.
- Understand and use `PRIMARY KEY` and `FOREIGN KEY`.
- Apply `NOT NULL` and `UNIQUE` constraints effectively.
- Retrieve data from multiple tables in a single request.
- Understand and utilize subqueries.
- Work with `JOIN` and `UNION` to manipulate data efficiently.

## Requirements

- **Allowed Editors**: `vi`, `vim`, `emacs`
- **Execution Environment**: Ubuntu 20.04 LTS with MySQL 8.0 (version 8.0.25)
- **File Formatting**:
  - All SQL files must end with a new line.
  - Each SQL file should start with a comment describing the task.
  - SQL keywords should be in **uppercase** (e.g., `SELECT`, `WHERE`).
  - Each query must have a comment just before execution.
- **A `README.md` file is mandatory** at the root of the project folder.
- **File length will be tested using `wc`**.

## Setup Instructions

### Install MySQL 8.0 on Ubuntu 20.04 LTS

```sh
sudo apt update
sudo apt install mysql-server
mysql --version
```

### Connect to MySQL Server

```sh
sudo mysql
```

### Start MySQL in the Sandbox

If using the sandbox environment:

```sh
service mysql start
```

## Tasks Overview

1. **List MySQL User Privileges** - Retrieve and display the privileges of users `user_0d_1` and `user_0d_2`.
2. **Create a New User** - Create `user_0d_1` with all privileges on the MySQL server.
3. **Create a Read-Only User** - Create `user_0d_2` with only `SELECT` privilege on the `hbtn_0d_2` database.
4. **Enforce NOT NULL Constraint** - Create a table `force_name` ensuring the `name` column cannot be null.
5. **Set Default ID Value** - Define a table `id_not_null` where `id` has a default value of `1`.
6. **Enforce Unique ID** - Create a table `unique_id` where `id` must be unique.
7. **Create a States Table** - Define the `states` table with an auto-generated `id` and a `name` column.
8. **Create a Cities Table with Foreign Key** - Define the `cities` table linked to the `states` table.
9. **List Cities in California** - Query the database to retrieve all cities in California (without using `JOIN`).
10. **List Cities with Their States** - Retrieve all cities with their corresponding states using a `JOIN`.
11. **List TV Shows with Genres** - Query the `hbtn_0d_tvshows` database for shows with at least one genre.
12. **Include Shows Without Genres** - Modify the previous query to include shows with no genres (`NULL` values).
13. **Count Shows by Genre** - List all genres and the number of shows associated with each.
14. **List Genres for a Specific Show** - Retrieve all genres associated with the show "Dexter".
15. **Find Only Comedy Shows** - List all TV shows that belong to the Comedy genre.
16. **List Shows with Their Genres** - Retrieve all shows and their respective genres, ensuring `NULL` is displayed for shows without genres.

## Repository Structure

- **GitHub Repository**: `holbertonschool-higher_level_programming`
- **Project Directory**: `SQL_more_queries`
- **Files**:
  - `0-privileges.sql` - Lists privileges for MySQL users.
  - `1-create_user.sql` - Creates a MySQL user with all privileges.
  - `2-create_read_user.sql` - Creates a read-only user.
  - `3-force_name.sql` - Creates a table with a `NOT NULL` constraint.
  - `4-never_empty.sql` - Creates a table with a default `id` value.
  - `5-unique_id.sql` - Creates a table with a unique `id`.
  - `6-states.sql` - Defines the `states` table.
  - `7-cities.sql` - Defines the `cities` table with a foreign key.
  - `8-cities_of_california_subquery.sql` - Retrieves cities in California.
  - `9-cities_by_state_join.sql` - Retrieves all cities with their states.
  - `10-genre_id_by_show.sql` - Lists shows with at least one genre.
  - `11-genre_id_all_shows.sql` - Lists all shows, including those without genres.
  - `12-no_genre.sql` - Lists all shows with no associated genre.
  - `13-count_shows_by_genre.sql` - Counts the number of shows per genre.
  - `14-my_genres.sql` - Retrieves genres for the show "Dexter".
  - `15-comedy_only.sql` - Lists all comedy shows.
  - `16-shows_by_genre.sql` - Lists shows and their genres.

## Conclusion

This project enhances SQL skills by focusing on user management, constraints, relationships, and complex queries. By completing the tasks, you will gain a solid understanding of database design, query optimization, and MySQL administration. 🚀