# Product Delivery Reference — BRD → FRD → UAT → Launch

## Overview

This reference covers the full product delivery lifecycle that comes **after** UX/UI design is complete. A professional designer understands the entire pipeline — not just screens — because every phase shapes what gets designed, tested, and shipped.

```
Phase 8:  BRD  — Business Requirements Document
Phase 9:  FRD  — Functional Requirements Document
Phase 10: UI/UX Mapping — Connecting screens to requirements
Phase 11: UAT  — User Acceptance Testing
Phase 12: PIN  — Penetration & Security Testing
Phase 13: Staging — Pre-launch validation
Phase 14: Publishing — Go live
```

---

## Key Book References (from your library)

These books directly inform how to write requirements, test products, and think like a product designer — not just a visual designer:

| Book | Relevance |
|---|---|
| **Business Thinking for Designers** (10 - Career & Business) | How to speak the language of business stakeholders when writing BRDs |
| **Getting Real** (05 - Agile & Lean UX) | Why less documentation is more — write the minimum viable spec |
| **Lean UX** (05 - Agile & Lean UX) | Requirements as assumptions, validated by experiments |
| **The Elements of User Experience** — Jesse James Garrett (03 - UX Process) | The 5 planes: Strategy → Scope → Structure → Skeleton → Surface — maps directly to BRD/FRD structure |
| **UX for Product Managers** (03 - UX Process) | Bridging design intent and functional specification |
| **A Project Guide to UX Design** (03 - UX Process) | Complete project documentation methodology |
| **Don't Make Me Think** — Steve Krug (04 - UI Design) | Usability principles that become acceptance test criteria |
| **100 Things Every Designer Needs to Know** (01 - Psychology) | Cognitive principles that inform business rules and error handling |
| **Information Architecture** (09 - HCI) | IA principles that shape FRD navigation and content structure |
| **The UX Book** — Rex Hartson (03 - UX Process) | Formal UX evaluation methods → UAT foundations |
| **Handbook of Usability Testing** (02 - UX Research) | How to write and run acceptance tests |
| **Designing User Interfaces** — Malewicz (04 - UI Design) | UI component specifications that feed into FRD pages/screens section |

---

## Phase 8: BRD — Business Requirements Document

### What Is a BRD?
A BRD answers: **WHY are we building this?** It defines business goals, stakeholders, success metrics, and product vision — before any functional or design decisions are made. Written for executives and stakeholders, not developers.

> Reference: *Business Thinking for Designers* — "Designers who understand business outcomes design solutions that get approved and funded."

### BRD Template Structure

```
1. Executive Summary
2. Business Objective
3. Stakeholders
4. Product Overview — Main Products Showcase
5. Market & Competitive Context
6. Business Rules
7. Success Metrics / KPIs
8. Budget & Resources
9. Timeline Overview
10. Risk Assessment
11. Assumptions & Dependencies
```

---

### BRD Section: Product Overview — Main Products Showcase

**Purpose:** Show the core product offerings visually and functionally so all stakeholders align on what is being built before requirements are written.

```html
<!-- Product Showcase Card -->
<div class="product-showcase">
  <div class="product-item">
    <div class="product-icon">[icon or screenshot]</div>
    <div class="product-name">[Product / Feature Name]</div>
    <div class="product-desc">[One sentence: what it does and who uses it]</div>
    <div class="product-meta">
      <span class="product-tag">[Platform]</span>
      <span class="product-tag">[User Role]</span>
      <span class="product-tag">[Phase/Priority]</span>
    </div>
  </div>
</div>

/* CSS */
.product-showcase {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: var(--space-6);
  margin: var(--space-6) 0;
}
.product-item {
  background: var(--color-bg-card);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  box-shadow: var(--shadow-md);
  transition: transform 0.2s, box-shadow 0.2s;
}
.product-item:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
.product-icon { font-size: 40px; margin-bottom: var(--space-4); }
.product-name { font-size: var(--text-h4); font-weight: 700; margin-bottom: var(--space-2); }
.product-desc { font-size: var(--text-body-sm); color: var(--color-text-secondary); margin-bottom: var(--space-4); line-height: 1.6; }
.product-meta { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.product-tag {
  background: var(--color-primary-subtle);
  color: var(--color-primary);
  padding: 4px 10px;
  border-radius: var(--radius-pill);
  font-size: var(--text-caption);
  font-weight: 600;
}
```

### BRD Full HTML Template → `brd.html`

```html
<!-- brd.html structure -->
<!-- Sections: -->
<!-- 1. Header: Project name, version, date, status badge -->
<!-- 2. Executive Summary: 3-5 sentences, business problem + proposed solution -->
<!-- 3. Business Objectives: numbered list of measurable goals -->
<!-- 4. Stakeholders table: Name | Role | Responsibility | Sign-off required? -->
<!-- 5. Product Overview: Main Products Showcase (cards as above) -->
<!-- 6. Market & Competitive Context: summary from Phase 2 research -->
<!-- 7. Business Rules: numbered, unambiguous rules that constrain the product -->
<!-- 8. KPIs / Success Metrics table: Metric | Current | Target | How Measured -->
<!-- 9. Budget & Resources: team composition, tools, timeline -->
<!-- 10. Risk Register: Risk | Likelihood | Impact | Mitigation -->
<!-- 11. Sign-off section: Stakeholder signatures + date -->
```

---

## Phase 9: FRD — Functional Requirements Document

### What Is an FRD?
An FRD answers: **WHAT should the system do?** It translates business requirements into specific functional behaviors. Written for developers, QA engineers, and project managers.

> Reference: *The Elements of User Experience* — "Scope defines what features and functions will appear in the product. The FRD is the scope plane made explicit."

> Reference: *Getting Real* — "Write the smallest FRD that captures what truly matters. Every extra requirement is a liability."

### FRD Complete Section Breakdown

---

#### 9.1 Overview / Objective

```
Document Title:   [Product Name] — Functional Requirements Document
Version:          [1.0 / 1.1 / 2.0]
Date:             [DD/MM/YYYY]
Status:           [Draft / In Review / Approved]
Author:           [Name, Role]
Based on BRD:     [BRD version and date]

Objective:
[2-3 sentences: What this document specifies, what system it covers,
and what decision or build phase it supports.]

Out of Scope:
[List what is explicitly NOT covered in this FRD to prevent scope creep]
```

---

#### 9.2 Scope

```
In Scope:
  ✦ [Module or feature 1]
  ✦ [Module or feature 2]
  ✦ [User-facing functionality]
  ✦ [Admin/backend functionality if applicable]

Out of Scope (this version):
  ✦ [Feature deferred to v2]
  ✦ [Third-party integration not included yet]
  ✦ [Platform excluded from this release]

Assumptions:
  ✦ [Technical assumption — e.g., users have internet access]
  ✦ [Business assumption — e.g., payment gateway already contracted]
  ✦ [Design assumption — e.g., Arabic RTL supported by all components]
```

---

#### 9.3 User Roles

```html
<!-- User Roles table in HTML -->
<table class="frd-table">
  <thead>
    <tr>
      <th>Role</th>
      <th>Description</th>
      <th>Access Level</th>
      <th>Key Permissions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Guest</strong></td>
      <td>Unauthenticated visitor</td>
      <td>Public</td>
      <td>Browse, search, view product listings</td>
    </tr>
    <tr>
      <td><strong>Registered User</strong></td>
      <td>Authenticated customer</td>
      <td>Standard</td>
      <td>All guest permissions + checkout, order history, profile</td>
    </tr>
    <tr>
      <td><strong>Admin</strong></td>
      <td>Internal team member</td>
      <td>Full</td>
      <td>All user permissions + manage products, orders, users, reports</td>
    </tr>
    <tr>
      <td><strong>[Custom Role]</strong></td>
      <td>[Description]</td>
      <td>[Level]</td>
      <td>[Permissions]</td>
    </tr>
  </tbody>
</table>
```

---

#### 9.4 User Flows

```
[Reference the User Flow diagrams from Phase 4 (Ideate) here]
[Each major flow gets a flow ID for traceability to functional requirements]

Flow ID | Flow Name              | Trigger              | Happy Path End State
--------|------------------------|----------------------|------------------------
UF-01   | Registration & Onboard | User opens app       | User lands on Home
UF-02   | Browse & Search        | User taps Search     | Results shown
UF-03   | [Core Transaction]     | User initiates [X]   | Success confirmation
UF-04   | Profile Management     | User opens profile   | Settings updated
UF-05   | [Error Recovery]       | System error occurs  | User recovers gracefully

Each flow ID maps to: FR (Functional Requirement) + Screen ID + UAT Test Case
```

---

#### 9.5 Functional Requirements

```
Format: FR-[Module]-[Number]: [Requirement statement]
Each requirement must be: Specific, Measurable, Achievable, Testable

── Authentication ──────────────────────────────────────────
FR-AUTH-01: The system shall allow users to register with email + password
FR-AUTH-02: The system shall validate email format on input (not only on submit)
FR-AUTH-03: The system shall send verification email within 60 seconds of registration
FR-AUTH-04: The system shall support Sign in with Google / Apple (OAuth 2.0)
FR-AUTH-05: The system shall lock account after 5 failed login attempts for 30 minutes
FR-AUTH-06: Password must be minimum 8 characters, include uppercase, number, and symbol

── [Core Feature Module] ───────────────────────────────────
FR-[MOD]-01: [Requirement — use "shall" for mandatory, "should" for preferred]
FR-[MOD]-02: [Requirement]
FR-[MOD]-03: [Requirement with measurable criterion — e.g., "within 2 seconds"]

── Search ──────────────────────────────────────────────────
FR-SEARCH-01: The system shall return results within 1.5 seconds for any query
FR-SEARCH-02: The system shall support Arabic and English search queries
FR-SEARCH-03: The system shall display "No results found" with suggestions when empty
FR-SEARCH-04: The system shall highlight the matched term in search results

── Notifications ───────────────────────────────────────────
FR-NOTIF-01: The system shall send push notification for [event] within 30 seconds
FR-NOTIF-02: Users shall be able to opt out of each notification type individually

── [Add all modules relevant to the product] ───────────────
```

---

#### 9.6 Pages / Screens

```
Screen ID | Screen Name       | Route/Path         | User Roles | FR References
----------|-------------------|--------------------|------------|----------------
SCR-01    | Splash / Onboard  | /onboarding        | Guest      | FR-AUTH-01
SCR-02    | Login             | /login             | Guest      | FR-AUTH-02,03,04
SCR-03    | Register          | /register          | Guest      | FR-AUTH-01,02
SCR-04    | Home / Dashboard  | /home              | User       | FR-[MOD]-01
SCR-05    | Search Results    | /search            | All        | FR-SEARCH-01,02,03
SCR-06    | [Screen Name]     | /[path]            | [Role]     | [FR-IDs]
SCR-07    | Profile           | /profile           | User       | FR-AUTH-06
SCR-08    | Settings          | /settings          | User       | FR-NOTIF-02
SCR-09    | Admin Dashboard   | /admin             | Admin      | All admin FRs
SCR-10    | Error / 404       | /error             | All        | FR-ERR-01,02

Notes:
- Each screen gets a unique SCR-ID for traceability to design files and test cases
- Route/Path = actual URL or navigation path in the app
- Link each screen to the Figma frame or HTML prototype screen
```

---

#### 9.7 Integrations

```
Integration ID | Service        | Type       | Purpose                    | Auth Method
---------------|----------------|------------|----------------------------|------------
INT-01         | [Payment GW]   | REST API   | Process payments           | API Key + HMAC
INT-02         | Google Maps    | REST API   | Location & delivery track  | OAuth 2.0
INT-03         | Firebase       | SDK        | Push notifications         | Service Account
INT-04         | [SMS Provider] | REST API   | OTP verification           | Bearer Token
INT-05         | [Analytics]    | SDK        | Event tracking             | Client ID
INT-06         | [CDN]          | Storage    | Media upload & serving     | S3-compatible

For each integration document:
  ├── Base URL / endpoint
  ├── Authentication method
  ├── Rate limits
  ├── Error codes and how the UI handles each
  ├── Fallback behavior when integration is unavailable
  └── Test credentials for staging environment
```

---

#### 9.8 Data Handling

```
Data Field     | Type     | Required | Validation Rule          | Stored | Encrypted | Retention
---------------|----------|----------|--------------------------|--------|-----------|----------
user_email     | String   | Yes      | RFC 5322 format          | DB     | Yes       | Until deletion
user_password  | String   | Yes      | Min 8 chars, complexity  | DB     | Bcrypt    | Until deletion
phone_number   | String   | No       | E.164 format             | DB     | Yes       | Until deletion
order_id       | UUID     | Auto     | System generated         | DB     | No        | 7 years
location_data  | GeoJSON  | No       | Valid coordinates        | Cache  | No        | Session only
payment_token  | String   | Auto     | PCI-DSS tokenized        | No     | N/A       | Not stored

PII Data Policy:
  ✦ Personal data: [List what counts as PII in your product]
  ✦ Where it's stored: [Database, cloud region, backup policy]
  ✦ Who can access: [Role-based access definition]
  ✦ GDPR/PDPL compliance: [Right to be forgotten, data export]
  ✦ Arabic-speaking markets: Consider Saudi PDPL, UAE Federal Law
```

---

#### 9.9 Business Rules

```
Business rules are constraints that come from the business context — not from technical choices.
Format: BR-[Number]: [Rule in plain language]

BR-01: A user cannot place an order without completing identity verification
BR-02: Orders above [SAR X] must require 2FA authentication at checkout
BR-03: Delivery is only available within [geographic boundary]
BR-04: A product cannot be listed without an approved image (min 800×800px)
BR-05: Cancellation is only allowed within [X] minutes of order placement
BR-06: Admin accounts must require 2FA — no exceptions
BR-07: [Currency] display must follow Saudi/UAE formatting standards (right-aligned, Arabic numerals optional)
BR-08: [Add product-specific business rules derived from stakeholder interviews]

Rule source: Each BR should trace back to a BRD business objective or stakeholder requirement
```

---

#### 9.10 Error Handling

```
Error ID | Trigger                     | User-Facing Message (EN)           | User-Facing Message (AR)         | Recovery Action
---------|-----------------------------|------------------------------------|----------------------------------|----------------
ERR-01   | Network timeout             | "Connection lost. Please retry."   | "انقطع الاتصال. حاول مجدداً."   | Retry button
ERR-02   | Invalid login credentials   | "Incorrect email or password."     | "بيانات الدخول غير صحيحة."      | Forgot password link
ERR-03   | Session expired             | "Your session expired."            | "انتهت جلستك."                   | Redirect to login
ERR-04   | Payment failed              | "Payment not processed. Try again."| "لم تتم العملية. أعد المحاولة." | Retry / Alt method
ERR-05   | File too large              | "File exceeds [X]MB limit."        | "حجم الملف يتجاوز [X] ميجابايت."| Upload guidance
ERR-06   | Empty search results        | "No results for '[query]'"         | "لا نتائج لـ '[query]'"          | Suggestions shown
ERR-07   | Server error (500)          | "Something went wrong."            | "حدث خطأ ما."                    | Support link
ERR-08   | Rate limit hit              | "Too many requests. Wait [X]s."    | "طلبات كثيرة. انتظر [X] ثانية." | Auto-retry countdown

Rules:
  ✦ NEVER expose technical error codes to end users
  ✦ ALWAYS provide a recovery path — never a dead end
  ✦ ALWAYS support both Arabic and English error messages
  ✦ Log error codes internally with context (user ID, timestamp, route)
```

---

#### 9.11 Responsiveness

```
Breakpoint   | Name       | Width      | Grid    | Design Approach
-------------|------------|------------|---------|------------------
Mobile S     | xs         | 320–375px  | 4 col   | Single column, stacked
Mobile L     | sm         | 376–479px  | 4 col   | Single column
Tablet       | md         | 480–767px  | 8 col   | 2 col layouts begin
Tablet L     | lg         | 768–1023px | 8 col   | Sidebar patterns
Desktop      | xl         | 1024–1279px| 12 col  | Full desktop layout
Desktop Wide | 2xl        | 1280px+    | 12 col  | Max-width: 1440px, centered

Responsiveness Rules:
  ✦ All interactive elements: minimum 44×44px touch target (WCAG 2.5.5)
  ✦ Text must not overflow containers at any breakpoint
  ✦ Images must use responsive sizing (max-width: 100%)
  ✦ Tables must scroll horizontally on mobile (overflow-x: auto)
  ✦ Navigation must collapse to hamburger below [breakpoint]
  ✦ RTL layout must be tested at every breakpoint
  ✦ Keyboard navigation must work at all breakpoints
  ✦ No horizontal scrollbar on mobile viewport
```

---

#### 9.12 Permissions & Security

```
AUTHENTICATION:
  ✦ Session tokens: JWT, 24-hour expiry, refresh token 30 days
  ✦ OAuth 2.0 for social login (Google, Apple)
  ✦ 2FA: TOTP (Google Authenticator) or SMS OTP
  ✦ Brute force protection: lockout after 5 failed attempts

AUTHORIZATION (RBAC):
  Role        | Read | Write | Delete | Admin Panel | User Data
  ------------|------|-------|--------|-------------|----------
  Guest       |  ✓   |  ✗    |   ✗    |      ✗      |    ✗
  User        |  ✓   |  ✓    |  Own   |      ✗      |  Own only
  Moderator   |  ✓   |  ✓    |  ✓     |  Limited    |  View only
  Admin       |  ✓   |  ✓    |  ✓     |    Full     |  Full

SECURITY STANDARDS:
  ✦ HTTPS everywhere — no HTTP fallback
  ✦ OWASP Top 10 compliance (see Phase 12 — Penetration Testing)
  ✦ No sensitive data in URL parameters
  ✦ Input sanitization on ALL user inputs (XSS prevention)
  ✦ SQL injection prevention via parameterized queries
  ✦ CSRF tokens on all state-changing requests
  ✦ Content Security Policy (CSP) headers
  ✦ Dependency scanning (no known vulnerable packages)
  ✦ Secrets management: no hardcoded API keys in code
```

---

#### 9.13 KPIs / Success Metrics

```
Category          | Metric                          | Current Baseline | Target     | Measurement Method
------------------|---------------------------------|-----------------|------------|--------------------
Acquisition       | App downloads (monthly)         | —               | [X,000]    | App Store Connect / Play Console
Activation        | Onboarding completion rate      | —               | > 75%      | Analytics event tracking
Engagement        | Daily Active Users (DAU)        | —               | [X,000]    | Analytics
Engagement        | Session duration (avg)          | —               | > [X] min  | Analytics
Retention         | 7-day retention rate            | —               | > 40%      | Cohort analysis
Conversion        | [Core action] completion rate   | —               | > [X]%     | Funnel analytics
Revenue           | [Revenue metric]                | —               | [X] SAR/mo | Payment gateway reports
Performance       | App load time (p95)             | —               | < 2s       | Lighthouse / Firebase
Performance       | Crash-free session rate         | —               | > 99.5%    | Firebase Crashlytics
Satisfaction      | App Store rating                | —               | > 4.5 ★    | App Store / Play Store
Support           | Avg. support ticket resolution  | —               | < 24h      | CRM
Accessibility     | WCAG 2.1 AA compliance          | —               | 100%       | Automated + manual audit
```

---

## Phase 10: UI/UX Mapping

**Purpose:** Create an explicit link between design screens and functional requirements. Ensures nothing is designed that isn't required, and nothing required is undesigned.

```
Mapping Table:

Screen ID | Screen Name    | FR References              | UAT Test IDs  | Figma Frame / HTML Section
----------|----------------|----------------------------|---------------|---------------------------
SCR-01    | Onboarding     | FR-AUTH-01, FR-AUTH-02     | UAT-01, 02    | screens.html #onboarding
SCR-02    | Login          | FR-AUTH-03, 04, 05         | UAT-03, 04    | screens.html #login
SCR-03    | Home           | FR-[MOD]-01, 02            | UAT-05        | screens.html #home
SCR-04    | Search         | FR-SEARCH-01 thru 04       | UAT-06, 07    | screens.html #search
SCR-05    | [Screen]       | [FR IDs]                   | [UAT IDs]     | screens.html #[id]

Rules:
  ✦ Every FR must appear in at least one screen — if not, it's either missing a screen or an unnecessary requirement
  ✦ Every screen must reference at least one FR — if not, the screen has no specification
  ✦ Every screen must have UAT test coverage — no untested screens at launch
```

---

## Phase 11: UAT — User Acceptance Testing

> Reference: *Handbook of Usability Testing* (02 - UX Research) — structured approach to test case design
> Reference: *Don't Make Me Think* (04 - UI Design) — "Test with real users, not with assumptions"

### UAT Structure

```
UAT Plan:
  ├── Test Environment:  Staging URL / TestFlight / Internal track
  ├── Test Period:       [Start date] → [End date]
  ├── Testers:          [Internal / Beta users / Stakeholders]
  ├── Devices:          [iOS 16+, Android 12+, Chrome Desktop, Safari Desktop]
  └── Sign-off required: [Stakeholder names]
```

### UAT Test Case Format

```
UAT-ID  | Screen  | FR Ref      | Test Scenario                           | Steps                          | Expected Result                    | Pass/Fail
--------|---------|-------------|----------------------------------------|--------------------------------|------------------------------------|----------
UAT-01  | SCR-01  | FR-AUTH-01  | New user registers with valid email    | 1. Open app 2. Tap Register    | Account created, email sent < 60s  | [ ]
UAT-02  | SCR-01  | FR-AUTH-02  | Registration with invalid email format | Enter "notanemail"             | Inline error shown immediately     | [ ]
UAT-03  | SCR-02  | FR-AUTH-05  | 5 failed logins trigger lockout        | Fail login 5 times             | Account locked, message shown      | [ ]
UAT-04  | SCR-03  | FR-SEARCH-01| Arabic search returns results < 1.5s   | Type Arabic query              | Results appear within 1.5 seconds  | [ ]
UAT-05  | SCR-05  | FR-ERR-06   | Search with no results shows guidance  | Type nonsense query            | "No results" + suggestions shown   | [ ]
UAT-06  | All     | WCAG 2.1    | Screen reader reads all elements       | Use VoiceOver/TalkBack         | All elements announced correctly   | [ ]
UAT-07  | All     | BR-06       | Admin cannot login without 2FA         | Login as admin without 2FA    | 2FA prompt shown, cannot bypass    | [ ]
```

### UAT Acceptance Criteria

```
PASS conditions (must all be true before sign-off):
  ✦ All P0 (critical) test cases pass — 0 failures allowed
  ✦ All P1 (high) test cases pass — 0 failures allowed
  ✦ P2 (medium) test cases pass — max 5% failure with documented workaround
  ✦ No crashes on primary user flows
  ✦ RTL (Arabic) layout correct on all screens
  ✦ Performance: load time < 2s on 4G connection (Lighthouse ≥ 90)
  ✦ Accessibility: WCAG 2.1 AA — no critical violations
  ✦ Stakeholder sign-off obtained

FAIL conditions (block launch):
  ✦ Any P0 test fails
  ✦ Payment flow fails in any test
  ✦ Data loss or corruption observed
  ✦ Security vulnerability found
  ✦ Crash rate > 0.5% in testing
```

---

## Phase 12: Penetration Testing (PIN)

**Purpose:** Security testing to find vulnerabilities before real users and attackers do. A responsible product team runs pen tests before every public launch.

> Note: PIN = Penetration + Intrusion + Network. For UX designers, the goal is to understand what the pen test covers so you can design error states, security flows, and permission patterns correctly.

### OWASP Top 10 — What Gets Tested

```
#  | Vulnerability                    | Design Implication
---|----------------------------------|------------------------------------------
1  | Broken Access Control            | Role-based UI states — hide admin features from regular users
2  | Cryptographic Failures           | Password fields, data masking in UI
3  | Injection (SQL, XSS, etc.)       | Input validation UX, sanitized error messages
4  | Insecure Design                  | Security from Phase 9 — permissions, auth flows
5  | Security Misconfiguration        | No debug info in production error messages
6  | Vulnerable Components            | Dependency audit — not user-facing but essential
7  | Auth & Session Failures          | Login timeouts, session expiry UX, logout flows
8  | Data Integrity Failures          | Verification screens, confirmation dialogs
9  | Security Logging & Monitoring    | Audit logs — relevant for admin panels
10 | Server-Side Request Forgery      | URL input validation in any form
```

### Pen Test Checklist (Design-Relevant Items)

```
□ All forms sanitize input — no XSS possible
□ Error messages never reveal system internals (stack traces, DB info)
□ Session tokens not stored in localStorage (use httpOnly cookies)
□ Password fields: autocomplete="new-password" for new, "current-password" for login
□ Logout destroys session server-side (not just client-side)
□ Admin routes inaccessible to non-admin users (403, not redirect)
□ File upload: validates type and size server-side (not just client-side)
□ Sensitive actions (delete, payment) require re-authentication
□ API endpoints require auth — no public access to private data
□ Rate limiting on login, search, and all API endpoints
□ HTTPS enforced — no mixed content
□ No sensitive data in URL parameters or browser history
```

### Pen Test Report Structure

```
1. Executive Summary — risk level, critical findings count
2. Scope — what was tested (URLs, APIs, mobile app, admin panel)
3. Methodology — tools used (Burp Suite, OWASP ZAP, Nmap)
4. Findings:
   ├── Critical (CVSS 9.0–10.0): Fix before launch — no exceptions
   ├── High (CVSS 7.0–8.9):     Fix before launch
   ├── Medium (CVSS 4.0–6.9):   Fix within 30 days of launch
   └── Low (CVSS 0.1–3.9):      Track and fix in next sprint
5. Remediation Evidence — proof each critical/high item was fixed
6. Re-test Confirmation
```

---

## Phase 13: Staging

**Purpose:** Final validation in an environment that mirrors production exactly. Nothing goes to production that hasn't passed staging.

### Staging vs Production

```
Property           | Staging                    | Production
-------------------|----------------------------|------------------
URL                | staging.[domain].com       | [domain].com
Database           | Clone (anonymized data)    | Real data
Payment            | Sandbox / Test mode        | Live mode
Integrations       | Test credentials           | Live credentials
Push notifications | Test device tokens only    | All users
Analytics          | Separate property          | Production property
Access             | Internal team + QA only    | Public
SSL                | Valid cert required         | Valid cert required
```

### Staging Smoke Tests

```
Run these immediately after every deployment to staging:

□ App/site loads without errors
□ User registration creates account + sends email
□ Login works (email + social)
□ Core user flow completes end-to-end (UF-03: [your core transaction])
□ Payment flow processes in sandbox mode
□ Admin panel loads and is accessible only to admin role
□ Push notifications received on test device
□ Arabic (RTL) layout correct on all tested screens
□ Lighthouse score ≥ 90 (Performance, Accessibility, Best Practices)
□ No 4xx/5xx errors in browser console
□ No JS errors in browser console
□ App works on: iPhone (Safari), Android (Chrome), Desktop Chrome, Desktop Safari
□ All UAT test cases re-run on staging — pass rate required before production deploy
```

### Go / No-Go Checklist

```
GO conditions (all must be true):
  ✦ All smoke tests pass on staging
  ✦ All UAT pass conditions met
  ✦ Pen test: all Critical and High findings remediated and re-tested
  ✦ Performance: Lighthouse score ≥ 90
  ✦ Stakeholder UAT sign-off obtained
  ✦ App Store / Play Store assets ready (screenshots, description, keywords)
  ✦ Support team trained on the product
  ✦ Monitoring and alerting configured (Sentry, Firebase Crashlytics, etc.)
  ✦ Rollback plan documented

NO-GO conditions (any one blocks launch):
  ✗ Any P0 bug in staging
  ✗ Pen test critical vulnerability unresolved
  ✗ Core payment flow fails
  ✗ Data loss observed in testing
  ✗ Crash rate > 0.5%
  ✗ Missing stakeholder sign-off
```

---

## Phase 14: Publishing

### App Store (iOS — App Store Connect)

```
Required Assets:
  ├── App icon: 1024×1024px PNG (no alpha channel)
  ├── Screenshots: 6.7" (iPhone 14 Pro Max) + 12.9" iPad (if iPad supported)
  ├── Preview video: Optional but recommended (up to 30 seconds)
  ├── App name: Max 30 characters
  ├── Subtitle: Max 30 characters
  ├── Keywords: Max 100 characters (comma-separated)
  ├── Description: Max 4000 characters (first 3 lines are critical — above the fold)
  ├── Support URL: Must be live before submission
  └── Privacy Policy URL: Required (must describe data practices accurately)

Localization:
  ├── English (en-US): Primary
  └── Arabic (ar): Required if Arabic is primary language of product

Review Guidelines Checklist:
  □ No references to competing platforms
  □ All external links work
  □ No placeholder content in UI
  □ In-app purchases declared if applicable
  □ Camera/microphone/location usage descriptions (NSUsageDescription strings)
  □ Age rating accurately set
```

### Google Play (Android — Play Console)

```
Required Assets:
  ├── App icon: 512×512px PNG
  ├── Feature graphic: 1024×500px PNG/JPG
  ├── Screenshots: Phone (min 2) + 7-inch tablet + 10-inch tablet
  ├── Short description: Max 80 characters
  ├── Full description: Max 4000 characters
  ├── Privacy Policy URL: Required
  └── Data safety form: Must accurately declare what data is collected

Release Types:
  1. Internal testing (team only) → alpha → beta → production
  Always use staged rollout for production: 10% → 25% → 50% → 100%
```

### Web Publishing

```
Pre-deployment:
  □ All environment variables set in production
  □ SSL certificate valid and auto-renewing
  □ CDN configured and cache rules set
  □ sitemap.xml and robots.txt correct
  □ Google Analytics / Tag Manager configured
  □ Error monitoring (Sentry) connected to production
  □ Uptime monitoring configured (alert if > 1 min downtime)
  □ Backup strategy confirmed (daily automated backups)

Post-launch monitoring (first 48 hours):
  □ Crash rate within acceptable range (< 0.5%)
  □ Core user flows completing successfully (monitor conversion funnel)
  □ No spike in error logs
  □ Load times within expected range
  □ Support inbox monitored for critical issues
  □ Social media monitored for user feedback
```

### Launch Checklist (Complete)

```
ONE WEEK BEFORE:
  □ Final staging validation complete
  □ App Store / Play Store submission approved (can take 24–72h for Apple)
  □ All team members briefed on launch day responsibilities
  □ Support documentation / FAQ ready
  □ Social media / marketing materials ready

LAUNCH DAY:
  □ Deploy to production (or flip App Store / Play Store to available)
  □ Run smoke test on production immediately
  □ Send launch announcement (internal + external)
  □ Monitor dashboards for 4 hours post-launch
  □ Team on standby for hotfixes

POST-LAUNCH (Week 1):
  □ Review analytics daily — acquisition, activation, retention
  □ Respond to App Store / Play Store reviews
  □ Compile list of bugs and UX issues from real users
  □ Plan first patch release
  □ Schedule retrospective with full team
```

---

## Summary: Full Delivery Pipeline

```
BRD → FRD → UI/UX Mapping → Design → Build → UAT → Pen Test → Staging → Publish

Role of UX Designer at each stage:
  BRD:         Provides user research inputs, validates business goals against user needs
  FRD:         Defines screen list, user flows, error states, responsiveness rules
  UI/UX Map:   Creates traceability matrix — screens ↔ requirements ↔ test cases
  UAT:         Designs test scenarios, evaluates usability during testing
  Pen Test:    Ensures security-conscious UI patterns (auth flows, error messages, permissions)
  Staging:     Validates visual/UX correctness in production-like environment
  Publishing:  Creates App Store screenshots, writes store copy, defines ASO keywords
```

---

## Post-Launch Design Metrics & A/B Testing Framework

Shipping is not the finish line. Design decisions must be validated with real user behavior after launch.

### Post-Launch Design KPIs

Track these metrics in the first 30 days after launch to measure whether the design is working:

#### Usability Metrics (Did users accomplish their goal?)

| Metric | How to Measure | Target |
|--------|---------------|--------|
| **Task completion rate** | % of sessions where primary CTA was completed | ≥ 60% for new products |
| **Time on task** | Average time to complete core workflow | Compare to competitor benchmarks |
| **Error rate** | Form validation errors per session | < 1 error per session |
| **Rage clicks** | Clicks on non-interactive elements | < 2% of sessions |
| **Drop-off point** | Screen/step with highest exit rate | Investigate anything > 40% drop |

#### Engagement Metrics (Did users find value?)

| Metric | How to Measure | Target |
|--------|---------------|--------|
| **Feature adoption** | % of users who use a specific feature | Track week-over-week growth |
| **Return rate (D7, D30)** | Users who return after 7/30 days | D7 ≥ 25%, D30 ≥ 10% for new apps |
| **Session depth** | Pages/screens visited per session | Compare to pre-launch baseline |
| **Scroll depth** | % of page scrolled (landing pages) | Top CTA in top 30% scrolled |

#### Conversion Metrics (Did design drive business outcomes?)

| Metric | How to Measure | Target |
|--------|---------------|--------|
| **Conversion rate** | Visitors → signup / purchase / desired action | Set baseline, improve iteratively |
| **Funnel drop-off** | Step-by-step drop-off in conversion funnel | Identify and fix the biggest leak |
| **CTA click-through** | Clicks ÷ Impressions on primary CTA | ≥ 3-5% for landing pages |
| **Bounce rate** | Single-page sessions | < 50% for landing pages |

### A/B Testing Framework for Design Decisions

When to run an A/B test vs. just shipping:

```
Ship without testing:
  ✓ Bug fixes and accessibility improvements
  ✓ Obvious UX improvements with no hypothesis conflict
  ✓ Content changes with clear direction from user research
  ✓ Error state improvements

Always A/B test:
  ✓ CTA button copy, color, or placement
  ✓ Landing page headline or hero variation
  ✓ Pricing page layout
  ✓ Onboarding flow step count
  ✓ Form field order or number
  ✓ Navigation architecture changes
```

#### Running a Design A/B Test

```
Step 1: Define the hypothesis
  "Changing [X] to [Y] will increase [metric] by [Z]% because [reason]"
  
  Example: "Changing the CTA from 'Get started' to 'Start free trial'
  will increase signup conversions by 15% because it sets clearer
  expectations about commitment."

Step 2: Define success criteria before launch
  Primary metric: Signup conversion rate
  Secondary: CTA click-through rate
  Guardrails: Session length must not decrease (unhappy path check)
  Minimum sample size: Use power calculator — typically 1000+ per variant

Step 3: Run the test
  Duration: Minimum 2 weeks, run through at least 2 full business cycles
  Traffic split: 50/50 for clean variants, 80/20 if high-risk change
  Never: Stop the test early because one variant is "winning" — wait for significance

Step 4: Analyze and document
  Statistical significance: p < 0.05 (95% confidence)
  Document: Hypothesis, variants, result, decision, and follow-up questions
  Even losing tests are valuable — document WHY the losing variant failed

Step 5: Ship the winner and iterate
  After shipping: Monitor for regression (winning in test ≠ permanent winner)
  Follow-up: What new hypothesis does this result suggest?
```

### Design Debt Register

Track post-launch design issues that weren't fixed before launch:

```markdown
## Design Debt Register — [Product Name]

| Issue | Screen | Severity | User Impact | Effort | Priority | Target |
|-------|--------|----------|-------------|--------|----------|--------|
| [Description] | [Screen] | High/Med/Low | [How users are affected] | S/M/L | P1-P3 | [Sprint] |
```

Severity guide:
- **High**: Users cannot complete a task or are confused about a core flow
- **Medium**: Friction that reduces efficiency or satisfaction
- **Low**: Polish issue — minor inconsistency or visual imperfection

Review the design debt register every sprint. Anything High-severity that appears consistently in user sessions becomes P1.

### 30-Day Post-Launch Design Review

Schedule this review 30 days after every major launch:

```
AGENDA:
1. Metrics review (15 min)
   - Conversion before vs. after
   - Task completion rate
   - Top drop-off points

2. User feedback synthesis (15 min)
   - App store reviews since launch
   - Support tickets with UX root cause
   - Session replay highlights (Hotjar, FullStory)

3. Design debt triage (15 min)
   - Review all open design debt items
   - Prioritize based on user impact data

4. A/B test results review (10 min)
   - Any tests that have reached significance?
   - New tests to queue?

5. Next sprint design priorities (5 min)
   - Top 3 design improvements for next sprint
```
