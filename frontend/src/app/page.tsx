"use client";

import Link from "next/link";

const FEATURES = [
  { icon: "📊", title: "Visual Animations", desc: "Step-by-step algorithm visualizations with interactive controls" },
  { icon: "🐍", title: "Python Code", desc: "Clean, commented implementations with complexity analysis" },
  { icon: "🎯", title: "Interactive Challenges", desc: "Practice problems with automated grading and feedback" },
  { icon: "🌍", title: "Real-World Examples", desc: "See how data structures power real systems" },
  { icon: "📈", title: "Progress Tracking", desc: "Track your learning journey from beginner to advanced" },
  { icon: "🚀", title: "Interview Ready", desc: "Build the skills needed to ace technical interviews" },
];

const TOPICS_PREVIEW = [
  { name: "Big O Notation", complexity: "O(1) → O(n!)", level: "Beginner", color: "#10b981" },
  { name: "Arrays & Hash Tables", complexity: "O(1) lookup", level: "Beginner", color: "#06b6d4" },
  { name: "Linked Lists & Stacks", complexity: "O(1) insert", level: "Beginner", color: "#8b5cf6" },
  { name: "Trees & Graphs", complexity: "O(log n)", level: "Intermediate", color: "#f59e0b" },
  { name: "Sorting Algorithms", complexity: "O(n log n)", level: "Intermediate", color: "#ec4899" },
  { name: "Dynamic Programming", complexity: "Optimization", level: "Advanced", color: "#ef4444" },
];

export default function Home() {
  return (
    <div style={{ position: 'relative' }}>
      {/* ── Hero Section ── */}
      <section style={{
        padding: '8rem 1.5rem 6rem',
        maxWidth: '1280px',
        margin: '0 auto',
        textAlign: 'center',
        position: 'relative',
      }}>
        {/* Badge */}
        <div className="animate-fade-in-up" style={{
          display: 'inline-flex',
          alignItems: 'center',
          gap: '0.6rem',
          padding: '0.6rem 1.5rem',
          borderRadius: '100px',
          background: 'rgba(255, 255, 255, 0.03)',
          border: '1px solid var(--border-subtle)',
          color: 'var(--text-secondary)',
          fontSize: '0.85rem',
          fontWeight: 600,
          marginBottom: '3rem',
          backdropFilter: 'blur(10px)',
          boxShadow: '0 4px 20px rgba(0, 0, 0, 0.2)'
        }}>
          <span style={{ fontSize: '1.2rem' }}>✨</span> Master Data Structures & Algorithms
        </div>

        {/* Heading */}
        <h1 className="animate-fade-in-up stagger-1" style={{
          fontSize: 'clamp(3.5rem, 8vw, 6.5rem)',
          fontWeight: 900,
          lineHeight: 1,
          marginBottom: '2rem',
          letterSpacing: '-0.04em',
        }}>
          The <span className="gradient-text">Premium</span> Path to
          <br />Algorithm Mastery
        </h1>

        {/* Subtitle */}
        <p className="animate-fade-in-up stagger-2" style={{
          fontSize: '1.25rem',
          color: 'var(--text-secondary)',
          maxWidth: '800px',
          margin: '0 auto 3.5rem',
          lineHeight: 1.6,
        }}>
          Experience the most comprehensive DSA learning platform. Beautifully documented,
          visually explained, and interactive from the ground up.
        </p>

        {/* CTA */}
        <div className="animate-fade-in-up stagger-3" style={{ display: 'flex', gap: '1.5rem', justifyContent: 'center', flexWrap: 'wrap' }}>
          <Link href="/learn" className="btn-primary" style={{ fontSize: '1.1rem', padding: '1rem 2.5rem', borderRadius: '100px' }}>
            Get Started for Free
          </Link>
          <Link href="/challenges" className="btn-secondary" style={{ fontSize: '1.1rem', padding: '1rem 2.5rem', borderRadius: '100px' }}>
            View Challenges
          </Link>
        </div>

        {/* Floating Icons/Elements */}
        <div style={{
          position: 'absolute',
          top: '20%',
          left: '5%',
          fontSize: '3rem',
          opacity: 0.1,
          filter: 'blur(2px)',
        }} className="animate-float">🐍</div>
        <div style={{
          position: 'absolute',
          bottom: '10%',
          right: '8%',
          fontSize: '4rem',
          opacity: 0.1,
          filter: 'blur(3px)',
        }} className="animate-float stagger-2">⚡</div>
      </section>

      {/* ── Stats Bar ── */}
      <section style={{
        background: 'rgba(255, 255, 255, 0.02)',
        borderTop: '1px solid var(--border-subtle)',
        borderBottom: '1px solid var(--border-subtle)',
        padding: '4rem 1.5rem',
        backdropFilter: 'blur(5px)'
      }}>
        <div style={{ maxWidth: '1280px', margin: '0 auto', display: 'flex', justifyContent: 'space-around', gap: '2rem', flexWrap: 'wrap' }}>
          {[
            { num: "35+", label: "Learning Modules" },
            { num: "20", label: "Interactive Challenges" },
            { num: "24/7", label: "Self-Paced Learning" },
            { num: "∞", label: "Free for Everyone" },
          ].map((stat, i) => (
            <div key={stat.label} className={`animate-fade-in-up stagger-${i + 1}`} style={{ textAlign: 'center' }}>
              <div style={{ fontSize: '3rem', fontWeight: 900 }} className="gradient-text">{stat.num}</div>
              <div style={{ color: 'var(--text-muted)', fontWeight: 600, marginTop: '0.5rem', textTransform: 'uppercase', letterSpacing: '0.1em', fontSize: '0.8rem' }}>{stat.label}</div>
            </div>
          ))}
        </div>
      </section>

      {/* ── Features ── */}
      <section style={{ padding: '8rem 1.5rem', maxWidth: '1280px', margin: '0 auto' }}>
        <div style={{ textAlign: 'center', marginBottom: '5rem' }}>
          <h2 className="gradient-text" style={{ fontSize: '1rem', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.2em', marginBottom: '1rem' }}>Feature Breakdown</h2>
          <h3 style={{ fontSize: '3rem', fontWeight: 800 }}>Engineered for <span className="gradient-text">Clarity</span></h3>
        </div>

        <div style={{
          display: 'grid',
          gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))',
          gap: '2rem',
        }}>
          {FEATURES.map((f, i) => (
            <div key={f.title} className="glass-card" style={{
              padding: '3rem 2rem',
              borderRadius: '24px',
              border: '1px solid rgba(255,255,255,0.05)',
            }}>
              <div style={{
                width: '60px',
                height: '60px',
                borderRadius: '16px',
                background: 'rgba(99, 102, 241, 0.1)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '2rem',
                marginBottom: '1.5rem'
              }}>{f.icon}</div>
              <h4 style={{ fontSize: '1.5rem', fontWeight: 800, marginBottom: '1rem' }}>{f.title}</h4>
              <p style={{ color: 'var(--text-secondary)', fontSize: '1.05rem', lineHeight: 1.6 }}>{f.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* ── Curriculum Preview ── */}
      <section style={{ padding: '4rem 1.5rem 10rem', maxWidth: '1280px', margin: '0 auto' }}>
        <div style={{
          background: 'linear-gradient(135deg, rgba(99, 102, 241, 0.1) 0%, rgba(236, 72, 153, 0.05) 100%)',
          borderRadius: '40px',
          padding: '5rem 3rem',
          border: '1px solid var(--border-subtle)',
          textAlign: 'center',
          position: 'relative',
          overflow: 'hidden'
        }}>
          <div style={{ position: 'absolute', top: '-10%', right: '-5%', width: '300px', height: '300px', background: 'var(--accent-primary)', filter: 'blur(100px)', opacity: 0.1 }} />

          <h2 style={{ fontSize: '3rem', fontWeight: 800, marginBottom: '1.5rem' }}>Ready to start your journey?</h2>
          <p style={{ color: 'var(--text-secondary)', fontSize: '1.2rem', maxWidth: '600px', margin: '0 auto 3rem' }}>
            Join developers mastering algorithms with our structured curriculum.
          </p>

          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fill, minmax(280px, 1fr))',
            gap: '1.5rem',
            marginBottom: '4rem'
          }}>
            {TOPICS_PREVIEW.map((topic) => (
              <div key={topic.name} className="glass-card" style={{ padding: '1.5rem', textAlign: 'left', borderRadius: '16px' }}>
                <div style={{ color: topic.color, fontWeight: 800, fontSize: '0.8rem', marginBottom: '0.5rem', textTransform: 'uppercase' }}>{topic.level}</div>
                <div style={{ fontWeight: 700, fontSize: '1.1rem', marginBottom: '0.25rem' }}>{topic.name}</div>
                <div style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>{topic.complexity}</div>
              </div>
            ))}
          </div>

          <Link href="/learn" className="btn-primary" style={{ fontSize: '1.2rem', padding: '1.25rem 3rem', borderRadius: '100px' }}>
            Explore the Curriculum
          </Link>
        </div>
      </section>
    </div>
  );
}
