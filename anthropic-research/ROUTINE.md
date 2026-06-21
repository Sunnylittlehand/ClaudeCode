# AI Intelligence Daily Routine — Specification

This is the canonical spec for the **daily AI intelligence report** that is generated as
`anthropic-research/sessions-YYYY-MM-DD.md` and emailed by
`.github/workflows/email-report.yml`. Every daily session MUST read this file and
`anthropic-research/captured-items.md` (the dedup ledger) **before** doing any research
or writing. The goals are (1) zero wasted re-processing of already-covered news and
(2) complete thematic coverage.

**Prepared for:** Sunny — Senior PM at an investment bank, leading a Claude Code
enterprise rollout in a regulated (UK/EU) financial-services context. Relevance to that
rollout is the lens for every item.

---

## 1. The two rules that matter most

### Rule A — Never process the same article from scratch twice (token discipline)
An item that was **already covered in full** in a previous day's report must **not** be
re-summarized. Once an item has a full write-up on day *N*, every later day either:
- **omits it** (if it is no longer relevant), or
- **carries it forward as a one-line link** in the "Previously Captured" section
  (see §4) — title + source + star rating + hyperlink to the issue where it was fully
  covered, plus a one-line status note **only if something actually changed**.

Do **not** re-read all prior `sessions-*.md` files to figure this out. Read
`captured-items.md` instead — that ledger is the single source of truth for "what have we
already covered." This is the whole point: the ledger exists so the daily run is cheap.

### Rule B — A full write-up is reserved for genuinely NEW or materially-updated items
Write a full entry (the section format in §3) only when the item is **not in the ledger**,
or when there is a **material update** since it was last covered (e.g. a model that was
launched is now suspended; a filing that was confidential is now public). A material
update gets a fresh short full entry that explicitly says what changed — not a re-run of
the original summary.

> Why this exists: as of 2026-06-21, "Anthropic S-1" had been written in full in 12
> separate daily reports, "Karpathy joins Anthropic" in 12, "Gates Foundation" in 10 —
> each re-derived from scratch, with the titles even drifting between runs. That is the
> waste this spec eliminates.

---

## 2. Daily workflow

1. **Read** this file and `captured-items.md`.
2. **Scan sources** (§5) for the coverage window (default: rolling 30 days) and identify
   candidate items against the criteria (§6).
3. **Classify** each candidate:
   - In ledger, no change → carry forward (link only).
   - In ledger, material update → short full entry noting the change; update ledger row.
   - Not in ledger → full entry; add a ledger row.
4. **Write** `sessions-YYYY-MM-DD.md` using the structure in §4.
5. **Update** `captured-items.md`: add new rows, update status/last-seen for carried items.
   Use **one canonical title and one canonical URL per item** so it never forks again.
6. **Trigger the email**: the workflow now runs automatically on a daily `schedule`
   (07:00 UTC) using the current date. For an off-cycle send, run the workflow manually
   (`workflow_dispatch`, leave the date blank for today) or push an
   `anthropic-research/email-trigger-YYYY-MM-DD.txt` file. (Scheduled runs only fire from
   the **default branch**, so this spec must be merged to `main` to take effect.)

---

## 3. Full-entry format (NEW / materially-updated items only)

Keep the existing section format already used in the reports:

```
## [Canonical Title](canonical-url)
**Source**: …
**Type**: …
**Date**: …
**Links**: primary · secondary · …

### Speaker / Author
### Significance Rating      ⭐…⭐ — one-line justification
### 摘要                      (Chinese summary)
### Summary                  (English summary)
### Main Takeaway
### Relevance to Sunny       ⭐…⭐ — rollout-specific implications
```

Sort full entries **highest significance first** (5★ → 1★).

---

## 4. Daily report structure

```
# AI Intelligence Report
**Generated / Coverage Period / Sources / Prepared for / Status / Sort order**

> Daily briefing note: one line stating what is NEW today vs carried forward.

---
## NEW & UPDATED ITEMS  (full entries, 5★ → 1★)
…

---
## Previously Captured — Still Relevant (no new full write-up)
A table of items already covered in full in earlier issues. Columns:
| Item (linked to the issue where it was fully covered) | Source | Date | Stars | Status / what changed |
Status is blank/"no change" unless there is a genuine update.

---
## Overall Themes This Period
## Recommended Actions for Sunny
**Status**: COMPLETE
```

The reader should be able to tell **at a glance** what is new (top) and what is recurring
context (the link table at the bottom).

---

## 5. Sources to scan

- **Anthropic** — news, research, institute, policy.
- **OpenAI / Codex** — news, research, changelog, developer posts.
- **Andrej Karpathy** — blog, talks.
- **Tier-1 press & interviews** — Bloomberg, Fortune, Axios, TechCrunch, CNBC, The
  Information, Reuters, WSJ — for **interviews, talks, op-eds, podcasts, and commentary**
  by AI leaders, plus labor-market / regulatory coverage.

---

## 6. Coverage criteria (EXPANDED)

Capture an item if it falls into **any** of these. Categories D and E were added on
2026-06-21 after Dario Amodei's Bloomberg interview on the future of work was missed —
the routine had been over-indexed on launches/funding/partnerships and was blind to
leadership commentary and labor-impact stories. Do not let that recur.

- **A. Models & products** — launches, major capability updates, benchmarks, pricing,
  availability/region restrictions.
- **B. Corporate & financial** — funding, valuations, IPO/S-1, partnerships, enterprise
  deals, org/leadership moves, office expansions.
- **C. Research, safety, policy & regulation** — papers, interpretability, governance
  frameworks, export controls, government enforcement.
- **D. Leadership voices & thought leadership** *(thematic, added 2026-06-21)* —
  interviews, talks, op-eds, podcasts, and public commentary by AI leaders (Amodei,
  Altman, Karpathy, Hassabis, etc.), **especially on the future of work, jobs, careers,
  white-collar / knowledge-work impact, and how individuals and organizations should
  adapt.** Dario Amodei's "Inside the Mind of…" Bloomberg interview is the reference
  example for this category.
- **E. Future-of-work & labor-market impact** *(thematic, added 2026-06-21)* — studies,
  data, and economic frameworks on AI's effect on employment and the workforce, even when
  not authored by Anthropic.
- **F. Enterprise / regulated-industry relevance** — anything materially affecting
  Claude Code adoption in banking/financial services and Sunny's rollout specifically.

When in doubt, prefer capturing (as at least a low-star item) over missing it; the ledger
keeps the cost of a recurring item near zero on subsequent days.
