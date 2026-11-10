#!/usr/bin/env python3
"""Check the publication assets included in this repository snapshot."""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
FIGURES = ROOT / "results" / "paper_assets" / "figures"
BREAKDOWN = ROOT / "results" / "paper_assets" / "tables" / "corrected_stress_breakdown.csv"

def main():
    assert BREAKDOWN.is_file(), f"Missing table: {BREAKDOWN}"
    df = pd.read_csv(BREAKDOWN)
    required = {"dimension", "level", "variant", "scenarios"}
    missing = required.difference(df.columns)
    assert not missing, f"Missing columns: {sorted(missing)}"

    expected_variants = {"adaptive", "fixed", "robust"}
    assert set(df["variant"].astype(str)) == expected_variants
    expected_dimensions = {"target_source", "mutation", "intensity"}
    assert set(df["dimension"].astype(str)) == expected_dimensions

    for dimension in sorted(expected_dimensions):
        totals = df.loc[df["dimension"] == dimension].groupby("variant")["scenarios"].sum()
        assert set(totals.index) == expected_variants
        assert all(int(v) == 240_000 for v in totals), (
            f"{dimension}: expected 240,000 scenarios per variant; got {totals.to_dict()}"
        )

    figures = sorted(p for p in FIGURES.iterdir() if p.is_file())
    assert figures, f"No manuscript figures found in {FIGURES}"

    print("Publication assets: PASS")
    print(f"Figures found: {len(figures)}")
    print("Corrected stress breakdown: 720,000 scenarios total per dimension")
    print("Per variant: 240,000 scenarios")

if __name__ == "__main__":
    main()
