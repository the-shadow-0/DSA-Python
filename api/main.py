"""
DSA Python — FastAPI Backend 
==============================

Provides endpoints for:
    - Curriculum content
    - Challenge listing and evaluation
    - Code execution in a sandboxed environment
    - User progress tracking
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Any
import json
import os
import subprocess
import tempfile
import sys

app = FastAPI(
    title="DSA Python API",
    description="Backend API for the DSA Python learning platform",
    version="1.0.0",
)

# CORS — allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ──────────────────────────────────────────────
# Paths
# ──────────────────────────────────────────────
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
CHALLENGES_DIR = os.path.join(PROJECT_ROOT, "challenges", "definitions")
CONTENT_DIR = os.path.join(PROJECT_ROOT, "content")

# ──────────────────────────────────────────────
# Models
# ──────────────────────────────────────────────

class CodeExecutionRequest(BaseModel):
    code: str
    timeout: int = 5

class CodeExecutionResponse(BaseModel):
    stdout: str
    stderr: str
    success: bool
    execution_time_ms: float

class ChallengeEvalRequest(BaseModel):
    challenge_id: str
    code: str

class TestResult(BaseModel):
    input: Any
    expected: Any
    actual: Any
    passed: bool

class ChallengeEvalResponse(BaseModel):
    passed: bool
    total_tests: int
    passed_tests: int
    results: List[TestResult]
    error: Optional[str] = None

class ProgressUpdate(BaseModel):
    topic_slug: str
    status: str  # "not_started", "in_progress", "completed"

# ──────────────────────────────────────────────
# Curriculum data
# ──────────────────────────────────────────────

CURRICULUM = [
    {
        "id": "python-course",
        "title": "Python: Zero to Hero",
        "icon": "🐍",
        "level": 1,
        "topics": [
            {"slug": "python-basics", "title": "Variables & Data Types", "description": "Strings, ints, floats, booleans, and type casting"},
            {"slug": "python-control-flow", "title": "Control Flow", "description": "If/else statements, for loops, and while loops"},
            {"slug": "python-functions", "title": "Functions & Scope", "description": "Defining functions, arguments, return values, and variable scope"},
            {"slug": "python-oop", "title": "Object-Oriented Programming", "description": "Classes, objects, inheritance, and encapsulation"},
            {"slug": "python-advanced", "title": "Advanced Python", "description": "List comprehensions, generators, decorators, and context managers"},
        ]
    },
    {
        "id": "foundations",
        "title": "Foundations",
        "icon": "📐",
        "level": 2,
        "topics": [
            {"slug": "big-o-notation", "title": "Big O Notation", "description": "Understand algorithm efficiency and growth rates"},
            {"slug": "time-complexity", "title": "Time Complexity", "description": "Analyze how runtime scales with input size"},
            {"slug": "space-complexity", "title": "Space Complexity", "description": "Analyze memory usage of algorithms"},
        ]
    },
    {
        "id": "data-structures",
        "title": "Data Structures",
        "icon": "🏗️",
        "level": 2,
        "topics": [
            {"slug": "arrays", "title": "Arrays", "description": "Contiguous memory, O(1) access"},
            {"slug": "linked-lists", "title": "Linked Lists", "description": "Node-based sequential data"},
            {"slug": "stacks", "title": "Stacks", "description": "LIFO — Last In, First Out"},
            {"slug": "queues", "title": "Queues", "description": "FIFO — First In, First Out"},
            {"slug": "hash-tables", "title": "Hash Tables", "description": "Key-value storage with O(1) lookup"},
            {"slug": "trees", "title": "Trees & BST", "description": "Hierarchical data with efficient operations"},
            {"slug": "heaps", "title": "Heaps", "description": "Priority-based tree structure"},
            {"slug": "graphs", "title": "Graphs", "description": "Vertices and edges — model relationships"},
        ]
    },
    {
        "id": "algorithms",
        "title": "Algorithms",
        "icon": "⚡",
        "level": 3,
        "topics": [
            {"slug": "searching", "title": "Searching Algorithms", "description": "Linear search, binary search"},
            {"slug": "sorting", "title": "Sorting Algorithms", "description": "Bubble, selection, merge, quick sort"},
            {"slug": "recursion", "title": "Recursion", "description": "Functions that call themselves"},
            {"slug": "divide-and-conquer", "title": "Divide & Conquer", "description": "Break problems into smaller subproblems"},
            {"slug": "greedy", "title": "Greedy Algorithms", "description": "Make locally optimal choices"},
            {"slug": "dynamic-programming", "title": "Dynamic Programming", "description": "Optimize by storing subproblem results"},
            {"slug": "graph-algorithms", "title": "Graph Algorithms", "description": "BFS, DFS, Dijkstra, topological sort"},
        ]
    },
    {
        "id": "advanced",
        "title": "Advanced Topics",
        "icon": "🚀",
        "level": 4,
        "topics": [
            {"slug": "tries", "title": "Tries", "description": "Prefix trees for string operations"},
            {"slug": "segment-trees", "title": "Segment Trees", "description": "Efficient range queries"},
            {"slug": "union-find", "title": "Union-Find", "description": "Disjoint set operations"},
        ]
    },
    {
        "id": "fastapi-course",
        "title": "FastAPI Course",
        "icon": "⚡",
        "level": 4,
        "topics": [
            {"slug": "intro-to-apis", "title": "Introduction to APIs", "description": "What are REST APIs? JSON & HTTP"},
            {"slug": "fastapi-basics", "title": "FastAPI Basics", "description": "Hello World and Uvicorn"},
            {"slug": "routing-parameters", "title": "Routing & Parameters", "description": "Path and query parameters"},
            {"slug": "pydantic-models", "title": "Pydantic Models", "description": "Data validation and POST bodies"},
            {"slug": "dependency-injection", "title": "Dependency Injection", "description": "Reusable logic and DB sessions"},
        ]
    },
]


# ──────────────────────────────────────────────
# Routes — Curriculum
# ──────────────────────────────────────────────

@app.get("/")
async def root():
    return {"message": "DSA Python API", "version": "1.0.0"}


@app.get("/api/curriculum")
async def get_curriculum():
    """Return the full curriculum structure."""
    return {"modules": CURRICULUM}


@app.get("/api/topics/{slug}")
async def get_topic(slug: str):
    """Return content for a specific topic."""
    # Try to load markdown content
    content_path = None
    for module in CURRICULUM:
        for topic in module["topics"]:
            if topic["slug"] == slug:
                # Find the content file
                for dirpath, dirs, files in os.walk(CONTENT_DIR):
                    for f in files:
                        if f == f"{slug}.md":
                            content_path = os.path.join(dirpath, f)
                            break

                content = ""
                if content_path and os.path.exists(content_path):
                    with open(content_path, "r") as f:
                        content = f.read()

                return {
                    **topic,
                    "module": module["title"],
                    "content": content,
                }

    raise HTTPException(status_code=404, detail=f"Topic '{slug}' not found")


# ──────────────────────────────────────────────
# Routes — Challenges
# ──────────────────────────────────────────────

@app.get("/api/challenges")
async def list_challenges(difficulty: Optional[str] = None,
                          category: Optional[str] = None):
    """List all challenges, optionally filtered."""
    challenges = []

    if os.path.exists(CHALLENGES_DIR):
        for filename in sorted(os.listdir(CHALLENGES_DIR)):
            if filename.endswith(".json"):
                filepath = os.path.join(CHALLENGES_DIR, filename)
                with open(filepath, "r") as f:
                    challenge = json.load(f)

                # Apply filters
                if difficulty and challenge.get("difficulty") != difficulty:
                    continue
                if category and challenge.get("category") != category:
                    continue

                # Don't expose solution in listing
                challenge_summary = {
                    "id": challenge["id"],
                    "title": challenge["title"],
                    "difficulty": challenge["difficulty"],
                    "category": challenge["category"],
                    "description": challenge["description"][:200] + "...",
                }
                challenges.append(challenge_summary)

    return {"challenges": challenges, "total": len(challenges)}


@app.get("/api/challenges/{challenge_id}")
async def get_challenge(challenge_id: str):
    """Get a specific challenge (without solution)."""
    filepath = os.path.join(CHALLENGES_DIR, f"{challenge_id}.json")

    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Challenge not found")

    with open(filepath, "r") as f:
        challenge = json.load(f)

    # Don't expose solution
    return {
        "id": challenge["id"],
        "title": challenge["title"],
        "difficulty": challenge["difficulty"],
        "category": challenge["category"],
        "description": challenge["description"],
        "starter_code": challenge["starter_code"],
        "hints": challenge["hints"],
        "time_complexity": challenge.get("time_complexity"),
        "space_complexity": challenge.get("space_complexity"),
        "related_topic": challenge.get("related_topic"),
        "num_tests": len(challenge["test_cases"]),
    }


# ──────────────────────────────────────────────
# Routes — Code Execution
# ──────────────────────────────────────────────

@app.post("/api/execute", response_model=CodeExecutionResponse)
async def execute_code(request: CodeExecutionRequest):
    """
    Execute Python code in a sandboxed subprocess.

    Security measures:
        - 5 second timeout
        - No network access
        - Restricted imports
    """
    # Basic import restrictions
    forbidden_imports = ["os", "sys", "subprocess", "shutil", "socket",
                         "http", "urllib", "requests", "importlib"]

    for forbidden in forbidden_imports:
        if f"import {forbidden}" in request.code or f"from {forbidden}" in request.code:
            return CodeExecutionResponse(
                stdout="",
                stderr=f"Security Error: import '{forbidden}' is not allowed.",
                success=False,
                execution_time_ms=0,
            )

    # Write code to temp file and execute
    import time
    start = time.perf_counter()

    try:
        with tempfile.NamedTemporaryFile(mode='w', suffix='.py',
                                          delete=False) as tmp:
            tmp.write(request.code)
            tmp_path = tmp.name

        result = subprocess.run(
            [sys.executable, tmp_path],
            capture_output=True,
            text=True,
            timeout=min(request.timeout, 10),
        )

        elapsed = (time.perf_counter() - start) * 1000

        return CodeExecutionResponse(
            stdout=result.stdout[:10000],  # Limit output
            stderr=result.stderr[:5000],
            success=result.returncode == 0,
            execution_time_ms=round(elapsed, 2),
        )

    except subprocess.TimeoutExpired:
        elapsed = (time.perf_counter() - start) * 1000
        return CodeExecutionResponse(
            stdout="",
            stderr="Error: Code execution timed out (5s limit).",
            success=False,
            execution_time_ms=round(elapsed, 2),
        )
    finally:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass


# ──────────────────────────────────────────────
# Routes — Challenge Evaluation
# ──────────────────────────────────────────────

@app.post("/api/evaluate", response_model=ChallengeEvalResponse)
async def evaluate_challenge(request: ChallengeEvalRequest):
    """
    Grade a user's solution against test cases.
    """
    filepath = os.path.join(CHALLENGES_DIR, f"{request.challenge_id}.json")

    if not os.path.exists(filepath):
        raise HTTPException(status_code=404, detail="Challenge not found")

    with open(filepath, "r") as f:
        challenge = json.load(f)

    test_cases = challenge["test_cases"]
    results = []

    for tc in test_cases:
        # Build test script
        test_code = request.code + "\n\n"

        if "test_setup" in challenge:
            test_code += challenge["test_setup"] + "\n\n"

        if "test_caller" in challenge:
            # Pass dictionary representation to format as kwargs
            args = repr(tc["input"])
            test_code += f"result = {challenge['test_caller'].format(args)}\n"
        else:
            # Call the function with test input
            func_name = challenge["starter_code"].split("(")[0].replace("def ", "").strip()
            args = ", ".join(repr(v) for v in tc["input"].values())
            test_code += f"result = {func_name}({args})\n"

        test_code += f"print('__RESULT_START__' + repr(result) + '__RESULT_END__')\n"

        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py',
                                              delete=False) as tmp:
                tmp.write(test_code)
                tmp_path = tmp.name

            proc = subprocess.run(
                [sys.executable, tmp_path],
                capture_output=True,
                text=True,
                timeout=5,
            )

            if proc.returncode != 0:
                results.append(TestResult(
                    input=tc["input"],
                    expected=tc["expected"],
                    actual=proc.stderr[:1000],
                    passed=False,
                ))
            else:
                stdout = proc.stdout
                if '__RESULT_START__' in stdout and '__RESULT_END__' in stdout:
                    actual_raw = stdout.split('__RESULT_START__')[1].split('__RESULT_END__')[0].strip()
                    try:
                        actual_val = eval(actual_raw)
                    except Exception:
                        actual_val = actual_raw
                else:
                    actual_val = stdout.strip()

                passed = actual_val == tc["expected"]
                results.append(TestResult(
                    input=tc["input"],
                    expected=tc["expected"],
                    actual=actual_val,
                    passed=passed,
                ))

        except subprocess.TimeoutExpired:
            results.append(TestResult(
                input=tc["input"],
                expected=tc["expected"],
                actual="Timeout",
                passed=False,
            ))
        finally:
            try:
                os.unlink(tmp_path)
            except Exception:
                pass

    passed_count = sum(1 for r in results if r.passed)

    return ChallengeEvalResponse(
        passed=passed_count == len(test_cases),
        total_tests=len(test_cases),
        passed_tests=passed_count,
        results=results,
    )


# ──────────────────────────────────────────────
# Progress (in-memory store for MVP)
# ──────────────────────────────────────────────

progress_store = {}

@app.get("/api/progress")
async def get_progress():
    """Get user progress data."""
    return {"progress": progress_store}


@app.post("/api/progress")
async def update_progress(update: ProgressUpdate):
    """Save user progress."""
    progress_store[update.topic_slug] = update.status
    return {"status": "saved", "progress": progress_store}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
