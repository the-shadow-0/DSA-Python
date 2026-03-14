# Introduction to REST APIs

An API (Application Programming Interface) is a set of definitions and protocols for building and integrating application software. REST (Representational State Transfer) is the most widely used architectural style for web-based APIs.

## The Core Concept: Resources
In REST, everything is a **Resource** (e.g., a "User", a "Post", or a "Message"). Each resource is identified by a unique URL (Uniform Resource Locator).

## HTTP Methods: The "Verbs"
We interact with resources using standard HTTP verbs:

| Method | Goal | Success Code |
|---|---|---|
| **GET** | Retrieve a resource. | 200 OK |
| **POST** | Create a new resource. | 201 Created |
| **PUT** | Replace an entire resource. | 200/204 |
| **PATCH** | Update part of a resource. | 200/204 |
| **DELETE** | Remove a resource. | 200/204 |

## Statelessness
One of the key constraints of REST is that it is **Stateless**. This means each request from a client to a server must contain all the information necessary to understand and process the request. The server does not store any "session" information about the client.

## JSON (JavaScript Object Notation)
JSON is the standard format for sending data between the client and the server. It is lightweight, text-based, and language-independent.

### Example JSON Payload:
```json
{
  "id": 42,
  "title": "Learning FastAPI",
  "tags": ["python", "web", "api"],
  "author": {
    "name": "Jane Doe",
    "verified": true
  }
}
```

## HTTP Status Codes
Servers communicate the result of a request using 3-digit status codes:
- **2xx (Success)**: Everything worked.
- **3xx (Redirection)**: The resource moved.
- **4xx (Client Error)**: You sent a bad request (e.g., 404 Not Found, 401 Unauthorized).
- **5xx (Server Error)**: The server crashed while processing.

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Intro To Apis?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Intro To Apis compare to other structures in its class?**
   - *Answer*: Contrast with related topics (e.g., Arrays vs Linked Lists).

### Thought Process
- **Understand the Constraints**: Ask about the size of input and memory limits.
- **Base Cases**: Always define the simplest form of the problem first.
- **Optimal Strategy**: Mention why the chosen approach is the most efficient.

## 📋 Cheat Sheet

| Metric | Complexity |
|---|---|
| Average Case | O(1) - O(n log n) |
| Worst Case | See specific analysis above |
| Space Used | Auxiliary space details |

## ⚠️ Common Pitfalls

- **Off-by-one Errors**: The most common mistake in indexing.
- **Memory Leaks**: Forgetting to clean up pointers in low-level implementations.
- **Infinite Recursion**: Missing or incorrect base cases.


## 🚀 Multi-Implementation Mastery: API Paradigms

### Way 3: Flask-style simple API
```python
from flask import Flask; app = Flask(__name__)
@app.route('/') def hello(): return 'Hello'
```

### Way 4: Node.js Express style (Conceptual Python equivalent)
```python
# Python logic mirroring Express.js middlewares
def use(middleware): chain.append(middleware)
```
