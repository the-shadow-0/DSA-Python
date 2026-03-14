"use client";

import { useParams } from "next/navigation";
import { useEffect, useState } from "react";
import Link from "next/link";

interface TopicData {
  slug: string;
  title: string;
  description: string;
  module: string;
  content: string;
}

export default function TopicPage() {
  const params = useParams();
  const slug = params.topic as string;
  const [topic, setTopic] = useState<TopicData | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch(`http://localhost:8000/api/topics/${slug}`)
      .then((res) => res.json())
      .then((data) => {
        setTopic(data);
        setLoading(false);
      })
      .catch(() => {
        setTopic({
          slug,
          title: slug.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase()),
          description: "Learn about this topic with visual explanations and Python code.",
          module: "Data Structures",
          content: `# ${slug.replace(/-/g, " ").replace(/\b\w/g, (c) => c.toUpperCase())}\n\nContent is loading... Start the API server with:\n\n\`\`\`bash\ncd api && uvicorn main:app --reload\n\`\`\``,
        });
        setLoading(false);
      });
  }, [slug]);

  const renderContent = (md: string) => {
    const lines = md.split("\n");
    const html: string[] = [];
    let inCodeBlock = false;
    let inTable = false;
    let codeLines: string[] = [];
    let codeLang = "";

    for (const line of lines) {
      if (line.startsWith("```") && !inCodeBlock) {
        inCodeBlock = true;
        codeLang = line.slice(3).trim();
        codeLines = [];
        continue;
      } else if (line.startsWith("```") && inCodeBlock) {
        inCodeBlock = false;
        html.push(`<pre><code class="language-${codeLang}">${codeLines.join("\n").replace(/</g, "&lt;").replace(/>/g, "&gt;")}</code></pre>`);
        continue;
      } else if (inCodeBlock) {
        codeLines.push(line);
        continue;
      }

      // Handle table ends
      if (!line.startsWith("|") && inTable) {
        inTable = false;
        html.push("</tbody></table></div>");
      }

      if (line.startsWith("## ")) {
        html.push(`<h2 style="font-size: 1.5rem; font-weight: 800; margin: 2rem 0 1rem; color: var(--text-primary);">${line.slice(3)}</h2>`);
      } else if (line.startsWith("# ")) {
        html.push(`<h1 style="font-size: 2rem; font-weight: 900; margin-bottom: 1.5rem;" class="gradient-text">${line.slice(2)}</h1>`);
      } else if (line.startsWith("### ")) {
        html.push(`<h3 style="font-size: 1.15rem; font-weight: 700; margin: 1.5rem 0 0.75rem; color: var(--text-primary);">${line.slice(4)}</h3>`);
      } else if (line.startsWith("|") && !line.includes("---")) {
        // Table support
        if (!inTable) {
          inTable = true;
          html.push(`<div style="overflow-x: auto; margin: 1rem 0;"><table style="width: 100%; border-collapse: collapse; font-size: 0.9rem;"><tbody>`);
        }
        const cells = line.split("|").filter(Boolean).map((c) => c.trim());
        html.push(`<tr>${cells.map((c) => `<td style="padding: 0.6rem 1rem; border: 1px solid var(--border-subtle); color: var(--text-secondary);">${c}</td>`).join("")}</tr>`);
      } else if (line.startsWith("|") && line.includes("---")) {
        // Ignore table separator line
      } else if (line.startsWith("- ") || line.startsWith("* ")) {
        html.push(`<li style="color: var(--text-secondary); margin-left: 1.5rem; margin-bottom: 0.3rem; line-height: 1.7;">${line.slice(2)}</li>`);
      } else if (line.startsWith("**") && line.endsWith("**")) {
        html.push(`<p style="font-weight: 600; color: var(--text-primary); margin: 0.75rem 0;">${line.slice(2, -2)}</p>`);
      } else if (line.trim() === "") {
        html.push("<br />");
      } else if (!line.startsWith("<!--")) {
        // Replace inline code and bolding
        const processed = line.replace(/`([^`]+)`/g, '<code>$1</code>');
        const bold = processed.replace(/\*\*([^*]+)\*\*/g, '<strong style="color: var(--text-primary);">$1</strong>');
        html.push(`<p style="color: var(--text-secondary); line-height: 1.8; margin-bottom: 0.5rem;">${bold}</p>`);
      }
    }

    if (inTable) {
      html.push("</tbody></table></div>");
    }

    return html.join("\n");
  };

  if (loading) {
    return (
      <div style={{ maxWidth: "900px", margin: "0 auto", padding: "3rem 1.5rem", textAlign: "center" }}>
        <div className="animate-shimmer" style={{ width: "200px", height: "24px", borderRadius: "8px", margin: "0 auto 1rem" }} />
        <p style={{ color: "var(--text-muted)" }}>Loading topic...</p>
      </div>
    );
  }

  return (
    <div style={{ maxWidth: "900px", margin: "0 auto", padding: "3rem 1.5rem" }}>
      {/* Breadcrumb */}
      <div className="animate-fade-in-up" style={{
        display: "flex",
        alignItems: "center",
        gap: "0.5rem",
        fontSize: "0.85rem",
        color: "var(--text-muted)",
        marginBottom: "2rem",
      }}>
        <Link href="/learn" style={{ color: "var(--accent-primary)", textDecoration: "none" }}>Learn</Link>
        <span>→</span>
        {topic?.module && <span>{topic.module}</span>}
        <span>→</span>
        <span style={{ color: "var(--text-secondary)" }}>{topic?.title}</span>
      </div>

      {/* Content */}
      <article className="animate-fade-in-up stagger-1">
        {topic?.content ? (
          <div dangerouslySetInnerHTML={{ __html: renderContent(topic.content) }} />
        ) : (
          <div>
            <h1 className="gradient-text" style={{ fontSize: "2rem", fontWeight: 900, marginBottom: "1.5rem" }}>
              {topic?.title}
            </h1>
            <p style={{ color: "var(--text-secondary)", fontSize: "1.1rem" }}>{topic?.description}</p>
          </div>
        )}
      </article>

      {/* Navigation */}
      <div className="animate-fade-in-up stagger-2" style={{
        display: "flex",
        justifyContent: "space-between",
        marginTop: "3rem",
        paddingTop: "2rem",
        borderTop: "1px solid var(--border-subtle)",
      }}>
        <Link href="/learn" className="btn-secondary">
          ← Back to Curriculum
        </Link>
        <Link href="/challenges" className="btn-primary">
          Practice Challenges →
        </Link>
      </div>
    </div>
  );
}
