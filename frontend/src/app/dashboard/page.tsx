"use client";

import { useState } from "react";
import Link from "next/link";

const MODULES = [
  {
    id: "foundations",
    title: "Foundations",
    icon: "📐",
    topics: [
      { slug: "big-o-notation", title: "Big O Notation" },
      { slug: "time-complexity", title: "Time Complexity" },
      { slug: "space-complexity", title: "Space Complexity" },
    ],
  },
  {
    id: "data-structures",
    title: "Data Structures",
    icon: "🏗️",
    topics: [
      { slug: "arrays", title: "Arrays" },
      { slug: "linked-lists", title: "Linked Lists" },
      { slug: "stacks", title: "Stacks" },
      { slug: "queues", title: "Queues" },
      { slug: "hash-tables", title: "Hash Tables" },
      { slug: "trees", title: "Trees & BST" },
      { slug: "heaps", title: "Heaps" },
      { slug: "graphs", title: "Graphs" },
    ],
  },
  {
    id: "algorithms",
    title: "Algorithms",
    icon: "⚡",
    topics: [
      { slug: "searching", title: "Searching" },
      { slug: "sorting", title: "Sorting" },
      { slug: "recursion", title: "Recursion" },
      { slug: "dynamic-programming", title: "Dynamic Programming" },
      { slug: "graph-algorithms", title: "Graph Algorithms" },
    ],
  },
  {
    id: "advanced",
    title: "Advanced",
    icon: "🚀",
    topics: [
      { slug: "tries", title: "Tries" },
      { slug: "segment-trees", title: "Segment Trees" },
      { slug: "union-find", title: "Union-Find" },
    ],
  },
];

export default function DashboardPage() {
  const [completedTopics, setCompletedTopics] = useState<Set<string>>(new Set());

  const totalTopics = MODULES.reduce((sum, m) => sum + m.topics.length, 0);
  const completedCount = completedTopics.size;
  const progressPct = totalTopics > 0 ? Math.round((completedCount / totalTopics) * 100) : 0;

  const toggleTopic = (slug: string) => {
    setCompletedTopics((prev) => {
      const next = new Set(prev);
      if (next.has(slug)) next.delete(slug);
      else next.add(slug);
      return next;
    });
  };

  return (
    <div style={{ maxWidth: "1280px", margin: "0 auto", padding: "3rem 1.5rem" }}>
      {/* Header */}
      <div className="animate-fade-in-up" style={{ marginBottom: "2.5rem" }}>
        <h1 style={{ fontSize: "2.5rem", fontWeight: 900, marginBottom: "0.75rem" }}>
          📈 Learning <span className="gradient-text">Dashboard</span>
        </h1>
        <p style={{ color: "var(--text-secondary)", fontSize: "1.1rem" }}>
          Track your progress across all DSA topics.
        </p>
      </div>

      {/* Overall Progress */}
      <div className="glass-card animate-fade-in-up stagger-1 animate-pulse-glow" style={{
        padding: "2rem",
        marginBottom: "2rem",
        textAlign: "center",
      }}>
        <div style={{ fontSize: "3rem", fontWeight: 900, marginBottom: "0.5rem" }} className="gradient-text">
          {progressPct}%
        </div>
        <p style={{ color: "var(--text-secondary)", marginBottom: "1rem" }}>
          {completedCount} of {totalTopics} topics completed
        </p>
        <div className="progress-bar" style={{ maxWidth: "400px", margin: "0 auto", height: "8px" }}>
          <div className="progress-bar-fill" style={{ width: `${progressPct}%` }} />
        </div>
      </div>

      {/* Stats Row */}
      <div className="animate-fade-in-up stagger-2" style={{
        display: "grid",
        gridTemplateColumns: "repeat(auto-fit, minmax(200px, 1fr))",
        gap: "1rem",
        marginBottom: "2.5rem",
      }}>
        {[
          { label: "Topics Available", value: totalTopics, icon: "📚", color: "#6366f1" },
          { label: "Completed", value: completedCount, icon: "✅", color: "#10b981" },
          { label: "In Progress", value: totalTopics - completedCount, icon: "🔄", color: "#f59e0b" },
          { label: "Challenges Solved", value: 0, icon: "🎯", color: "#ec4899" },
        ].map((stat) => (
          <div key={stat.label} className="glass-card" style={{ padding: "1.25rem", textAlign: "center" }}>
            <div style={{ fontSize: "1.5rem", marginBottom: "0.5rem" }}>{stat.icon}</div>
            <div style={{ fontSize: "1.5rem", fontWeight: 800, color: stat.color }}>{stat.value}</div>
            <div style={{ fontSize: "0.8rem", color: "var(--text-muted)", marginTop: "0.25rem" }}>{stat.label}</div>
          </div>
        ))}
      </div>

      {/* Module Progress */}
      {MODULES.map((mod, mi) => {
        const moduleCompleted = mod.topics.filter((t) => completedTopics.has(t.slug)).length;
        const modulePct = Math.round((moduleCompleted / mod.topics.length) * 100);

        return (
          <div key={mod.id} className={`glass-card animate-fade-in-up stagger-${mi + 1}`} style={{
            padding: "1.5rem",
            marginBottom: "1rem",
          }}>
            <div style={{
              display: "flex", justifyContent: "space-between", alignItems: "center",
              marginBottom: "1rem",
            }}>
              <div style={{ display: "flex", alignItems: "center", gap: "0.75rem" }}>
                <span style={{ fontSize: "1.5rem" }}>{mod.icon}</span>
                <h2 style={{ fontSize: "1.2rem", fontWeight: 800 }}>{mod.title}</h2>
              </div>
              <span style={{ fontSize: "0.85rem", color: "var(--text-muted)" }}>
                {moduleCompleted}/{mod.topics.length} • {modulePct}%
              </span>
            </div>

            <div className="progress-bar" style={{ marginBottom: "1rem" }}>
              <div className="progress-bar-fill" style={{ width: `${modulePct}%` }} />
            </div>

            <div style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))",
              gap: "0.5rem",
            }}>
              {mod.topics.map((topic) => (
                <div
                  key={topic.slug}
                  onClick={() => toggleTopic(topic.slug)}
                  style={{
                    display: "flex",
                    alignItems: "center",
                    gap: "0.5rem",
                    padding: "0.6rem 0.75rem",
                    borderRadius: "8px",
                    cursor: "pointer",
                    background: completedTopics.has(topic.slug) ? "rgba(16, 185, 129, 0.1)" : "rgba(99, 102, 241, 0.05)",
                    border: `1px solid ${completedTopics.has(topic.slug) ? "rgba(16, 185, 129, 0.3)" : "transparent"}`,
                    transition: "all 0.2s ease",
                  }}
                >
                  <div style={{
                    width: "18px", height: "18px", borderRadius: "4px",
                    border: completedTopics.has(topic.slug) ? "2px solid #10b981" : "2px solid var(--border-active)",
                    display: "flex", alignItems: "center", justifyContent: "center",
                    background: completedTopics.has(topic.slug) ? "#10b981" : "transparent",
                    fontSize: "0.7rem", color: "white", flexShrink: 0,
                  }}>
                    {completedTopics.has(topic.slug) && "✓"}
                  </div>
                  <Link href={`/learn/${topic.slug}`} style={{
                    fontSize: "0.85rem",
                    color: completedTopics.has(topic.slug) ? "#34d399" : "var(--text-secondary)",
                    textDecoration: completedTopics.has(topic.slug) ? "line-through" : "none",
                    fontWeight: 500,
                  }}>
                    {topic.title}
                  </Link>
                </div>
              ))}
            </div>
          </div>
        );
      })}
    </div>
  );
}
