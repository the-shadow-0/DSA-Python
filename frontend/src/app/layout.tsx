import type { Metadata } from "next";
import "./globals.css";
import Link from "next/link";

export const metadata: Metadata = {
  title: "DSA Python — Learn Data Structures & Algorithms",
  description: "Master DSA through visual explanations, Python implementations, and interactive challenges. From Big O to advanced algorithms.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <div className="mesh-bg">
          <div className="mesh-orb orb-1" />
          <div className="mesh-orb orb-2" />
          <div className="mesh-orb orb-3" />
          <div className="grid-overlay" />
        </div>
        {/* ── Navigation ── */}
        <nav style={{
          position: 'sticky',
          top: 0,
          zIndex: 50,
          background: 'rgba(10, 10, 26, 0.8)',
          backdropFilter: 'blur(16px)',
          borderBottom: '1px solid var(--border-subtle)',
          padding: '0.75rem 0',
        }}>
          <div style={{
            maxWidth: '1280px',
            margin: '0 auto',
            padding: '0 1.5rem',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'space-between',
          }}>
            {/* Logo */}
            <Link href="/" style={{ textDecoration: 'none', display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
              <div style={{
                width: '36px',
                height: '36px',
                borderRadius: '10px',
                background: 'linear-gradient(135deg, var(--accent-primary), var(--accent-secondary))',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontSize: '1.1rem',
              }}>⚡</div>
              <span style={{
                fontSize: '1.15rem',
                fontWeight: 700,
                color: 'var(--text-primary)',
              }}>DSA <span className="gradient-text">Python</span></span>
            </Link>

            {/* Nav Links */}
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.25rem' }}>
              <Link href="/learn" className="nav-link">Learn</Link>
              <Link href="/challenges" className="nav-link">Challenges</Link>
              <Link href="/visualizer" className="nav-link">Visualizer</Link>
              <Link href="/dashboard" className="nav-link">Dashboard</Link>
            </div>
          </div>
        </nav>

        {/* ── Main Content ── */}
        <main style={{ minHeight: 'calc(100vh - 120px)' }}>
          {children}
        </main>

        {/* ── Footer ── */}
        <footer style={{
          borderTop: '1px solid var(--border-subtle)',
          padding: '2rem 0',
          textAlign: 'center',
          color: 'var(--text-muted)',
          fontSize: '0.85rem',
        }}>
          <div style={{ maxWidth: '1280px', margin: '0 auto', padding: '0 1.5rem' }}>
            <p>Built with ❤️ for the developer community • Open Source • MIT License</p>
            <p style={{ marginTop: '0.5rem' }}>
              <Link href="https://github.com/the-shadow-0" style={{ color: 'var(--accent-primary)', textDecoration: 'none' }}>GitHub</Link>
              {' • '}
              <Link href="/learn" style={{ color: 'var(--accent-primary)', textDecoration: 'none' }}>Start Learning</Link>
            </p>
          </div>
        </footer>
      </body>
    </html>
  );
}
