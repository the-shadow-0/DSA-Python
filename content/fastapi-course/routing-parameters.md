# Routing and Parameters

Routing identifies which function should handle a specific incoming URL request. Parameters allow you to pass dynamic data into those functions.

## 1. Path Parameters
Path parameters are part of the URL path itself. They are defined using curly braces `{}`.

```python
@app.get("/users/{user_id}")
def get_user(user_id: int): # Automatically converted to int!
    return {"user_id": user_id}
```

### Path Validation
You can add extra constraints using the `Path` class:

```python
from fastapi import Path

@app.get("/items/{item_id}")
def read_item(item_id: int = Path(..., title="The ID", ge=1)):
    return {"item_id": item_id}
```
In this example, `item_id` **must** be greater than or equal to 1.

## 2. Query Parameters
Query parameters are key-value pairs that come after the `?` in the URL.

```python
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}]

@app.get("/items/")
def read_items(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]
```
If you visit `/items/?skip=1&limit=5`, FastAPI automatically extracts those values.

## 3. Request Header Parameters
You can also extract information from the HTTP headers, such as user-agents or auth tokens.

```python
from fastapi import Header

@app.get("/info/")
def get_info(user_agent: str | None = Header(default=None)):
    return {"User-Agent": user_agent}
```

## 4. Path vs Query
- Use **Path** parameters to identify a specific resource (e.g., `/users/123`).
- Use **Query** parameters to filter or sort resources (e.g., `/users?sort=asc`).

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Routing Parameters?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Routing Parameters compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Routing: Routing

### Way 1: Path Parameters
```python
@app.get('/items/{id}')
```

### Way 2: Query Parameters
```python
@app.get('/items/') def read(skip: int = 0, limit: int =10):
```


### Way 3: Header-based routing
```python
@app.get('/') def read(x_token: str = Header()): ...
```

### Way 4: Dynamic Regex Routing (Lower-level)
```python
# Python implementation of regex-based path matching
import re; match = re.match(r'/users/(\d+)', path)
```

## 🌍 Real-World Use Case
**Scenario**: Building RESTful search and filtering interfaces.
*Why it matters*: Practical engineering requires a deep understanding of these trade-offs to build resilient systems.

