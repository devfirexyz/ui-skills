import { useMemo } from "react";

const TOKENS = {
  bg: "#f0f0e8",
  bgAlt: "#e8e8e0",
  fg: "#1a1a1a",
  fgMuted: "#888888",
  inverse: "#f0f0e8",
  border: "#1a1a1a",
  accent: "#2d5a2d",
  accentHover: "#3a6a3a",
  shadow: "#1a1a1a",
};

export default function MarketingLandingTemplate() {
  const vars = useMemo(
    () => ({
      "--background": TOKENS.bg,
      "--background-alt": TOKENS.bgAlt,
      "--foreground": TOKENS.fg,
      "--foreground-muted": TOKENS.fgMuted,
      "--foreground-inverse": TOKENS.inverse,
      "--border": TOKENS.border,
      "--accent": TOKENS.accent,
      "--accent-hover": TOKENS.accentHover,
      "--shadow-color": TOKENS.shadow,
    }),
    []
  );

  return (
    <main
      style={{
        ...vars,
        minHeight: "100vh",
        background: "var(--background)",
        color: "var(--foreground)",
        fontFamily: "'Geist Mono', ui-monospace, monospace",
      }}
    >
      <nav
        style={{
          position: "fixed",
          inset: "0 0 auto 0",
          zIndex: 20,
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          padding: "14px 24px",
          borderBottom: "2px solid var(--border)",
          background: "var(--background)",
        }}
      >
        <strong style={{ fontFamily: "'Geist', sans-serif", fontWeight: 900, fontSize: 22 }}>
          brand.
        </strong>
        <div style={{ display: "flex", gap: 18, alignItems: "center", fontWeight: 700, textTransform: "uppercase", fontSize: 12 }}>
          <a href="#features">Features</a>
          <a href="#pricing">Pricing</a>
          <a
            href="#cta"
            style={{
              border: "2px solid var(--border)",
              padding: "8px 14px",
              textDecoration: "none",
              color: "var(--foreground)",
            }}
          >
            Start
          </a>
        </div>
      </nav>

      <section
        style={{
          padding: "132px 24px 84px",
          borderBottom: "2px solid var(--border)",
        }}
      >
        <h1
          style={{
            fontFamily: "'Geist', sans-serif",
            fontWeight: 900,
            fontSize: "clamp(80px, 18vw, 220px)",
            lineHeight: 0.8,
            letterSpacing: "-0.05em",
          }}
        >
          brand
        </h1>

        <div style={{ marginTop: 32, display: "grid", gap: 16, maxWidth: 760 }}>
          <div
            style={{
              display: "inline-block",
              width: "fit-content",
              background: "var(--accent)",
              color: "var(--foreground-inverse)",
              border: "2px solid var(--border)",
              boxShadow: "8px 8px 0 0 var(--shadow-color)",
              transform: "rotate(-1.5deg)",
              padding: "12px 18px",
              fontFamily: "'Geist', sans-serif",
              fontWeight: 900,
              textTransform: "uppercase",
            }}
          >
            End-to-end AI music production.
          </div>
          <div
            style={{
              display: "inline-block",
              width: "fit-content",
              marginLeft: 24,
              background: "var(--foreground)",
              color: "var(--foreground-inverse)",
              border: "2px solid var(--border)",
              boxShadow: "8px 8px 0 0 var(--accent)",
              transform: "rotate(1deg)",
              padding: "12px 18px",
              fontFamily: "'Geist', sans-serif",
              fontWeight: 900,
              textTransform: "uppercase",
            }}
          >
            Less noise. More output.
          </div>
        </div>
      </section>

      <section id="features" style={{ borderBottom: "2px solid var(--border)" }}>
        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(220px, 1fr))" }}>
          {[
            ["01", "Prompt to Song"],
            ["02", "Auto Mastered"],
            ["03", "Cover Art"],
            ["04", "One-Click Release"],
          ].map(([n, title], i) => (
            <article
              key={title}
              style={{
                borderRight: i % 4 === 3 ? "none" : "2px solid var(--border)",
                borderBottom: "2px solid var(--border)",
                padding: 24,
              }}
            >
              <p style={{ fontWeight: 900, color: "var(--foreground-muted)", marginBottom: 18 }}>/{n}</p>
              <h3 style={{ fontFamily: "'Geist', sans-serif", fontWeight: 900, textTransform: "uppercase" }}>{title}</h3>
            </article>
          ))}
        </div>
      </section>

      <section id="cta" style={{ padding: "56px 24px", background: "var(--background-alt)" }}>
        <div style={{ maxWidth: 960, margin: "0 auto", border: "2px solid var(--border)", background: "var(--background)", boxShadow: "8px 8px 0 0 var(--shadow-color)", padding: 28 }}>
          <h2 style={{ fontFamily: "'Geist', sans-serif", fontWeight: 900, textTransform: "uppercase", fontSize: "clamp(28px, 5vw, 56px)", lineHeight: 0.9 }}>
            Ship your next track today.
          </h2>
          <button
            style={{
              marginTop: 20,
              border: "2px solid var(--border)",
              background: "var(--accent)",
              color: "var(--foreground-inverse)",
              boxShadow: "4px 4px 0 0 var(--shadow-color)",
              textTransform: "uppercase",
              fontWeight: 900,
              padding: "10px 16px",
            }}
          >
            Start free trial
          </button>
        </div>
      </section>
    </main>
  );
}
