# Queues: First In, First Out (FIFO)

A queue is a linear data structure where elements are added at the back and removed from the front.

## Analogy
Think of a line of people waiting for a bus. The first person in the line is the first person to get on.

## Core Operations

1. **Enqueue**: Add an element to the back. `O(1)`
2. **Dequeue**: Remove an element from the front. `O(1)`
3. **Front/Peek**: Get the front element. `O(1)`
4. **Rear**: Get the last element. `O(1)`

## Python Implementation
While you can use `list.pop(0)`, it is **inefficient** (`O(n)`) because it has to shift all other items. Use `collections.deque` for `O(1)` performance.

```python
from collections import deque
queue = deque()
queue.append(1) # Enqueue
queue.append(2)
first = queue.popleft() # Dequeue -> returns 1
```

## Types of Queues

1. **Simple Queue**: Basic back-to-front queue.
2. **Circular Queue**: The last position is connected back to the first.
3. **Priority Queue**: Elements have a priority; higher priority items are dequeued first.
4. **Double-Ended Queue (Deque)**: Supports insertion and deletion at both ends.

## Real-world Applications

1. **Task Scheduling**: Managing print jobs or CPU tasks.
2. **Data Buffering**: Handling asynchronous data (like video streaming).
3. **Broadcasting**: Sending messages to multiple users in order.
4. **BFS (Breadth First Search)**: A primary algorithm for exploring graphs layer by layer.

## 🧠 Interview Corner

### Common Questions
1. **Can you explain the trade-offs of using Queues?**
   - *Answer*: Focus on time vs space complexity and the specific use-case suitability.
2. **How does Queues compare to other structures in its class?**
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

## 🚀 Multi-Implementation Mastery: Queues: Queues

### Way 1: Using `collections.deque.popleft()`
```python
from collections import deque; q = deque(); q.append(1); q.popleft()
```

### Way 2: Using `queue.Queue` (Thread-safe)
```python
from queue import Queue; q = Queue(); q.put(1); q.get()
```


### Way 3: Priority Queue with `heapq`
```python
import heapq
q = []; heapq.heappush(q, (priority, val))
# Standard way to implement task queues
```

### Way 4: Circular Buffer Queue (using fixed-size list)
```python
q = [None]*size; head = tail = 0
def enqueue(x): q[tail] = x; tail = (tail + 1) % size
```

## 🌍 Real-World Use Case
**Scenario**: Message brokers and print job scheduling.
*Why it matters*: Choosing the right implementation balances cognitive load with technical performance.

