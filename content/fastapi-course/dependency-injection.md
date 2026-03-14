# Dependency Injection: Architectural Mastery

FastAPI's `Depends` is a radical approach to software architecture that enables decoupling and testability.

## Dependency Scoping
- **Route Scope**: `Depends` is called once for the route.
- **Global Scope**: Apply an authentication dependency to every single endpoint in `FastAPI(dependencies=[Depends(auth)])`.

## Dependency Resolution
FastAPI builds a "Dependency Graph" before executing the route.
1. It calculates which dependencies depends on other dependencies.
2. It solves them in the correct order.
3. It **caches** results! if `Sub-dep A` is required by two different dependencies in the same request, it is only executed **once**.

## Yielding Dependencies (Context Managers)
This is the standard way to handle Database connections or resources that need cleanup.
```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() # Always closes, even if the route crashes!
```

## Testing with Dependency Overrides
This is the most powerful feature for developers. You can replace a real database dependency with a mock one for your unit tests without changing your application code!

```python
from main import app, get_db

def override_get_db():
    return MockDatabase()

app.dependency_overrides[get_db] = override_get_db
```

## Security Dependencies
FastAPI has built-in support for OAuth2, API Keys, and JWT (JSON Web Tokens) using the dependency system.
`def get_current_user(token: str = Depends(oauth2_scheme)): ...`

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Dependency Injection?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Dependency Injection compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Dependency Injection: Dependency Injection

### Way 1: Functional `Depends`
```python
async def get_db(): ...
```

### Way 2: Class-based `Depends` with state
```python
class Database: def __init__(self, name): self.name = name
```


### Way 3: Annotated Dependencies (Clean code)
```python
from typing import Annotated
def get_db(): ...
@app.get('/') def read(db: Annotated[DB, Depends(get_db)]): ...
```

### Way 4: Sub-dependency Graphs
```python
def sub_dep(p=Depends(parent_dep)): ...
@app.get('/') def final(s=Depends(sub_dep)): ...
```

## 🌍 Real-World Use Case
**Scenario**: Injecting configuration and database clients into API routes.
*Why it matters*: Choosing the right implementation balances cognitive load with technical performance.

