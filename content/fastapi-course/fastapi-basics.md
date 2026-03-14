# FastAPI: The Modern Python Framework

FastAPI is a high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Key Features
1. **Speed**: It is one of the fastest Python frameworks available (comparable to Go and Node.js).
2. **Fast to code**: Increase the speed to develop features by about 200% to 300%.
3. **Fewer bugs**: Reduce about 40% of human (developer) induced errors.
4. **Intuitive**: Great editor support (autocompletion everywhere).
5. **Standards-based**: Based on OpenAPI (previously known as Swagger) and JSON Schema.

## Installation
Typically installed alongside an ASGI server like Uvicorn:
`pip install fastapi uvicorn`

## Creating Your First App
The simplest FastAPI app consists of an instance and a route.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}
```

## Why the `async` keyword?
FastAPI is built on top of `Starlette`, which supports `asyncio`. If your code interacts with a database or slow external API, using `async def` allows Python to handle other requests while waiting, significantly improving performance.

```python
@app.get("/items")
async def get_items():
    items = await database.fetch_all()
    return items
```

## Interactive API Docs (The Killer Feature)
Once you run your app, FastAPI automatically generates two sets of interactive documentation:
- **/docs**: The most popular one (Swagger UI), allowing you to call your API directly from the browser.
- **/redoc**: A cleaner, alternative documentation style.

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Fastapi Basics?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Fastapi Basics compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Endpoints: Endpoints

### Way 1: Synchronous Def
```python
@app.get('/')
def read_root():
    return {'msg': 'Hello'}
```

### Way 2: Asynchronous Async Def
```python
@app.get('/')
async def read_root():
    return {'msg': 'Hello'}
```


### Way 3: Streaming Response (Large files)
```python
from fastapi.responses import StreamingResponse
def iter_file(): yield from file
@app.get('/') def stream(): return StreamingResponse(iter_file())
```

### Way 4: WebSocket Implementation
```python
@app.websocket('/ws')
async def ws(websocket: WebSocket):
    await websocket.accept(); await websocket.send_text('Hello')
```

## 🌍 Real-World Use Case
**Scenario**: High-throughput API microservices.
*Why it matters*: Real-world systems prioritize either maintenance simplicity or raw execution speed depending on scale.

