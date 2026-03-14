"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

interface Topic {
  slug: string;
  title: string;
  description: string;
}

interface Module {
  id: string;
  title: string;
  icon: string;
  level: number;
  topics: Topic[];
}

const LEVEL_COLORS: Record<number, string> = {
  1: "#10b981",
  2: "#f59e0b",
  3: "#ef4444",
};

const LEVEL_LABELS: Record<number, string> = {
  1: "Beginner",
  2: "Intermediate",
  3: "Advanced",
};

export default function LearnPage() {
  const [modules, setModules] = useState<Module[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/api/curriculum")
      .then((res) => res.json())
      .then((data) => {
        setModules(data.modules);
        setLoading(false);
      })
      .catch(() => {
        // Fallback static data
        setModules([
          {
            id: "python-course", title: "Python: Zero to Hero", icon: "🐍", level: 1,
            topics: [
              { slug: "python-basics", title: "Variables & Data Types", description: "Strings, ints, floats, booleans, and type casting" },
              { slug: "python-control-flow", title: "Control Flow", description: "If/else statements, for loops, and while loops" },
              { slug: "python-functions", title: "Functions & Scope", description: "Defining functions, arguments, return values, and variable scope" },
              { slug: "python-oop", title: "Object-Oriented Programming", description: "Classes, objects, inheritance, and encapsulation" },
              { slug: "python-advanced", title: "Advanced Python", description: "List comprehensions, generators, decorators, and context managers" },
            ],
          },
          {
            id: "foundations", title: "Foundations", icon: "📐", level: 2,
            topics: [
              { slug: "big-o-notation", title: "Big O Notation", description: "Understand algorithm efficiency" },
              { slug: "time-complexity", title: "Time Complexity", description: "Analyze runtime scaling" },
              { slug: "space-complexity", title: "Space Complexity", description: "Analyze memory usage" },
            ],
          },
          {
            id: "data-structures", title: "Data Structures", icon: "🏗️", level: 2,
            topics: [
              { slug: "arrays", title: "Arrays", description: "Contiguous memory, O(1) access" },
              { slug: "linked-lists", title: "Linked Lists", description: "Node-based sequential data" },
              { slug: "stacks", title: "Stacks", description: "LIFO — Last In, First Out" },
              { slug: "queues", title: "Queues", description: "FIFO — First In, First Out" },
              { slug: "hash-tables", title: "Hash Tables", description: "O(1) key-value lookup" },
              { slug: "trees", title: "Trees & BST", description: "Hierarchical data structures" },
              { slug: "heaps", title: "Heaps", description: "Priority-based tree structure" },
              { slug: "graphs", title: "Graphs", description: "Vertices and edges" },
            ],
          },
          {
            id: "algorithms", title: "Algorithms", icon: "⚡", level: 3,
            topics: [
              { slug: "searching", title: "Searching", description: "Linear & binary search" },
              { slug: "sorting", title: "Sorting", description: "Bubble, merge, quick sort" },
              { slug: "recursion", title: "Recursion", description: "Self-calling functions" },
              { slug: "dynamic-programming", title: "Dynamic Programming", description: "Optimal substructure" },
              { slug: "graph-algorithms", title: "Graph Algorithms", description: "BFS, DFS, Dijkstra" },
            ],
          },
          {
            id: "advanced", title: "Advanced Topics", icon: "🚀", level: 4,
            topics: [
              { slug: "tries", title: "Tries", description: "Prefix trees" },
              { slug: "segment-trees", title: "Segment Trees", description: "Range queries" },
              { slug: "union-find", title: "Union-Find", description: "Disjoint sets" },
            ],
          },
          {
            id: "fastapi-course", title: "FastAPI Course", icon: "⚡", level: 4,
            topics: [
              { slug: "intro-to-apis", title: "Introduction to APIs", description: "What are REST APIs? JSON & HTTP" },
              { slug: "fastapi-basics", title: "FastAPI Basics", description: "Hello World and Uvicorn" },
              { slug: "routing-parameters", title: "Routing & Parameters", description: "Path and query parameters" },
              { slug: "pydantic-models", title: "Pydantic Models", description: "Data validation and POST bodies" },
              { slug: "dependency-injection", title: "Dependency Injection", description: "Reusable logic and DB sessions" },
            ],
          },
        ]);
        setLoading(false);
      });
  }, []);

  return (
    <div style={{ maxWidth: "1280px", margin: "0 auto", padding: "3rem 1.5rem" }}>
      {/* Header */}
      <div className="animate-fade-in-up" style={{ marginBottom: "3rem" }}>
        <h1 style={{ fontSize: "2.5rem", fontWeight: 900, marginBottom: "0.75rem" }}>
          📚 Learning <span className="gradient-text">Curriculum</span>
        </h1>
        <p style={{ color: "var(--text-secondary)", fontSize: "1.1rem", maxWidth: "600px" }}>
          A structured path from fundamentals to advanced algorithms.
          Each topic includes visual explanations, Python code, and practice problems.
        </p>
      </div>

      {/* Modules */}
      {loading ? (
        <div style={{ textAlign: "center", padding: "4rem", color: "var(--text-muted)" }}>
          <div className="animate-shimmer" style={{ width: "300px", height: "20px", borderRadius: "8px", margin: "0 auto 1rem" }} />
          <p>Loading curriculum...</p>
        </div>
      ) : (
        modules.map((mod, mi) => (
          <div key={mod.id} className={`animate-fade-in-up stagger-${mi + 1}`} style={{ marginBottom: "3rem" }}>
            {/* Module Header */}
            <div style={{
              display: "flex",
              alignItems: "center",
              gap: "1rem",
              marginBottom: "1.25rem",
            }}>
              <span style={{ fontSize: "2rem" }}>{mod.icon}</span>
              <div>
                <h2 style={{ fontSize: "1.5rem", fontWeight: 800 }}>{mod.title}</h2>
                <span style={{
                  fontSize: "0.75rem",
                  fontWeight: 600,
                  color: LEVEL_COLORS[mod.level],
                  textTransform: "uppercase",
                  letterSpacing: "0.05em",
                }}>
                  {LEVEL_LABELS[mod.level]} • {mod.topics.length} topics
                </span>
              </div>
            </div>

            {/* Topics Grid */}
            <div style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fill, minmax(280px, 1fr))",
              gap: "1rem",
            }}>
              {mod.topics.map((topic) => (
                <Link
                  key={topic.slug}
                  href={`/learn/${topic.slug}`}
                  className="glass-card"
                  style={{
                    padding: "1.5rem",
                    textDecoration: "none",
                    display: "flex",
                    flexDirection: "column",
                    gap: "0.5rem",
                    position: "relative",
                    overflow: "hidden",
                    transition: "all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)"
                  }}
                  onMouseEnter={(e) => {
                    e.currentTarget.style.transform = 'translateY(-5px) scale(1.02)';
                    e.currentTarget.style.boxShadow = `0 8px 25px ${LEVEL_COLORS[mod.level]}30`;
                    e.currentTarget.style.borderColor = `${LEVEL_COLORS[mod.level]}50`;
                  }}
                  onMouseLeave={(e) => {
                    e.currentTarget.style.transform = 'translateY(0) scale(1)';
                    e.currentTarget.style.boxShadow = 'var(--glow-primary)';
                    e.currentTarget.style.borderColor = 'var(--border-subtle)';
                  }}
                >
                  <div style={{ position: 'absolute', top: 0, left: 0, right: 0, height: '3px', background: LEVEL_COLORS[mod.level], opacity: 0.7 }} />
                  <h3 style={{
                    fontSize: "1.1rem",
                    fontWeight: 800,
                    color: "var(--text-primary)",
                  }}>
                    {topic.title}
                  </h3>
                  <p style={{
                    fontSize: "0.85rem",
                    color: "var(--text-secondary)",
                    lineHeight: 1.5,
                  }}>
                    {topic.description}
                  </p>
                  <span style={{
                    fontSize: "0.8rem",
                    color: LEVEL_COLORS[mod.level],
                    fontWeight: 500,
                    marginTop: "auto",
                  }}>
                    Start learning →
                  </span>
                </Link>
              ))}
            </div>
          </div>
        ))
      )}
    </div>
  );
}
