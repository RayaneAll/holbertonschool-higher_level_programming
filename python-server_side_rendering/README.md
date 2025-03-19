# Python - Server-Side Rendering

## Project Overview
This project focuses on implementing **Server-Side Rendering (SSR)** in Python using the **Flask** framework and the **Jinja** templating engine. Unlike Client-Side Rendering (CSR), where the browser processes JavaScript to generate the UI dynamically, **SSR pre-generates fully formed HTML on the server and sends it to the client**, improving performance, SEO, and accessibility.

Through this project, we will progressively build a Flask web application that serves dynamic content using SSR techniques, leveraging various data sources including **JSON, CSV, and SQLite databases**.

---

## Learning Objectives
By completing this project, you will:
- Understand the differences between **server-side rendering (SSR)** and **client-side rendering (CSR)**.
- Learn the advantages of **SSR**, including **SEO-friendliness, faster initial page loads, and improved accessibility**.
- Use **Flask** as a web framework to implement **SSR**.
- Utilize **Jinja** templates for **dynamic HTML generation**.
- Read and process data from **JSON, CSV, and SQLite databases**.
- Handle **dynamic content** and user inputs effectively.

---

## Project Structure
The project is organized as follows:

```
python-server_side_rendering/
│── templates/         # HTML templates for rendering pages
│   ├── index.html     # Homepage template
│   ├── items.html     # Dynamic template with loops and conditions
│   ├── product_display.html # Template to display data from JSON, CSV, or SQLite
│   ├── header.html    # Reusable header template
│   ├── footer.html    # Reusable footer template
│── static/            # Static assets (CSS, images, JS if needed)
│── data/              # JSON and CSV files
│   ├── items.json     # Sample JSON file for dynamic rendering
│   ├── products.json  # Product data in JSON format
│   ├── products.csv   # Product data in CSV format
│── task_00_intro.py   # Script for basic templating with placeholders
│── task_01_jinja.py   # Flask app with basic Jinja templates
│── task_02_logic.py   # Flask app with loops & conditions in Jinja templates
│── task_03_files.py   # Flask app that reads data from JSON & CSV
│── task_04_db.py      # Flask app that integrates SQLite database
│── products.db        # SQLite database containing product data
│── README.md          # Project documentation (this file)
```

---

## Tasks Breakdown

### 0. **Creating a Simple Templating Program**
- Implement a function to generate invitation letters using string templating.
- Read a **template file** and populate placeholders with **user data**.
- Handle **missing data, invalid inputs, and empty template files**.
- Generate sequential **output files** with personalized invitations.

### 1. **Creating a Basic HTML Template in Flask**
- Set up a **Flask** project and create a basic web application.
- Use the **render_template()** function to serve an HTML page.
- Structure HTML using:
  - **Header**
  - **Body (Paragraphs, Lists, etc.)**
  - **Footer**
- Implement **template inheritance** to reuse **headers and footers** across multiple pages.

### 2. **Creating a Dynamic Template with Loops and Conditions in Flask**
- Use **Jinja’s templating engine** to generate HTML dynamically.
- Read a **list of items from a JSON file** and display them on the page.
- Implement **loops (`{% for %}`) and conditions (`{% if %}`)** in Jinja.
- Display a **fallback message** when no data is available.

### 3. **Displaying Data from JSON or CSV Files in Flask**
- Read product data from **both JSON and CSV files**.
- Implement **Flask routes** that accept a **query parameter (`?source=json/csv`)** to determine the data source.
- Display product information using **dynamic tables**.
- Implement **error handling** for:
  - Invalid source (e.g., `?source=xml` should return an error).
  - Non-existing product IDs (`?id=10` when product 10 does not exist).

### 4. **Extending Dynamic Data Display to Include SQLite in Flask**
- Integrate a **SQLite database (`products.db`)** to fetch and display product data.
- Extend the existing Flask route to handle `?source=sql`.
- Store product details in a **Products table**.
- Implement **database interactions** using Python’s `sqlite3` module.
- Maintain a single **HTML template** for all data sources (`JSON, CSV, SQLite`).

---

## How to Run the Project

### **Setup Environment**
Ensure you have Python installed (preferably **Python 3.8+**).

1. **Clone the repository**
   ```sh
   git clone https://github.com/holbertonschool-higher_level_programming
   cd holbertonschool-higher_level_programming/python-server_side_rendering
   ```

2. **Install dependencies**
   ```sh
   pip install Flask
   ```

3. **Run each task**
   - **Task 1 (Basic Flask Template)**:
     ```sh
     python3 task_01_jinja.py
     ```
     Open your browser and go to **`http://localhost:5000/`**.

   - **Task 2 (Dynamic Templates with JSON)**:
     ```sh
     python3 task_02_logic.py
     ```
     Access **`http://localhost:5000/items`**.

   - **Task 3 (JSON & CSV Display)**:
     ```sh
     python3 task_03_files.py
     ```
     Try different URLs:
     ```
     http://localhost:5000/products?source=json
     http://localhost:5000/products?source=csv
     ```

   - **Task 4 (SQLite Integration)**:
     - First, create the database:
       ```sh
       python3 task_04_db.py
       ```
     - Then run the Flask server:
       ```sh
       python3 task_04_db.py
       ```
     - Access:
       ```
       http://localhost:5000/products?source=sql
       ```

---

## Key Concepts Covered
✅ **Flask**: A lightweight Python web framework.  
✅ **Jinja2**: A powerful templating engine for HTML generation.  
✅ **JSON & CSV Handling**: Parsing and reading structured data.  
✅ **SQLite Integration**: Storing and querying data using SQL.  
✅ **SSR vs CSR**: Learning the advantages of server-side rendering.  

---

## Additional Resources
- 🔹 Flask Documentation: [Flask Official Docs](https://flask.palletsprojects.com/en/latest/)
- 🔹 Jinja2 Documentation: [Jinja Official Docs](https://jinja.palletsprojects.com/en/latest/)
- 🔹 SQLite3 in Python: [SQLite Docs](https://docs.python.org/3/library/sqlite3.html)
- 🔹 JSON & CSV Handling: [Python JSON](https://docs.python.org/3/library/json.html) | [Python CSV](https://docs.python.org/3/library/csv.html)

---

## Author
This project is part of **Holberton School's Higher-Level Programming curriculum**  
📌 **Project Author**: Javier Valenzani  
📌 **Contributor**: Rayane

This project aims to build a **solid foundation** in **Python web development** using **Flask, Jinja, and SQL** to create **efficient, scalable, and SEO-friendly applications**. 🚀