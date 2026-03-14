<div align="center">

# ⚡ DSA Python

### Master Data Structures & Algorithms — The Visual Way

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)
[![Next.js](https://img.shields.io/badge/Next.js-15-black.svg)](https://nextjs.org)
[![Tests](https://img.shields.io/badge/tests-53%20passing-brightgreen.svg)](#-running-tests)

*An open-source platform that teaches DSA through visual explanations, Python implementations, and interactive coding challenges.*

</div>

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 **Algorithm Visualizer** | Step-by-step animated sorting with play/pause/step controls |
| 🐍 **Python Implementations** | 25+ clean, commented implementations with complexity analysis |
| 🎯 **Interactive Challenges** | Write code, run tests, get instant grading & feedback |
| 📚 **Structured Curriculum** | From Big O basics to advanced graph algorithms |
| 📈 **Progress Dashboard** | Track your learning journey across all topics |
| 🌍 **Real-World Examples** | See how data structures power real systems |

---

## 🏗️ Architecture

```
DSA_python/
├── 🐍 algorithms/          # Python algorithm library
│   ├── foundations/         # Big O, complexity analysis
│   ├── data_structures/     # Arrays, linked lists, trees, graphs...
│   ├── sorting/             # Bubble, selection, merge, quick, heap sort
│   ├── searching/           # Linear search, binary search
│   ├── graph_algorithms/    # BFS, DFS, Dijkstra, topological sort
│   ├── dynamic_programming/ # Fibonacci, knapsack, LCS, coin change
│   ├── advanced/            # Trie, segment tree, union-find
│   └── tests/               # 53 comprehensive tests
├── ⚡ api/                  # FastAPI backend
│   └── main.py              # REST API (execute, evaluate, curriculum)
├── 🎯 challenges/           # Coding challenge definitions
│   └── definitions/         # JSON problem specs with test cases
├── 📖 content/              # Curriculum markdown content
├── 🎨 frontend/             # Next.js + Tailwind CSS
│   └── src/app/
│       ├── page.tsx          # Landing page
│       ├── learn/            # Curriculum explorer & topic viewer
│       ├── challenges/       # Challenge browser & workspace
│       ├── visualizer/       # Sorting algorithm visualizer
│       └── dashboard/        # Progress tracking
├── docker-compose.yml
├── LICENSE
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Node.js 18+
- npm

### 1. Clone & Install

```bash
git clone https://github.com/your-username/DSA_python.git
cd DSA_python

# Install Python dependencies
pip install fastapi uvicorn pytest

# Install frontend dependencies
cd frontend && npm install && cd ..
```

### 2. Start the API

```bash
cd api
uvicorn main:app --reload --port 8000
```

### 3. Start the Frontend

```bash
cd frontend
npm run dev
```

Visit **http://localhost:3000** 🎉

---

## 📚 Curriculum

### 🟢 Level 1 — Beginner
- Big O Notation & Complexity Analysis
- Arrays & Array Operations
- Linked Lists
- Stacks & Queues
- Hash Tables
- Linear & Binary Search

### 🟡 Level 2 — Intermediate
- Trees & Binary Search Trees
- Heaps & Priority Queues
- Graphs
- Sorting Algorithms (Bubble → Quick Sort)
- Recursion & Divide and Conquer
- Greedy Algorithms
- Dynamic Programming
- Graph Algorithms (BFS, DFS, Dijkstra)

### 🔴 Level 3 — Advanced
- Tries (Prefix Trees)
- Segment Trees
- Union-Find (Disjoint Sets)
- Algorithm Optimization Techniques

---

## 🧪 Running Tests

```bash
# Run all 53 algorithm tests
python -m pytest algorithms/tests/ -v

# Run specific test suites
python -m pytest algorithms/tests/test_sorting.py -v
python -m pytest algorithms/tests/test_data_structures.py -v
python -m pytest algorithms/tests/test_graph_algorithms.py -v
python -m pytest algorithms/tests/test_dynamic_programming.py -v
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/curriculum` | List all learning modules |
| `GET` | `/api/topics/{slug}` | Get topic content |
| `GET` | `/api/challenges` | List challenges (filter by difficulty) |
| `GET` | `/api/challenges/{id}` | Get challenge details |
| `POST` | `/api/execute` | Execute Python code |
| `POST` | `/api/evaluate` | Grade challenge submission |
| `GET` | `/api/progress` | Get user progress |
| `POST` | `/api/progress` | Update progress |

---

## 🎯 Challenges

| Challenge | Difficulty | Category |
|-----------|-----------|----------|
| Two Sum | 🟢 Easy | Arrays / Hash Tables |
| Valid Parentheses | 🟢 Easy | Stacks |
| Reverse Linked List | 🟢 Easy | Linked Lists |
| Merge Sorted Arrays | 🟢 Easy | Arrays |
| Binary Tree Inorder | 🟡 Medium | Trees |

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-algorithm`)
3. Add your implementation with tests
4. Submit a pull request

### Adding a New Algorithm

1. Create a file in the appropriate `algorithms/` subdirectory
2. Include docstrings, step-by-step comments, and a `_traced` version
3. Add tests in `algorithms/tests/`
4. Add curriculum content in `content/`

### Adding a New Challenge

Create a JSON file in `challenges/definitions/` following the schema:
```json
{
  "id": "your_challenge",
  "title": "Your Challenge",
  "difficulty": "easy|medium|hard",
  "category": "arrays|stacks|trees|...",
  "description": "Problem description...",
  "starter_code": "def solve():\n    pass",
  "test_cases": [{"input": {...}, "expected": ...}],
  "hints": ["Hint 1", "Hint 2"],
  "solution": "def solve():\n    ..."
}
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

<div align="center">

**Built with ❤️ for the developer community**

⭐ Star this repo if it helps you learn DSA!

</div>
