## index.html — Project Hub Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Project Name] — DesignXI</title>
  <link href="https://fonts.googleapis.com/css2?family=[Font]:wght@400;600;700&family=Tajawal:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* [Paste shared CSS here] */
    .hub-container { max-width: 960px; margin: 0 auto; padding: var(--space-12) var(--space-6); }
    .project-header { text-align: center; margin-bottom: var(--space-12); }
    .project-badge { display: inline-block; background: var(--color-primary); color: white; padding: 4px 12px; border-radius: var(--radius-pill); font-size: var(--text-caption); font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: var(--space-4); }
    .project-title { font-size: var(--text-display); font-weight: 700; margin-bottom: var(--space-3); }
    .project-subtitle { font-size: var(--text-body-lg); color: var(--color-text-secondary); max-width: 600px; margin: 0 auto; }
    .phases-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: var(--space-4); margin-bottom: var(--space-12); }
    .phase-card { background: white; border-radius: var(--radius-lg); padding: var(--space-6); box-shadow: var(--shadow-sm); border: 1px solid var(--color-border); }
    .phase-number { font-size: var(--text-caption); font-weight: 700; color: var(--color-primary); text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: var(--space-2); }
    .phase-name { font-size: var(--text-h4); font-weight: 600; margin-bottom: var(--space-2); }
    .phase-desc { font-size: var(--text-body-sm); color: var(--color-text-secondary); }
    .nav-cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: var(--space-4); }
    .nav-card { background: white; border-radius: var(--radius-lg); padding: var(--space-6); box-shadow: var(--shadow-sm); text-decoration: none; color: inherit; border: 2px solid transparent; transition: all 0.2s; display: flex; flex-direction: column; align-items: flex-start; }
    .nav-card:hover { border-color: var(--color-primary); box-shadow: var(--shadow-md); transform: translateY(-2px); }
    .nav-card-icon { font-size: 2rem; margin-bottom: var(--space-3); }
    .nav-card-title { font-size: var(--text-h4); font-weight: 600; margin-bottom: var(--space-2); }
    .nav-card-desc { font-size: var(--text-body-sm); color: var(--color-text-secondary); }
    .section-label { font-size: var(--text-body-sm); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--color-text-tertiary); margin-bottom: var(--space-4); }
  </style>
</head>
<body>
  <div class="lang-switcher">
    <button class="lang-btn active" onclick="setLang('en', this)">English</button>
    <button class="lang-btn" onclick="setLang('ar', this)">العربية</button>
  </div>
  <div id="content-en" class="lang-block">
    <div class="hub-container">
      <header class="project-header">
        <div class="project-badge">DesignXI Project</div>
        <h1 class="project-title">[Project Name]</h1>
        <p class="project-subtitle">[One sentence describing the product and audience]</p>
      </header>
      <p class="section-label">Process Overview</p>
      <div class="phases-grid">
        <div class="phase-card"><div class="phase-number">Phase 1</div><div class="phase-name">Discovery</div><div class="phase-desc">[Key finding]</div></div>
        <div class="phase-card"><div class="phase-number">Phase 2</div><div class="phase-name">Research</div><div class="phase-desc">[X interviews, X survey responses, X competitors analyzed]</div></div>
        <div class="phase-card"><div class="phase-number">Phase 3</div><div class="phase-name">Define</div><div class="phase-desc">[X personas, journey map, HMW statements]</div></div>
        <div class="phase-card"><div class="phase-number">Phase 4</div><div class="phase-name">Ideate</div><div class="phase-desc">[X screens, X user flows, card sorting complete]</div></div>
        <div class="phase-card"><div class="phase-number">Phase 5</div><div class="phase-name">UI Design</div><div class="phase-desc">[Design school, color system, X screens]</div></div>
        <div class="phase-card"><div class="phase-number">Phase 6</div><div class="phase-name">Testing</div><div class="phase-desc">[X usability sessions, X issues fixed]</div></div>
      </div>
      <p class="section-label" style="margin-top:var(--space-12);">Deliverables</p>
      <div class="nav-cards">
        <a href="casestudy.html" class="nav-card"><div class="nav-card-icon">📖</div><div class="nav-card-title">Case Study</div><div class="nav-card-desc">Full story from problem to solution</div></a>
        <a href="screens.html" class="nav-card"><div class="nav-card-icon">📱</div><div class="nav-card-title">UI Screens</div><div class="nav-card-desc">Interactive prototype — all flows</div></a>
        <a href="personas.html" class="nav-card"><div class="nav-card-icon">👤</div><div class="nav-card-title">Personas</div><div class="nav-card-desc">Who we designed for</div></a>
        <a href="process.html" class="nav-card"><div class="nav-card-icon">🧠</div><div class="nav-card-title">UX Process</div><div class="nav-card-desc">Thinking behind decisions</div></a>
        <a href="handoff.html" class="nav-card"><div class="nav-card-icon">⚙️</div><div class="nav-card-title">Dev Handoff</div><div class="nav-card-desc">Specs for developers</div></a>
      </div>
    </div>
  </div>
  <div id="content-ar" class="lang-block" style="display:none;" dir="rtl">
    <!-- Arabic version of index.html -->
  </div>
  <script>
  function setLang(lang, btn) {
    document.querySelectorAll('.lang-block').forEach(el => el.style.display = 'none');
    document.getElementById('content-' + lang).style.display = 'block';
    document.querySelectorAll('.lang-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
  }
  </script>
</body>
</html>
```

---

