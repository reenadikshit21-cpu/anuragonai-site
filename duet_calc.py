#!/usr/bin/env python3
"""Claude Duet: the arithmetic used in the video (no libraries). Every input is tagged T (Anthropic says), R (reported) or A (my assumption)."""
print("1. Background checks: if Duet checks every N hours (N is A: Anthropic only says 'every few hours')")
print(f"{'N (h)':>6} {'per day':>8} {'per 30 days':>12}")
for n in (2, 3, 4, 6, 8, 12):
    d = 24 / n
    print(f"{n:>6} {d:>8.0f} {d * 30:>12.0f}")
print("   Missing number (not published): allowance used by ONE check. Without it these counts cannot be turned into a % of a plan.\n")
print("2. Zapier AutomationBench, Opus 5.5 (R, a model test, NOT Duet): 263 passed of 657 tasks")
p = 263 / 657
print(f"   pass rate = {p * 100:.1f}%   ->  fails = {657 - 263} of 657 ({(1 - p) * 100:.1f}%)")
print("   estimated cost: $4.22 per attempted task (R) -> per pass = 4.22 / pass_rate =", f"${4.22 / p:.2f}", "(reported: $10.54)\n")
print("3. Anthropic's Claude Code auto-mode report (R, NOT Duet): 5.7% false negatives on 1,000 synthetic exfiltration attempts")
print(f"   = {1000 * 0.057:.0f} of 1,000 attempts not blocked;  17% of 52 curated overeager actions = {52 * 0.17:.1f} (about 9) not blocked")
print("   Browser prompt injection (older model, R): 1.4% attack success after 100 tries/environment.")
