#!/usr/bin/env python3
"""Napkin math for 'Claude writes 90% of Claude Code'. Every input points to a SOURCES.md row."""
pr_growth, revert_share_drop = 2.0, 0.40          # rows 3: "more than doubled", "fell by more than 40 percent"
print(f"M1 absolute reverts vs June: {pr_growth*(1-revert_share_drop):.2f}x  (flat needs 2.5x PRs and -60% share: {2.5*0.4:.2f}x)")
print(f"M2 human share: at 80% -> {1-0.80:.0%}, at 90% -> {1-0.90:.0%} (halved)")   # rows 10, 1
lines_mult, human_share = 8, 0.20                 # row 12 (8x lines/engineer/day vs 2024), row 10
print(f"M3 human-typed lines vs 2024: {lines_mult*human_share:.1f}x")
changes, minutes = 30_000, 10                     # row 4; 10 min/change = ASSUMPTION
hours = changes*minutes/60; print(f"M4 reading load: {hours:,.0f} h/day = {hours/8:,.0f} full-time readers")
print(f"M5 monorepo growth May->Sep: {30_000/2_500:.0f}x")                          # row 4
print(f"M6 Cherny month: net {40_000-38_000:+,} lines, {259/30:.1f} PRs/day")       # row 16
print("M7 forecast Mar 2025 +3..6 mo = Jun..Sep 2025; measured 80% in May 2026 -> 8..11 months later")  # rows 14, 10
