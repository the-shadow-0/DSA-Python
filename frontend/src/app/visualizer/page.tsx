"use client";

import { useState, useRef, useEffect, useCallback } from "react";

type AlgorithmKey = 'bubbleSort' | 'selectionSort' | 'insertionSort' | 'mergeSort' | 'quickSort';

interface Step {
  type: string;
  indices: number[];
  array: number[];
}

// ── Sorting algorithms with step tracing ──
function bubbleSortTrace(arr: number[]): Step[] {
  const a = [...arr];
  const steps: Step[] = [{ type: "initial", indices: [], array: [...a] }];
  const n = a.length;
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      steps.push({ type: "compare", indices: [j, j + 1], array: [...a] });
      if (a[j] > a[j + 1]) {
        [a[j], a[j + 1]] = [a[j + 1], a[j]];
        steps.push({ type: "swap", indices: [j, j + 1], array: [...a] });
      }
    }
  }
  steps.push({ type: "done", indices: [], array: [...a] });
  return steps;
}

function selectionSortTrace(arr: number[]): Step[] {
  const a = [...arr];
  const steps: Step[] = [{ type: "initial", indices: [], array: [...a] }];
  for (let i = 0; i < a.length; i++) {
    let min = i;
    for (let j = i + 1; j < a.length; j++) {
      steps.push({ type: "compare", indices: [min, j], array: [...a] });
      if (a[j] < a[min]) min = j;
    }
    if (min !== i) {
      [a[i], a[min]] = [a[min], a[i]];
      steps.push({ type: "swap", indices: [i, min], array: [...a] });
    }
  }
  steps.push({ type: "done", indices: [], array: [...a] });
  return steps;
}

function insertionSortTrace(arr: number[]): Step[] {
  const a = [...arr];
  const steps: Step[] = [{ type: "initial", indices: [], array: [...a] }];
  for (let i = 1; i < a.length; i++) {
    const key = a[i];
    let j = i - 1;
    steps.push({ type: "select", indices: [i], array: [...a] });
    while (j >= 0 && a[j] > key) {
      steps.push({ type: "compare", indices: [j, j + 1], array: [...a] });
      a[j + 1] = a[j];
      j--;
    }
    a[j + 1] = key;
    steps.push({ type: "insert", indices: [j + 1], array: [...a] });
  }
  steps.push({ type: "done", indices: [], array: [...a] });
  return steps;
}

function mergeSortTrace(arr: number[]): Step[] {
  const a = [...arr];
  const steps: Step[] = [{ type: "initial", indices: [], array: [...a] }];
  function sort(a: number[], l: number, r: number, out: number[]) {
    if (l >= r) return;
    const m = Math.floor((l + r) / 2);
    sort(a, l, m, out);
    sort(a, m + 1, r, out);
    const merged: number[] = [];
    let i = l, j = m + 1;
    while (i <= m && j <= r) {
      steps.push({ type: "compare", indices: [i, j], array: [...out] });
      if (out[i] <= out[j]) merged.push(out[i++]);
      else merged.push(out[j++]);
    }
    while (i <= m) merged.push(out[i++]);
    while (j <= r) merged.push(out[j++]);
    for (let k = 0; k < merged.length; k++) out[l + k] = merged[k];
    steps.push({ type: "merge", indices: Array.from({ length: r - l + 1 }, (_, k) => l + k), array: [...out] });
  }
  sort(a, 0, a.length - 1, a);
  steps.push({ type: "done", indices: [], array: [...a] });
  return steps;
}

function quickSortTrace(arr: number[]): Step[] {
  const a = [...arr];
  const steps: Step[] = [{ type: "initial", indices: [], array: [...a] }];
  function sort(l: number, h: number) {
    if (l >= h) return;
    const pivot = a[h];
    steps.push({ type: "pivot", indices: [h], array: [...a] });
    let i = l - 1;
    for (let j = l; j < h; j++) {
      steps.push({ type: "compare", indices: [j, h], array: [...a] });
      if (a[j] <= pivot) {
        i++;
        [a[i], a[j]] = [a[j], a[i]];
        if (i !== j) steps.push({ type: "swap", indices: [i, j], array: [...a] });
      }
    }
    [a[i + 1], a[h]] = [a[h], a[i + 1]];
    steps.push({ type: "swap", indices: [i + 1, h], array: [...a] });
    sort(l, i);
    sort(i + 2, h);
  }
  sort(0, a.length - 1);
  steps.push({ type: "done", indices: [], array: [...a] });
  return steps;
}

const ALGORITHMS: Record<AlgorithmKey, { name: string; fn: (arr: number[]) => Step[]; complexity: string }> = {
  bubbleSort: { name: "Bubble Sort", fn: bubbleSortTrace, complexity: "O(n²)" },
  selectionSort: { name: "Selection Sort", fn: selectionSortTrace, complexity: "O(n²)" },
  insertionSort: { name: "Insertion Sort", fn: insertionSortTrace, complexity: "O(n²)" },
  mergeSort: { name: "Merge Sort", fn: mergeSortTrace, complexity: "O(n log n)" },
  quickSort: { name: "Quick Sort", fn: quickSortTrace, complexity: "O(n log n)" },
};

function generateArray(size: number): number[] {
  return Array.from({ length: size }, () => Math.floor(Math.random() * 80) + 10);
}

export default function VisualizerPage() {
  const [algo, setAlgo] = useState<AlgorithmKey>("bubbleSort");
  const [arraySize, setArraySize] = useState(20);
  const [speed, setSpeed] = useState(75);
  const [data, setData] = useState<number[]>([]);
  const [steps, setSteps] = useState<Step[]>([]);
  const [stepIndex, setStepIndex] = useState(0);
  const [playing, setPlaying] = useState(false);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const timerRef = useRef<ReturnType<typeof setInterval> | null>(null);

  // Generate initial array
  useEffect(() => {
    const arr = generateArray(arraySize);
    setData(arr);
    setSteps([{ type: "initial", indices: [], array: arr }]);
    setStepIndex(0);
    setPlaying(false);
  }, [arraySize]);

  // Render canvas
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const step = steps[stepIndex] || { type: "initial", indices: [], array: data };
    const arr = step.array;
    const w = canvas.width;
    const h = canvas.height;
    const barWidth = Math.max(2, (w - 20) / arr.length - 1);
    const maxVal = Math.max(...arr, 1);

    ctx.clearRect(0, 0, w, h);

    arr.forEach((val, i) => {
      const barHeight = (val / maxVal) * (h - 40);
      const x = 10 + i * (barWidth + 1);
      const y = h - 20 - barHeight;

      // Color based on step type
      let color = "#6366f1";
      if (step.type === "done") {
        color = "#10b981";
      } else if (step.indices.includes(i)) {
        if (step.type === "compare") color = "#f59e0b";
        else if (step.type === "swap") color = "#ec4899";
        else if (step.type === "pivot") color = "#ef4444";
        else if (step.type === "merge") color = "#06b6d4";
        else if (step.type === "select" || step.type === "insert") color = "#8b5cf6";
      }

      // Bar
      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.roundRect(x, y, barWidth, barHeight, [3, 3, 0, 0]);
      ctx.fill();

      // Glow effect for active indices
      if (step.indices.includes(i) && step.type !== "done") {
        ctx.shadowColor = color;
        ctx.shadowBlur = 12;
        ctx.fillStyle = color;
        ctx.beginPath();
        ctx.roundRect(x, y, barWidth, barHeight, [3, 3, 0, 0]);
        ctx.fill();
        ctx.shadowBlur = 0;
      }
    });
  }, [steps, stepIndex, data]);

  // Playback control
  useEffect(() => {
    if (playing && stepIndex < steps.length - 1) {
      timerRef.current = setInterval(() => {
        setStepIndex((prev) => {
          if (prev >= steps.length - 1) {
            setPlaying(false);
            return prev;
          }
          return prev + 1;
        });
      }, Math.max(10, 200 - speed * 2));
    }
    return () => { if (timerRef.current) clearInterval(timerRef.current); };
  }, [playing, speed, steps.length, stepIndex]);

  const handleStart = useCallback(() => {
    const arr = [...data];
    const stepsResult = ALGORITHMS[algo].fn(arr);
    setSteps(stepsResult);
    setStepIndex(0);
    setPlaying(true);
  }, [algo, data]);

  const handleReset = useCallback(() => {
    const arr = generateArray(arraySize);
    setData(arr);
    setSteps([{ type: "initial", indices: [], array: arr }]);
    setStepIndex(0);
    setPlaying(false);
  }, [arraySize]);

  const currentStep = steps[stepIndex];

  return (
    <div style={{ maxWidth: "1280px", margin: "0 auto", padding: "2rem 1.5rem" }}>
      {/* Header */}
      <div className="animate-fade-in-up" style={{ marginBottom: "2rem" }}>
        <h1 style={{ fontSize: "2.5rem", fontWeight: 900, marginBottom: "0.75rem" }}>
          📊 Algorithm <span className="gradient-text">Visualizer</span>
        </h1>
        <p style={{ color: "var(--text-secondary)", fontSize: "1.1rem" }}>
          Watch sorting algorithms execute step-by-step with animated bars.
        </p>
      </div>

      {/* Controls */}
      <div className="glass-card animate-fade-in-up stagger-1" style={{
        padding: "1.25rem", marginBottom: "1.5rem",
        display: "flex", flexWrap: "wrap", gap: "1.5rem", alignItems: "center",
      }}>
        {/* Algorithm selector */}
        <div>
          <label style={{ fontSize: "0.75rem", color: "var(--text-muted)", fontWeight: 600, textTransform: "uppercase", letterSpacing: "0.05em", display: "block", marginBottom: "0.5rem" }}>Algorithm</label>
          <select
            value={algo}
            onChange={(e) => { setAlgo(e.target.value as AlgorithmKey); setStepIndex(0); setPlaying(false); }}
            style={{
              background: "#0d0d2b", border: "1px solid var(--border-subtle)",
              borderRadius: "8px", padding: "0.5rem 1rem", color: "var(--text-primary)",
              fontFamily: "inherit", fontSize: "0.9rem", cursor: "pointer", outline: "none",
            }}
          >
            {Object.entries(ALGORITHMS).map(([key, { name, complexity }]) => (
              <option key={key} value={key}>{name} — {complexity}</option>
            ))}
          </select>
        </div>

        {/* Array size */}
        <div>
          <label style={{ fontSize: "0.75rem", color: "var(--text-muted)", fontWeight: 600, textTransform: "uppercase", letterSpacing: "0.05em", display: "block", marginBottom: "0.5rem" }}>
            Size: {arraySize}
          </label>
          <input type="range" min="5" max="80" value={arraySize}
            onChange={(e) => setArraySize(Number(e.target.value))}
            style={{ width: "120px", accentColor: "var(--accent-primary)" }}
          />
        </div>

        {/* Speed */}
        <div>
          <label style={{ fontSize: "0.75rem", color: "var(--text-muted)", fontWeight: 600, textTransform: "uppercase", letterSpacing: "0.05em", display: "block", marginBottom: "0.5rem" }}>
            Speed: {speed}%
          </label>
          <input type="range" min="1" max="100" value={speed}
            onChange={(e) => setSpeed(Number(e.target.value))}
            style={{ width: "120px", accentColor: "var(--accent-secondary)" }}
          />
        </div>

        {/* Buttons */}
        <div style={{ display: "flex", gap: "0.5rem", marginLeft: "auto" }}>
          <button onClick={handleStart} className="btn-primary" style={{ padding: "0.5rem 1.25rem", fontSize: "0.85rem" }}>
            ▶ {playing ? "Restart" : "Start"}
          </button>
          <button onClick={() => setPlaying(!playing)} className="btn-secondary" style={{ padding: "0.5rem 1rem", fontSize: "0.85rem" }}>
            {playing ? "⏸ Pause" : "▶ Resume"}
          </button>
          <button onClick={() => setStepIndex(Math.min(stepIndex + 1, steps.length - 1))} className="btn-secondary" style={{ padding: "0.5rem 0.75rem", fontSize: "0.85rem" }}>
            ⏭
          </button>
          <button onClick={handleReset} className="btn-secondary" style={{ padding: "0.5rem 1rem", fontSize: "0.85rem" }}>
            🔄 Reset
          </button>
        </div>
      </div>

      {/* Canvas */}
      <div className="glass-card animate-fade-in-up stagger-2" style={{ padding: "1.5rem" }}>
        <canvas
          ref={canvasRef}
          width={1200}
          height={400}
          style={{
            width: "100%",
            height: "400px",
            borderRadius: "8px",
            background: "#0a0a1a",
          }}
        />

        {/* Step info */}
        <div style={{
          display: "flex", justifyContent: "space-between", alignItems: "center",
          marginTop: "1rem", color: "var(--text-muted)", fontSize: "0.85rem",
        }}>
          <div>
            Step: <strong style={{ color: "var(--text-primary)" }}>{stepIndex}</strong> / {steps.length - 1}
          </div>
          <div style={{ display: "flex", gap: "1rem" }}>
            {currentStep && (
              <>
                <span>Action: <strong style={{
                  color: currentStep.type === "swap" ? "#ec4899" :
                    currentStep.type === "compare" ? "#f59e0b" :
                    currentStep.type === "done" ? "#10b981" : "var(--text-primary)"
                }}>{currentStep.type}</strong></span>
                {currentStep.indices.length > 0 && (
                  <span>Indices: <strong style={{ color: "var(--text-primary)" }}>[{currentStep.indices.join(", ")}]</strong></span>
                )}
              </>
            )}
          </div>
        </div>

        {/* Progress bar */}
        <div className="progress-bar" style={{ marginTop: "0.75rem" }}>
          <div className="progress-bar-fill" style={{ width: `${steps.length > 1 ? (stepIndex / (steps.length - 1)) * 100 : 0}%` }} />
        </div>

        {/* Legend */}
        <div style={{
          display: "flex", gap: "1.5rem", marginTop: "1rem", fontSize: "0.8rem",
          color: "var(--text-muted)", flexWrap: "wrap",
        }}>
          {[
            { color: "#6366f1", label: "Default" },
            { color: "#f59e0b", label: "Comparing" },
            { color: "#ec4899", label: "Swapping" },
            { color: "#ef4444", label: "Pivot" },
            { color: "#06b6d4", label: "Merging" },
            { color: "#10b981", label: "Sorted" },
          ].map(({ color, label }) => (
            <div key={label} style={{ display: "flex", alignItems: "center", gap: "0.4rem" }}>
              <div style={{ width: "12px", height: "12px", borderRadius: "3px", background: color }} />
              {label}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
