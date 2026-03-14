"use client";

import { useParams } from "next/navigation";
import { useEffect, useState, useCallback } from "react";
import Link from "next/link";

interface ChallengeDetail {
  id: string;
  title: string;
  difficulty: string;
  category: string;
  description: string;
  starter_code: string;
  hints: string[];
  time_complexity: string;
  space_complexity: string;
  num_tests: number;
}

interface TestResultItem {
  input: Record<string, unknown>;
  expected: unknown;
  actual: unknown;
  passed: boolean;
}

interface EvalResult {
  passed: boolean;
  total_tests: number;
  passed_tests: number;
  results: TestResultItem[];
  error?: string;
}

export default function ChallengePage() {
  const params = useParams();
  const id = params.id as string;

  const [challenge, setChallenge] = useState<ChallengeDetail | null>(null);
  const [code, setCode] = useState("");
  const [evalResult, setEvalResult] = useState<EvalResult | null>(null);
  const [running, setRunning] = useState(false);
  const [showHints, setShowHints] = useState(false);
  const [activeHint, setActiveHint] = useState(0);

  useEffect(() => {
    fetch(`http://localhost:8000/api/challenges/${id}`)
      .then((res) => {
        if (!res.ok) throw new Error("Challenge not found");
        return res.json();
      })
      .then((data) => {
        setChallenge(data);
        setCode(data.starter_code || "");
      })
      .catch(() => {
        setChallenge({
          id, title: id.replace(/_/g, " ").replace(/\b\w/g, (c) => c.toUpperCase()),
          difficulty: "easy", category: "general",
          description: "Challenge loading... Start the API: `cd api && uvicorn main:app --reload`",
          starter_code: "# Your code here\n",
          hints: ["Start the API server to load this challenge."],
          time_complexity: "?", space_complexity: "?", num_tests: 0,
        });
        setCode("# Your code here\n");
      });
  }, [id]);

  const handleSubmit = useCallback(async () => {
    setRunning(true);
    setEvalResult(null);

    try {
      const res = await fetch("http://localhost:8000/api/evaluate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ challenge_id: id, code }),
      });
      if (!res.ok) throw new Error("Evaluation failed");
      const data = await res.json();
      setEvalResult(data);
    } catch {
      setEvalResult({
        passed: false, total_tests: 0, passed_tests: 0, results: [],
        error: "Could not connect to API or an internal error occurred. Try reloading or check server.",
      });
    }

    setRunning(false);
  }, [id, code]);

  if (!challenge) {
    return (
      <div style={{ maxWidth: "1280px", margin: "0 auto", padding: "3rem 1.5rem", textAlign: "center" }}>
        <p style={{ color: "var(--text-muted)" }}>Loading challenge...</p>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: "1280px", margin: "0 auto", padding: "2rem 1.5rem" }}>
      {/* Header */}
      <div className="animate-fade-in-up" style={{
        display: "flex", justifyContent: "space-between", alignItems: "flex-start",
        marginBottom: "1.5rem", flexWrap: "wrap", gap: "1rem",
      }}>
        <div>
          <div style={{ display: "flex", alignItems: "center", gap: "0.75rem", marginBottom: "0.5rem" }}>
            <Link href="/challenges" style={{ color: "var(--text-muted)", textDecoration: "none", fontSize: "0.85rem" }}>
              ← Challenges
            </Link>
          </div>
          <h1 style={{ fontSize: "1.75rem", fontWeight: 800, marginBottom: "0.5rem" }}>
            {challenge.title}
          </h1>
          <div style={{ display: "flex", gap: "0.75rem", alignItems: "center" }}>
            <span className={`badge badge-${challenge.difficulty}`}>{challenge.difficulty}</span>
            <span className="complexity-badge">Time: {challenge.time_complexity}</span>
            <span className="complexity-badge">Space: {challenge.space_complexity}</span>
          </div>
        </div>
      </div>

      {/* Two-column layout */}
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "1.5rem", minHeight: "500px" }}>
        {/* Left — Problem description */}
        <div className="glass-card animate-fade-in-up stagger-1" style={{ padding: "1.5rem", overflow: "auto" }}>
          <h2 style={{ fontSize: "1rem", fontWeight: 700, marginBottom: "1rem", color: "var(--accent-primary)" }}>
            📋 Problem Description
          </h2>
          <div style={{ color: "var(--text-secondary)", fontSize: "0.9rem", lineHeight: 1.8, whiteSpace: "pre-wrap" }}>
            {challenge.description}
          </div>

          {/* Hints */}
          <div style={{ marginTop: "1.5rem" }}>
            <button
              onClick={() => setShowHints(!showHints)}
              style={{
                background: "rgba(245, 158, 11, 0.1)",
                border: "1px solid rgba(245, 158, 11, 0.3)",
                color: "#fbbf24",
                padding: "0.5rem 1rem",
                borderRadius: "8px",
                cursor: "pointer",
                fontSize: "0.85rem",
                fontWeight: 600,
                fontFamily: "inherit",
              }}
            >
              💡 {showHints ? "Hide" : "Show"} Hints ({challenge.hints.length})
            </button>

            {showHints && (
              <div style={{ marginTop: "1rem" }}>
                {challenge.hints.slice(0, activeHint + 1).map((hint, i) => (
                  <div key={i} style={{
                    background: "rgba(245, 158, 11, 0.05)",
                    border: "1px solid rgba(245, 158, 11, 0.15)",
                    borderRadius: "8px",
                    padding: "0.75rem 1rem",
                    marginBottom: "0.5rem",
                    color: "var(--text-secondary)",
                    fontSize: "0.85rem",
                  }}>
                    <strong style={{ color: "#fbbf24" }}>Hint {i + 1}:</strong> {hint}
                  </div>
                ))}
                {activeHint < challenge.hints.length - 1 && (
                  <button
                    onClick={() => setActiveHint(activeHint + 1)}
                    style={{
                      background: "transparent",
                      border: "none",
                      color: "#fbbf24",
                      cursor: "pointer",
                      fontSize: "0.8rem",
                      fontFamily: "inherit",
                      padding: "0.25rem 0",
                    }}
                  >
                    Show next hint →
                  </button>
                )}
              </div>
            )}
          </div>
        </div>

        {/* Right — Code editor + results */}
        <div style={{ display: "flex", flexDirection: "column", gap: "1rem" }}>
          {/* Code Editor */}
          <div className="glass-card animate-fade-in-up stagger-2" style={{ padding: "1.5rem", flex: 1, display: "flex", flexDirection: "column" }}>
            <div style={{
              display: "flex", justifyContent: "space-between", alignItems: "center",
              marginBottom: "1rem",
            }}>
              <h2 style={{ fontSize: "1.1rem", fontWeight: 800, color: "var(--accent-primary)" }}>
                🐍 Python Workspace
              </h2>
              <button
                onClick={handleSubmit}
                disabled={running}
                className="btn-primary"
                style={{
                  padding: "0.6rem 1.5rem",
                  fontSize: "0.9rem",
                  opacity: running ? 0.6 : 1,
                  boxShadow: '0 4px 15px rgba(16, 185, 129, 0.3)',
                  background: 'linear-gradient(135deg, #10b981, #059669)'
                }}
              >
                {running ? "⏳ Executing..." : "▶ Run Tests"}
              </button>
            </div>

            <textarea
              value={code}
              onChange={(e) => setCode(e.target.value)}
              spellCheck={false}
              style={{
                width: "100%",
                flex: 1,
                minHeight: "350px",
                background: "#0a0a1a",
                border: "1px solid var(--border-active)",
                borderRadius: "12px",
                padding: "1.25rem",
                color: "#e2e8f0",
                fontFamily: "'JetBrains Mono', monospace",
                fontSize: "0.9rem",
                lineHeight: 1.7,
                resize: "vertical",
                outline: "none",
                boxShadow: "inset 0 2px 10px rgba(0,0,0,0.5)"
              }}
            />
          </div>

          {/* Results */}
          {evalResult && (
            <div className="glass-card animate-fade-in-up" style={{ padding: "1.5rem" }}>
              <div style={{
                display: "flex", justifyContent: "space-between", alignItems: "center",
                marginBottom: "1rem",
              }}>
                <h2 style={{
                  fontSize: "1rem", fontWeight: 700,
                  color: evalResult.passed ? "#34d399" : "#f87171",
                }}>
                  {evalResult.passed ? "✅ All Tests Passed!" : `❌ ${evalResult.passed_tests}/${evalResult.total_tests} Passed`}
                </h2>
              </div>

              {evalResult.error && (
                <div style={{
                  background: "rgba(239, 68, 68, 0.1)",
                  border: "1px solid rgba(239, 68, 68, 0.3)",
                  borderRadius: "8px", padding: "0.75rem 1rem",
                  color: "#f87171", fontSize: "0.85rem", marginBottom: "1rem",
                }}>
                  {evalResult.error}
                </div>
              )}

              {evalResult.results.map((r, i) => (
                <div key={i} style={{
                  background: r.passed ? "rgba(16, 185, 129, 0.05)" : "rgba(239, 68, 68, 0.05)",
                  border: `1px solid ${r.passed ? "rgba(16, 185, 129, 0.2)" : "rgba(239, 68, 68, 0.2)"}`,
                  borderRadius: "8px", padding: "0.75rem 1rem",
                  marginBottom: "0.5rem", fontSize: "0.8rem",
                  fontFamily: "'JetBrains Mono', monospace",
                }}>
                  <div style={{ color: r.passed ? "#34d399" : "#f87171", fontWeight: 600, marginBottom: "0.25rem" }}>
                    {r.passed ? "✅" : "❌"} Test {i + 1}
                  </div>
                  <div style={{ color: "var(--text-muted)" }}>
                    Input: {JSON.stringify(r.input)} | Expected: {JSON.stringify(r.expected)} | Got: {JSON.stringify(r.actual)}
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
