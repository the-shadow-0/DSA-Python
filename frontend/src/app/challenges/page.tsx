"use client";

import Link from "next/link";
import { useEffect, useState } from "react";

interface Challenge {
  id: string;
  title: string;
  difficulty: string;
  category: string;
  description: string;
}

const FALLBACK_CHALLENGES: Challenge[] = [
  { id: "two_sum", title: "Two Sum", difficulty: "easy", category: "arrays", description: "Find two numbers that add up to target using a hash map approach." },
  { id: "reverse_linked_list", title: "Reverse Linked List", difficulty: "easy", category: "linked_lists", description: "Reverse a singly linked list using three pointers." },
  { id: "valid_parentheses", title: "Valid Parentheses", difficulty: "easy", category: "stacks", description: "Check if brackets are properly nested using a stack." },
  { id: "merge_sorted_arrays", title: "Merge Two Sorted Arrays", difficulty: "easy", category: "arrays", description: "Merge two sorted arrays into one using two pointers." },
  { id: "binary_tree_inorder", title: "Binary Tree Inorder Traversal", difficulty: "medium", category: "trees", description: "Return inorder traversal of binary tree nodes." },
];

const DIFFICULTY_ORDER = ["easy", "medium", "hard"];

export default function ChallengesPage() {
  const [challenges, setChallenges] = useState<Challenge[]>([]);
  const [filter, setFilter] = useState<string>("all");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://localhost:8000/api/challenges")
      .then((res) => res.json())
      .then((data) => { setChallenges(data.challenges); setLoading(false); })
      .catch(() => { setChallenges(FALLBACK_CHALLENGES); setLoading(false); });
  }, []);

  const filtered = filter === "all" ? challenges : challenges.filter((c) => c.difficulty === filter);

  return (
    <div style={{ maxWidth: "1280px", margin: "0 auto", padding: "3rem 1.5rem" }}>
      {/* Header */}
      <div className="animate-fade-in-up" style={{ marginBottom: "2rem" }}>
        <h1 style={{ fontSize: "2.5rem", fontWeight: 900, marginBottom: "0.75rem" }}>
          🎯 Coding <span className="gradient-text">Challenges</span>
        </h1>
        <p style={{ color: "var(--text-secondary)", fontSize: "1.1rem", maxWidth: "600px" }}>
          Practice your skills with hands-on coding problems.
          Write Python code, run tests, and get instant feedback.
        </p>
      </div>

      {/* Filters */}
      <div className="animate-fade-in-up stagger-1" style={{
        display: "flex", gap: "0.5rem", marginBottom: "2rem", flexWrap: "wrap",
      }}>
        {["all", ...DIFFICULTY_ORDER].map((d) => (
          <button
            key={d}
            onClick={() => setFilter(d)}
            style={{
              padding: "0.5rem 1.25rem",
              borderRadius: "20px",
              border: filter === d ? "1px solid var(--accent-primary)" : "1px solid var(--border-subtle)",
              background: filter === d ? "rgba(99, 102, 241, 0.15)" : "transparent",
              color: filter === d ? "var(--accent-primary)" : "var(--text-secondary)",
              cursor: "pointer",
              fontSize: "0.85rem",
              fontWeight: 600,
              textTransform: "capitalize",
              fontFamily: "inherit",
              transition: "all 0.2s ease",
            }}
          >
            {d === "all" ? "All" : d} {d !== "all" ? `(${challenges.filter(c => c.difficulty === d).length})` : `(${challenges.length})`}
          </button>
        ))}
      </div>

      {/* Challenge List */}
      {loading ? (
        <div style={{ textAlign: "center", padding: "3rem", color: "var(--text-muted)" }}>Loading challenges...</div>
      ) : (
        <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
          {filtered.map((challenge, i) => (
            <Link
              key={challenge.id}
              href={`/challenges/${challenge.id}`}
              className={`glass-card animate-fade-in-up stagger-${Math.min(i + 1, 6)}`}
              style={{
                padding: "1.75rem",
                textDecoration: "none",
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                gap: "1.5rem",
                position: "relative",
                overflow: "hidden",
                transition: "all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275)"
              }}
              onMouseEnter={(e) => {
                e.currentTarget.style.transform = 'translateY(-5px) scale(1.01)';
                e.currentTarget.style.boxShadow = '0 8px 30px rgba(99, 102, 241, 0.2)';
                e.currentTarget.style.borderColor = 'rgba(99, 102, 241, 0.5)';
              }}
              onMouseLeave={(e) => {
                e.currentTarget.style.transform = 'translateY(0) scale(1)';
                e.currentTarget.style.boxShadow = 'var(--glow-primary)';
                e.currentTarget.style.borderColor = 'var(--border-subtle)';
              }}
            >
              <div style={{ flex: 1 }}>
                <div style={{ display: "flex", alignItems: "center", gap: "1rem", marginBottom: "0.5rem" }}>
                  <h3 style={{ fontSize: "1.2rem", fontWeight: 800, color: "var(--text-primary)" }}>
                    {challenge.title}
                  </h3>
                  <span className={`badge badge-${challenge.difficulty}`}>{challenge.difficulty}</span>
                </div>
                <p style={{ fontSize: "0.95rem", color: "var(--text-secondary)", lineHeight: 1.6 }}>
                  {challenge.description}
                </p>
              </div>
              <div style={{
                padding: "0.5rem 1rem",
                borderRadius: "8px",
                background: "rgba(99, 102, 241, 0.1)",
                color: "var(--accent-primary)",
                fontSize: "0.85rem",
                fontWeight: 600,
                whiteSpace: "nowrap",
              }}>
                Solve →
              </div>
            </Link>
          ))}

          {filtered.length === 0 && (
            <div style={{ textAlign: "center", padding: "3rem", color: "var(--text-muted)" }}>
              No challenges found for this filter.
            </div>
          )}
        </div>
      )}
    </div>
  );
}
