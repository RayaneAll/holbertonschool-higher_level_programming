# **Project: RESTful API**

## **Project Description**
This project explores the fundamental concepts of RESTful APIs, a key element in modern web service development. RESTful APIs enable efficient communication between systems using principles such as scalability, statelessness, and caching. The project covers various aspects, from consuming APIs to developing them, including security and documentation.

---

## **Learning Objectives**
1. **HTTP/HTTPS**: Understand the basics of HTTP and HTTPS protocols, including methods and status codes.
2. **API Consumption**:
   - Use command-line tools like `curl` to interact with APIs.
   - Use Python to consume and manipulate API data.
3. **API Development**:
   - Create a simple API using Python's `http.server` module.
   - Develop a more advanced API using the Flask framework.
4. **API Security**:
   - Implement basic authentication and token-based authentication (JWT).
   - Understand the concepts of authentication and authorization.
5. **API Documentation**:
   - Use OpenAPI to standardize and document APIs.

---

## **Importance of RESTful APIs**
RESTful APIs play a central role in integrating systems and applications. They enable various services to communicate with each other, whether to share data, trigger actions, or automate processes. This project will help you master the skills needed to consume, develop, secure, and document APIs.

---

## **Project Tasks**

### **0. Basics of HTTP/HTTPS**
- **Objective**: Differentiate between HTTP and HTTPS, understand the structure of HTTP requests/responses, and know common methods and status codes.
- **Resources**:
  - [MDN - An Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
  - [Difference between HTTP and HTTPS](https://www.cloudflare.com/learning/ssl/why-is-http-not-secure/)
  - [List of HTTP Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- **Expected Output**:
  - Summary of differences between HTTP and HTTPS.
  - Structure of an HTTP request/response.
  - List of HTTP methods (GET, POST, etc.) and status codes (200, 404, etc.).

---

### **1. Consume Data from an API Using Command Line Tools (curl)**
- **Objective**: Use `curl` to interact with APIs, set headers, and inspect responses.
- **Resources**:
  - [Everything curl](https://curl.se/docs/)
  - [Public API: JSONPlaceholder](https://jsonplaceholder.typicode.com/)
- **Expected Output**:
  - Retrieve posts using `curl`.
  - Make a POST request to simulate creating a post.

---

### **2. Consuming and Processing Data from an API Using Python**
- **Objective**: Use the `requests` library to interact with an API, parse JSON data, and convert it to CSV.
- **Resources**:
  - [Python Requests Library](https://docs.python-requests.org/)
  - [Working with JSON Data in Python](https://docs.python.org/3/library/json.html)
- **Expected Output**:
  - A Python script that fetches and displays posts.
  - A script that saves the data to a CSV file.

---

### **3. Develop a Simple API Using Python's `http.server` Module**
- **Objective**: Create a basic HTTP server using Python's `http.server` module.
- **Resources**:
  - [Python `http.server` Documentation](https://docs.python.org/3/library/http.server.html)
- **Expected Output**:
  - A server that responds to GET requests with simple messages.
  - An endpoint `/data` that returns JSON data.

---

### **4. Develop a Simple API Using Flask**
- **Objective**: Create a RESTful API with Flask, handle routes, and process POST requests.
- **Resources**:
  - [Flask Documentation](https://flask.palletsprojects.com/)
- **Expected Output**:
  - An API with endpoints to display messages, retrieve JSON data, and add users via POST.

---

### **5. API Security and Authentication Techniques**
- **Objective**: Implement basic authentication and token-based authentication (JWT) to secure an API.
- **Resources**:
  - [Flask-HTTPAuth](https://flask-httpauth.readthedocs.io/)
  - [Flask-JWT-Extended](https://flask-jwt-extended.readthedocs.io/)
- **Expected Output**:
  - An API with routes protected by basic authentication and JWT.
  - A role-based system to restrict access to certain routes.

---

## **Project Structure**
- **Directory**: `restful-api`
- **Files**:
  - `task_00_http_https.md`: Documentation on HTTP/HTTPS.
  - `task_01_curl.sh`: Scripts to interact with an API using `curl`.
  - `task_02_requests.py`: Python script to consume an API.
  - `task_03_http_server.py`: Simple HTTP server using `http.server`.
  - `task_04_flask.py`: RESTful API with Flask.
  - `task_05_basic_security.py`: Security implementation with Flask.

---

## **How to Use This Project**
1. Clone the repository:
   ```bash
   git clone https://github.com/holbertonschool-higher_level_programming.git
   ```
2. Navigate to the project directory:
   ```bash
   cd restful-api
   ```
3. Follow the instructions in each file to execute the tasks.

---

## **Additional Resources**
- [OpenAPI Specification](https://swagger.io/specification/)
- [Introduction to REST](https://restfulapi.net/)
- [Python Documentation](https://docs.python.org/3/)

---

## **Author**
- **Javier Valenzani**: Project designer.

---

## **Score**
- **Current Score**: 89.5%
- **Badge**: RESTful API Novice

---

This project will help you master the essential skills for working with RESTful APIs, from consumption to creation and securing. Good luck! 🚀