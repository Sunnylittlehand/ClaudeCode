with open('anthropic-research/captured-items.md', 'r') as f:
    content = f.read()

oct4_line = '> Updated 2026-10-04 with one material update: Anthropic Pre-IPO Investor Day Scheduled for October 14 (MATERIAL UPDATE to S-1 entry; invitations sent ~Oct 1–3; event at Anthropic SF HQ Oct 14; pre-roadshow meeting with institutional investors ahead of Nov 9 formal marketing start; enterprise commercial window now effectively closes ~Oct 14 before quiet period; bloomberg.com/news/articles/2026-10-01/anthropic-is-said-to-plan-pre-ipo-investor-day-as-listing-nears).\n'

oct3_marker = '> Updated 2026-10-03 with five new items:'

old_s1 = '| Anthropic S-1 Prospectus Circulated — $518B Compute Commitments, $11.5B Q2 Revenue, November IPO at $2T | https://finance.yahoo.com/technology/ai/articles/anthropic-1-518-billion-commitment-165731037.html | Anthropic | B/F | 2026-09-28 to 2026-10-01 | ⭐⭐⭐⭐⭐ | sessions-2026-10-02.md | 2026-10-02 | MATERIAL UPDATE to "Anthropic Begins Pre-IPO Investor Meetings" (sessions-2026-07-16.md); $4.59B FY2025 revenue; Q2 2026 $11.5B (≈$46B run rate); $518B forward compute obligations (80% non-cancelable): Google $111.1B, Amazon $110B, Microsoft $31.4B, Broadcom $161.2B, SpaceX $84.5B; Broadcom $42B convertible facility; net loss $42B ($34B non-cash); two customers = 25% 2025 revenue; Nov 9 week marketing start, pre-Thanksgiving Nasdaq listing; $2T valuation, $100B raise |'

new_s1 = '| Anthropic S-1 Prospectus Circulated — $518B Compute Commitments, $11.5B Q2 Revenue, November IPO at $2T | https://finance.yahoo.com/technology/ai/articles/anthropic-1-518-billion-commitment-165731037.html | Anthropic | B/F | 2026-09-28 to 2026-10-01 | ⭐⭐⭐⭐⭐ | sessions-2026-10-02.md | 2026-10-04 | MATERIAL UPDATE to "Anthropic Begins Pre-IPO Investor Meetings" (sessions-2026-07-16.md); $4.59B FY2025 revenue; Q2 2026 $11.5B (≈$46B run rate); $518B forward compute obligations (80% non-cancelable): Google $111.1B, Amazon $110B, Microsoft $31.4B, Broadcom $161.2B, SpaceX $84.5B; Broadcom $42B convertible facility; net loss $42B ($34B non-cash); two customers = 25% 2025 revenue; Nov 9 week marketing start, pre-Thanksgiving Nasdaq listing; $2T valuation, $100B raise; MATERIAL UPDATE 10-04: Pre-IPO Investor Day at SF HQ confirmed for Oct 14; invitations sent ~Oct 1–3; sessions-2026-10-04.md |'

if oct3_marker not in content:
    raise RuntimeError('Oct-03 marker not found in file')

updated = content.replace(oct3_marker, oct4_line + oct3_marker, 1)

if old_s1 not in updated:
    raise RuntimeError('Old S-1 row not found in file')

updated = updated.replace(old_s1, new_s1, 1)

with open('anthropic-research/captured-items.md', 'w') as f:
    f.write(updated)

print('Patch applied: +1 Oct-04 header line, updated S-1 row last_seen to 2026-10-04')
