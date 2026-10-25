## frd.html — Functional Requirements Document Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>[Project Name] — FRD</title>
  <link href="https://fonts.googleapis.com/css2?family=[Font]:wght@400;500;600;700&family=Tajawal:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* [Paste shared CSS tokens here] */
    .frd-wrapper { max-width: 960px; margin: 0 auto; padding: var(--space-8) var(--space-6) var(--space-20); }
    .frd-header { border-bottom: 3px solid var(--color-primary); padding-bottom: var(--space-6); margin-bottom: var(--space-8); }
    .frd-doc-title { font-size: var(--text-display); font-weight: 700; margin-bottom: var(--space-3); }
    .frd-meta { display: flex; flex-wrap: wrap; gap: var(--space-6); font-size: var(--text-body-sm); color: var(--color-text-secondary); }
    .frd-meta-item strong { color: var(--color-text-primary); }
    .frd-status {
      display: inline-block; padding: 4px 14px; border-radius: var(--radius-pill);
      font-size: var(--text-caption); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em;
    }
    .status-draft { background: #FFFBEB; color: #D97706; }
    .status-review { background: #EFF6FF; color: #2563EB; }
    .status-approved { background: #F0FDF4; color: #16A34A; }

    /* TOC */
    .frd-toc { background: var(--color-bg-card); border: 1px solid var(--color-border); border-radius: var(--radius-lg); padding: var(--space-6); margin-bottom: var(--space-8); }
    .frd-toc-title { font-size: var(--text-body-sm); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--color-text-tertiary); margin-bottom: var(--space-4); }
    .frd-toc ol { list-style: decimal; padding-left: var(--space-6); }
    .frd-toc li { padding: var(--space-2) 0; }
    .frd-toc a { color: var(--color-primary); text-decoration: none; font-size: var(--text-body-sm); font-weight: 500; }
    .frd-toc a:hover { text-decoration: underline; }

    /* Section */
    .frd-section { margin-top: var(--space-12); padding-top: var(--space-6); border-top: 2px solid var(--color-border); }
    .frd-section-label { font-size: var(--text-caption); font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: var(--color-primary); margin-bottom: var(--space-2); }
    .frd-section-title { font-size: var(--text-h2); font-weight: 700; margin-bottom: var(--space-6); }
    .frd-subsection { margin-top: var(--space-8); }
    .frd-subsection-title { font-size: var(--text-h4); font-weight: 700; margin-bottom: var(--space-4); color: var(--color-text-primary); }
    .frd-body { font-size: var(--text-body); color: var(--color-text-secondary); line-height: 1.7; margin-bottom: var(--space-4); }

    /* FRD Table */
    .frd-table { width: 100%; border-collapse: collapse; font-size: var(--text-body-sm); margin: var(--space-4) 0; }
    .frd-table th { background: var(--color-primary); color: white; padding: var(--space-3) var(--space-4); text-align: left; font-weight: 600; }
    [dir="rtl"] .frd-table th { text-align: right; }
    .frd-table td { padding: var(--space-3) var(--space-4); border-bottom: 1px solid var(--color-border); color: var(--color-text-secondary); vertical-align: top; }
    .frd-table tr:nth-child(even) td { background: var(--color-bg-page); }

    /* FR Requirement */
    .fr-block { background: var(--color-bg-card); border: 1px solid var(--color-border); border-radius: var(--radius-lg); margin-bottom: var(--space-3); overflow: hidden; }
    .fr-id { display: inline-block; background: var(--color-primary); color: white; padding: 4px 12px; font-size: var(--text-caption); font-weight: 700; font-family: monospace; border-radius: var(--radius-pill); margin-right: var(--space-3); flex-shrink: 0; }
    .fr-row { display: flex; align-items: flex-start; padding: var(--space-4) var(--space-5); gap: var(--space-3); }
    .fr-text { font-size: var(--text-body-sm); color: var(--color-text-primary); line-height: 1.6; flex: 1; }
    .fr-priority { display: inline-block; padding: 2px 8px; border-radius: var(--radius-pill); font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.06em; flex-shrink: 0; }
    .fr-shall { background: #FEF2F2; color: #DC2626; }
    .fr-should { background: #FFFBEB; color: #D97706; }
    .fr-module-header { background: var(--color-primary-subtle); padding: var(--space-3) var(--space-5); border-bottom: 1px solid var(--color-border); font-size: var(--text-caption); font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: var(--color-primary); }

    /* UAT Table */
    .uat-pass { color: #16A34A; font-weight: 700; }
    .uat-fail { color: #DC2626; font-weight: 700; }
    .uat-pending { color: var(--color-text-tertiary); }
    .uat-checkbox { width: 20px; height: 20px; border: 2px solid var(--color-border); border-radius: 4px; display: inline-block; }

    /* Sign-off */
    .signoff-table { width: 100%; border-collapse: collapse; }
    .signoff-table th { background: var(--gray-100); padding: var(--space-3) var(--space-4); text-align: left; font-size: var(--text-body-sm); font-weight: 700; border: 1px solid var(--color-border); }
    .signoff-table td { padding: var(--space-4) var(--space-4); border: 1px solid var(--color-border); height: 48px; font-size: var(--text-body-sm); color: var(--color-text-secondary); }
  </style>
</head>
<body>
<div class="lang-switcher">
  <button class="lang-btn active" onclick="setLang('en', this)">English</button>
  <button class="lang-btn" onclick="setLang('ar', this)">العربية</button>
</div>

<div id="content-en" class="lang-block">
<div class="frd-wrapper">

  <!-- ─── DOCUMENT HEADER ─── -->
  <div class="frd-header">
    <div style="display:flex; align-items:center; gap:var(--space-3); margin-bottom:var(--space-3);">
      <span class="frd-status status-draft">Draft</span>
      <!-- status-draft / status-review / status-approved -->
      <span style="font-size:var(--text-caption); color:var(--color-text-tertiary);">v[1.0] · [DD/MM/YYYY]</span>
    </div>
    <div class="frd-doc-title">[Project Name] — Functional Requirements Document</div>
    <div class="frd-meta">
      <div class="frd-meta-item"><strong>Author:</strong> [Name, Role]</div>
      <div class="frd-meta-item"><strong>Based on BRD:</strong> v[X.X] dated [DD/MM/YYYY]</div>
      <div class="frd-meta-item"><strong>Platform:</strong> [iOS / Android / Web]</div>
      <div class="frd-meta-item"><strong>Review deadline:</strong> [DD/MM/YYYY]</div>
    </div>
  </div>

  <!-- ─── TABLE OF CONTENTS ─── -->
  <div class="frd-toc">
    <div class="frd-toc-title">Table of Contents</div>
    <ol>
      <li><a href="#overview">Overview / Objective</a></li>
      <li><a href="#scope">Scope</a></li>
      <li><a href="#user-roles">User Roles</a></li>
      <li><a href="#user-flows">User Flows</a></li>
      <li><a href="#functional-requirements">Functional Requirements</a></li>
      <li><a href="#pages-screens">Pages / Screens</a></li>
      <li><a href="#integrations">Integrations</a></li>
      <li><a href="#data-handling">Data Handling</a></li>
      <li><a href="#business-rules">Business Rules</a></li>
      <li><a href="#error-handling">Error Handling</a></li>
      <li><a href="#responsiveness">Responsiveness</a></li>
      <li><a href="#permissions-security">Permissions & Security</a></li>
      <li><a href="#kpis">KPIs / Success Metrics</a></li>
      <li><a href="#uat">UAT — Acceptance Test Cases</a></li>
      <li><a href="#signoff">Sign-off</a></li>
    </ol>
  </div>

  <!-- ─── 1. OVERVIEW ─── -->
  <div id="overview" class="frd-section">
    <div class="frd-section-label">Section 1</div>
    <h2 class="frd-section-title">Overview / Objective</h2>
    <p class="frd-body">[2-3 sentences: What this FRD specifies, what system it covers, and what decision or build phase it supports.]</p>
    <p class="frd-body"><strong>Out of scope:</strong> [What is explicitly excluded from this version — be precise]</p>
  </div>

  <!-- ─── 2. SCOPE ─── -->
  <div id="scope" class="frd-section">
    <div class="frd-section-label">Section 2</div>
    <h2 class="frd-section-title">Scope</h2>
    <div class="cs-2col">
      <div class="cs-card">
        <div class="cs-card-title" style="margin-bottom:var(--space-3);">✅ In Scope</div>
        <ul style="list-style:none; font-size:var(--text-body-sm); color:var(--color-text-secondary);">
          <li style="padding:6px 0; border-bottom:1px solid var(--color-border);">✦ [Module or feature 1]</li>
          <li style="padding:6px 0; border-bottom:1px solid var(--color-border);">✦ [Module or feature 2]</li>
          <li style="padding:6px 0;">✦ [Module or feature 3]</li>
        </ul>
      </div>
      <div class="cs-card">
        <div class="cs-card-title" style="margin-bottom:var(--space-3);">❌ Out of Scope (v1)</div>
        <ul style="list-style:none; font-size:var(--text-body-sm); color:var(--color-text-secondary);">
          <li style="padding:6px 0; border-bottom:1px solid var(--color-border);">✦ [Feature deferred to v2]</li>
          <li style="padding:6px 0; border-bottom:1px solid var(--color-border);">✦ [Integration not included]</li>
          <li style="padding:6px 0;">✦ [Platform excluded]</li>
        </ul>
      </div>
    </div>
    <div class="cs-card" style="margin-top:var(--space-4);">
      <div class="cs-card-title" style="margin-bottom:var(--space-3);">⚠️ Assumptions</div>
      <ul style="list-style:none; font-size:var(--text-body-sm); color:var(--color-text-secondary);">
        <li style="padding:6px 0; border-bottom:1px solid var(--color-border);">✦ [Technical assumption]</li>
        <li style="padding:6px 0; border-bottom:1px solid var(--color-border);">✦ [Business assumption]</li>
        <li style="padding:6px 0;">✦ [Design assumption]</li>
      </ul>
    </div>
  </div>

  <!-- ─── 3. USER ROLES ─── -->
  <div id="user-roles" class="frd-section">
    <div class="frd-section-label">Section 3</div>
    <h2 class="frd-section-title">User Roles</h2>
    <table class="frd-table">
      <thead><tr><th>Role</th><th>Description</th><th>Access Level</th><th>Key Permissions</th></tr></thead>
      <tbody>
        <tr><td><strong>Guest</strong></td><td>Unauthenticated visitor</td><td>Public</td><td>Browse, view, search</td></tr>
        <tr><td><strong>Registered User</strong></td><td>Authenticated customer</td><td>Standard</td><td>All guest + checkout, profile, history</td></tr>
        <tr><td><strong>Admin</strong></td><td>Internal team member</td><td>Full</td><td>All + manage products, users, reports</td></tr>
        <tr><td><strong>[Custom Role]</strong></td><td>[Description]</td><td>[Level]</td><td>[Permissions]</td></tr>
      </tbody>
    </table>
  </div>

  <!-- ─── 4. USER FLOWS ─── -->
  <div id="user-flows" class="frd-section">
    <div class="frd-section-label">Section 4</div>
    <h2 class="frd-section-title">User Flows</h2>
    <p class="frd-body">Each flow maps to UI screens and functional requirements for full traceability.</p>
    <table class="frd-table">
      <thead><tr><th>Flow ID</th><th>Flow Name</th><th>Trigger</th><th>Happy Path End State</th><th>FR References</th></tr></thead>
      <tbody>
        <tr><td><strong>UF-01</strong></td><td>Registration & Onboarding</td><td>User opens app</td><td>User lands on Home</td><td>FR-AUTH-01, 02</td></tr>
        <tr><td><strong>UF-02</strong></td><td>Browse & Search</td><td>User taps Search</td><td>Results shown</td><td>FR-SEARCH-01 thru 04</td></tr>
        <tr><td><strong>UF-03</strong></td><td>[Core Transaction]</td><td>User initiates [X]</td><td>Success confirmation</td><td>FR-[MOD]-01 thru 05</td></tr>
        <tr><td><strong>UF-04</strong></td><td>Profile Management</td><td>User opens Profile</td><td>Settings updated</td><td>FR-AUTH-06</td></tr>
      </tbody>
    </table>
  </div>

  <!-- ─── 5. FUNCTIONAL REQUIREMENTS ─── -->
  <div id="functional-requirements" class="frd-section">
    <div class="frd-section-label">Section 5</div>
    <h2 class="frd-section-title">Functional Requirements</h2>
    <p class="frd-body">Format: FR-[MODULE]-[N]. "Shall" = mandatory. "Should" = preferred. Every requirement is testable.</p>

    <!-- Auth Module -->
    <div class="fr-block">
      <div class="fr-module-header">🔐 Authentication</div>
      <div class="fr-row"><span class="fr-id">FR-AUTH-01</span><span class="fr-text">The system <strong>shall</strong> allow users to register with email and password.</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-AUTH-02</span><span class="fr-text">The system <strong>shall</strong> validate email format inline (not only on submit).</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-AUTH-03</span><span class="fr-text">The system <strong>shall</strong> send a verification email within 60 seconds of registration.</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-AUTH-04</span><span class="fr-text">The system <strong>shall</strong> lock account after 5 consecutive failed login attempts for 30 minutes.</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-AUTH-05</span><span class="fr-text">The system <strong>should</strong> support Sign in with Google and Apple (OAuth 2.0).</span><span class="fr-priority fr-should">SHOULD</span></div>
    </div>

    <!-- Core Feature Module — repeat pattern -->
    <div class="fr-block">
      <div class="fr-module-header">⚡ [Core Feature Module]</div>
      <div class="fr-row"><span class="fr-id">FR-[MOD]-01</span><span class="fr-text">[Requirement — use "shall" for mandatory, testable criterion]</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-[MOD]-02</span><span class="fr-text">[Requirement with measurable criterion — e.g., "within 2 seconds"]</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-[MOD]-03</span><span class="fr-text">[Preferred behavior]</span><span class="fr-priority fr-should">SHOULD</span></div>
    </div>

    <!-- Search Module -->
    <div class="fr-block">
      <div class="fr-module-header">🔍 Search</div>
      <div class="fr-row"><span class="fr-id">FR-SEARCH-01</span><span class="fr-text">The system <strong>shall</strong> return results within 1.5 seconds for any query.</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-SEARCH-02</span><span class="fr-text">The system <strong>shall</strong> support Arabic and English search queries equally.</span><span class="fr-priority fr-shall">SHALL</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">FR-SEARCH-03</span><span class="fr-text">The system <strong>shall</strong> display a "No results" state with alternative suggestions when empty.</span><span class="fr-priority fr-shall">SHALL</span></div>
    </div>
    <!-- Add more modules as needed: Notifications, Payment, Admin, etc. -->
  </div>

  <!-- ─── 6. PAGES / SCREENS ─── -->
  <div id="pages-screens" class="frd-section">
    <div class="frd-section-label">Section 6</div>
    <h2 class="frd-section-title">Pages / Screens</h2>
    <table class="frd-table">
      <thead><tr><th>Screen ID</th><th>Screen Name</th><th>Route / Path</th><th>User Roles</th><th>FR References</th></tr></thead>
      <tbody>
        <tr><td><strong>SCR-01</strong></td><td>Splash / Onboarding</td><td>/onboarding</td><td>Guest</td><td>FR-AUTH-01</td></tr>
        <tr><td><strong>SCR-02</strong></td><td>Login</td><td>/login</td><td>Guest</td><td>FR-AUTH-02, 03, 04, 05</td></tr>
        <tr><td><strong>SCR-03</strong></td><td>Register</td><td>/register</td><td>Guest</td><td>FR-AUTH-01, 02</td></tr>
        <tr><td><strong>SCR-04</strong></td><td>Home / Dashboard</td><td>/home</td><td>User</td><td>FR-[MOD]-01</td></tr>
        <tr><td><strong>SCR-05</strong></td><td>Search Results</td><td>/search</td><td>All</td><td>FR-SEARCH-01, 02, 03</td></tr>
        <tr><td><strong>SCR-06</strong></td><td>Profile</td><td>/profile</td><td>User</td><td>FR-AUTH-06</td></tr>
        <tr><td><strong>SCR-07</strong></td><td>Error / 404</td><td>/error</td><td>All</td><td>FR-ERR-01</td></tr>
        <!-- Add all screens -->
      </tbody>
    </table>
  </div>

  <!-- ─── 7. INTEGRATIONS ─── -->
  <div id="integrations" class="frd-section">
    <div class="frd-section-label">Section 7</div>
    <h2 class="frd-section-title">Integrations</h2>
    <table class="frd-table">
      <thead><tr><th>ID</th><th>Service</th><th>Type</th><th>Purpose</th><th>Auth Method</th><th>Fallback</th></tr></thead>
      <tbody>
        <tr><td><strong>INT-01</strong></td><td>[Payment GW]</td><td>REST API</td><td>Process payments</td><td>API Key + HMAC</td><td>Show manual payment option</td></tr>
        <tr><td><strong>INT-02</strong></td><td>Firebase</td><td>SDK</td><td>Push notifications</td><td>Service Account</td><td>In-app notification only</td></tr>
        <tr><td><strong>INT-03</strong></td><td>[SMS Provider]</td><td>REST API</td><td>OTP verification</td><td>Bearer Token</td><td>Email OTP fallback</td></tr>
        <tr><td><strong>INT-04</strong></td><td>[Analytics]</td><td>SDK</td><td>Event tracking</td><td>Client ID</td><td>Silent fail — no UX impact</td></tr>
      </tbody>
    </table>
  </div>

  <!-- ─── 8. DATA HANDLING ─── -->
  <div id="data-handling" class="frd-section">
    <div class="frd-section-label">Section 8</div>
    <h2 class="frd-section-title">Data Handling</h2>
    <table class="frd-table">
      <thead><tr><th>Field</th><th>Type</th><th>Required</th><th>Validation</th><th>Stored</th><th>Encrypted</th><th>Retention</th></tr></thead>
      <tbody>
        <tr><td>user_email</td><td>String</td><td>Yes</td><td>RFC 5322</td><td>DB</td><td>Yes</td><td>Until deletion</td></tr>
        <tr><td>user_password</td><td>String</td><td>Yes</td><td>Min 8 chars</td><td>DB</td><td>Bcrypt</td><td>Until deletion</td></tr>
        <tr><td>[field_name]</td><td>[type]</td><td>[Y/N]</td><td>[Rule]</td><td>[DB/Cache/None]</td><td>[Y/N]</td><td>[Duration]</td></tr>
      </tbody>
    </table>
    <p class="frd-body" style="margin-top:var(--space-4);"><strong>PII Policy:</strong> [Describe what counts as PII, where stored, who can access, GDPR/PDPL compliance approach]</p>
  </div>

  <!-- ─── 9. BUSINESS RULES ─── -->
  <div id="business-rules" class="frd-section">
    <div class="frd-section-label">Section 9</div>
    <h2 class="frd-section-title">Business Rules</h2>
    <div class="fr-block">
      <div class="fr-row"><span class="fr-id">BR-01</span><span class="fr-text">[Business rule — plain language, unambiguous, traceable to BRD objective]</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">BR-02</span><span class="fr-text">[Business rule 2]</span></div>
      <div class="fr-row" style="border-top:1px solid var(--color-border);"><span class="fr-id">BR-03</span><span class="fr-text">[Business rule 3]</span></div>
    </div>
  </div>

  <!-- ─── 10. ERROR HANDLING ─── -->
  <div id="error-handling" class="frd-section">
    <div class="frd-section-label">Section 10</div>
    <h2 class="frd-section-title">Error Handling</h2>
    <table class="frd-table">
      <thead><tr><th>Error ID</th><th>Trigger</th><th>Message (EN)</th><th>Message (AR)</th><th>Recovery</th></tr></thead>
      <tbody>
        <tr><td><strong>ERR-01</strong></td><td>Network timeout</td><td>"Connection lost. Please retry."</td><td>"انقطع الاتصال. حاول مجدداً."</td><td>Retry button</td></tr>
        <tr><td><strong>ERR-02</strong></td><td>Invalid credentials</td><td>"Incorrect email or password."</td><td>"بيانات الدخول غير صحيحة."</td><td>Forgot password link</td></tr>
        <tr><td><strong>ERR-03</strong></td><td>Session expired</td><td>"Your session has expired."</td><td>"انتهت جلستك."</td><td>Redirect to login</td></tr>
        <tr><td><strong>ERR-04</strong></td><td>Payment failed</td><td>"Payment not processed. Try again."</td><td>"لم تتم العملية. أعد المحاولة."</td><td>Retry / Alt method</td></tr>
        <tr><td><strong>ERR-05</strong></td><td>Server error</td><td>"Something went wrong."</td><td>"حدث خطأ ما."</td><td>Support link</td></tr>
      </tbody>
    </table>
  </div>

  <!-- ─── 11. RESPONSIVENESS ─── -->
  <div id="responsiveness" class="frd-section">
    <div class="frd-section-label">Section 11</div>
    <h2 class="frd-section-title">Responsiveness</h2>
    <table class="frd-table">
      <thead><tr><th>Name</th><th>Width</th><th>Grid</th><th>Design Approach</th></tr></thead>
      <tbody>
        <tr><td>Mobile</td><td>320–479px</td><td>4 col</td><td>Single column, stacked components</td></tr>
        <tr><td>Tablet</td><td>480–767px</td><td>8 col</td><td>2-column layouts begin</td></tr>
        <tr><td>Desktop</td><td>1024px+</td><td>12 col</td><td>Full layout, max-width: 1440px</td></tr>
      </tbody>
    </table>
    <p class="frd-body" style="margin-top:var(--space-4);">All interactive elements: minimum <strong>44×44px</strong> touch target (WCAG 2.5.5). RTL layout tested at all breakpoints.</p>
  </div>

  <!-- ─── 12. PERMISSIONS & SECURITY ─── -->
  <div id="permissions-security" class="frd-section">
    <div class="frd-section-label">Section 12</div>
    <h2 class="frd-section-title">Permissions & Security</h2>
    <table class="frd-table">
      <thead><tr><th>Role</th><th>Read</th><th>Write</th><th>Delete</th><th>Admin Panel</th><th>User Data</th></tr></thead>
      <tbody>
        <tr><td><strong>Guest</strong></td><td>✓ Public</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td></tr>
        <tr><td><strong>User</strong></td><td>✓</td><td>✓ Own</td><td>✓ Own</td><td>✗</td><td>Own only</td></tr>
        <tr><td><strong>Admin</strong></td><td>✓</td><td>✓</td><td>✓</td><td>✓ Full</td><td>✓ Full</td></tr>
      </tbody>
    </table>
    <p class="frd-body" style="margin-top:var(--space-4);">Security standards: HTTPS enforced, OWASP Top 10 compliance, JWT (24h expiry), 2FA mandatory for admin accounts, no sensitive data in URLs.</p>
  </div>

  <!-- ─── 13. KPIS ─── -->
  <div id="kpis" class="frd-section">
    <div class="frd-section-label">Section 13</div>
    <h2 class="frd-section-title">KPIs / Success Metrics</h2>
    <table class="frd-table">
      <thead><tr><th>Category</th><th>Metric</th><th>Baseline</th><th>Target</th><th>Measurement</th></tr></thead>
      <tbody>
        <tr><td>Acquisition</td><td>Monthly downloads</td><td>—</td><td>[X,000]</td><td>App Store Connect</td></tr>
        <tr><td>Activation</td><td>Onboarding completion</td><td>—</td><td>&gt; 75%</td><td>Analytics funnel</td></tr>
        <tr><td>Engagement</td><td>DAU (Daily Active Users)</td><td>—</td><td>[X,000]</td><td>Analytics</td></tr>
        <tr><td>Retention</td><td>7-day retention</td><td>—</td><td>&gt; 40%</td><td>Cohort analysis</td></tr>
        <tr><td>Performance</td><td>Load time (p95)</td><td>—</td><td>&lt; 2s</td><td>Lighthouse</td></tr>
        <tr><td>Accessibility</td><td>WCAG 2.1 AA</td><td>—</td><td>100%</td><td>Audit</td></tr>
      </tbody>
    </table>
  </div>

  <!-- ─── 14. UAT ─── -->
  <div id="uat" class="frd-section">
    <div class="frd-section-label">Section 14</div>
    <h2 class="frd-section-title">UAT — Acceptance Test Cases</h2>
    <p class="frd-body">Environment: [Staging URL] · Period: [dates] · Testers: [names/roles] · Devices: [list]</p>
    <table class="frd-table">
      <thead><tr><th>UAT-ID</th><th>Screen</th><th>FR Ref</th><th>Scenario</th><th>Expected Result</th><th>Result</th></tr></thead>
      <tbody>
        <tr><td><strong>UAT-01</strong></td><td>SCR-02</td><td>FR-AUTH-01</td><td>Register with valid email</td><td>Account created, email sent &lt; 60s</td><td><span class="uat-checkbox"></span></td></tr>
        <tr><td><strong>UAT-02</strong></td><td>SCR-02</td><td>FR-AUTH-02</td><td>Invalid email format</td><td>Inline error shown immediately</td><td><span class="uat-checkbox"></span></td></tr>
        <tr><td><strong>UAT-03</strong></td><td>SCR-02</td><td>FR-AUTH-04</td><td>5 failed logins → lockout</td><td>Account locked, message shown</td><td><span class="uat-checkbox"></span></td></tr>
        <tr><td><strong>UAT-04</strong></td><td>SCR-05</td><td>FR-SEARCH-01</td><td>Arabic search &lt; 1.5s</td><td>Results within 1.5 seconds</td><td><span class="uat-checkbox"></span></td></tr>
        <tr><td><strong>UAT-05</strong></td><td>All</td><td>WCAG 2.1</td><td>Screen reader traversal</td><td>All elements announced correctly</td><td><span class="uat-checkbox"></span></td></tr>
        <!-- Add all UAT cases -->
      </tbody>
    </table>
  </div>

  <!-- ─── 15. SIGN-OFF ─── -->
  <div id="signoff" class="frd-section">
    <div class="frd-section-label">Section 15</div>
    <h2 class="frd-section-title">Sign-off</h2>
    <p class="frd-body">By signing below, each stakeholder confirms they have reviewed this FRD and approve it for development.</p>
    <table class="signoff-table">
      <thead><tr><th>Name</th><th>Role</th><th>Signature</th><th>Date</th><th>Status</th></tr></thead>
      <tbody>
        <tr><td>[Name]</td><td>Product Owner</td><td></td><td></td><td><span class="frd-status status-draft">Pending</span></td></tr>
        <tr><td>[Name]</td><td>UX Lead</td><td></td><td></td><td><span class="frd-status status-draft">Pending</span></td></tr>
        <tr><td>[Name]</td><td>Tech Lead</td><td></td><td></td><td><span class="frd-status status-draft">Pending</span></td></tr>
        <tr><td>[Name]</td><td>QA Lead</td><td></td><td></td><td><span class="frd-status status-draft">Pending</span></td></tr>
      </tbody>
    </table>
  </div>

  <!-- Nav back -->
  <div style="margin-top:var(--space-20); text-align:center; border-top:1px solid var(--color-border); padding-top:var(--space-8);">
    <a href="index.html" style="color:var(--color-primary); font-weight:600; text-decoration:none;">← Back to Project Hub</a>
  </div>

</div>
</div>

<!-- Arabic version -->
<div id="content-ar" class="lang-block" style="display:none;" dir="rtl">
  <div class="frd-wrapper">
    <!-- [Exact same structure — all content fully translated to natural Arabic] -->
    <!-- Section labels, table headers, error messages, and requirement text all in Arabic -->
    <!-- Arabic error messages are already defined in Section 10 above — use them here -->
  </div>
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

