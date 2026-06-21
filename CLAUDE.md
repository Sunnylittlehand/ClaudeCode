# CLAUDE.md

This repo produces a **daily AI intelligence report** for Sunny (Senior PM at an
investment bank running a Claude Code enterprise rollout). The report lives at
`anthropic-research/sessions-YYYY-MM-DD.md` and is emailed by
`.github/workflows/email-report.yml`.

## Before generating any daily report, read these first
1. **`anthropic-research/ROUTINE.md`** — the full routine spec (workflow, format, criteria).
2. **`anthropic-research/captured-items.md`** — the dedup ledger of everything already covered.

## Non-negotiable rules
- **Do not re-summarize an article that is already in the ledger.** Re-processing
  already-covered news from scratch is the #1 failure mode here and wastes tokens. If an
  item was fully covered in an earlier issue and still matters, **carry it forward as a
  one-line link** (title + source + stars + link to the issue where it was covered) in the
  "Previously Captured — Still Relevant" section at the bottom. Write a full entry only for
  **new** items or ones with a **material update** (state what changed).
- **Use one canonical title and one canonical URL per item** across all days so entries
  never fork (e.g. always "Anthropic Raises $65 Billion in Series H at $965 Billion
  Valuation", not a new variant each day).
- **Update `captured-items.md`** every day: add new items, refresh status for carried ones.
- **Cover the full criteria in ROUTINE.md §6** — not just launches/funding/partnerships,
  but also leadership interviews/talks/commentary and future-of-work / labor-impact stories
  (categories D & E). The structure should make it obvious at a glance what is new today
  vs. recurring context.

## Email workflow
- Runs daily on `schedule` (07:00 UTC) for the current date; also on `workflow_dispatch`
  (blank date = today) or on pushing `anthropic-research/email-trigger-YYYY-MM-DD.txt`.
- Scheduled runs only fire from the **default branch** — changes must reach `main` to take effect.
