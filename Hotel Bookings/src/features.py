"""
features.py

Purpose:
Creates new features (variables) that help explain cancellations.

What this file does:
- Creates total_nights (weekend + weekday stays)
- Creates total_guests (adults + children + babies)

Why it exists:
Feature engineering improves model performance.
Keeps transformation logic separate from cleaning and modeling.
"""

import pandas as pd

def add_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates extra variables that may help explain cancellations.

    Adds:
    - total_nights = staysinweeknights + staysinweekendnights
    - total_guests = adults + children + babies
    """
    df = df.copy()

    # total nights
    if "staysinweeknights" in df.columns and "staysinweekendnights" in df.columns:
        df["total_nights"] = df["staysinweeknights"] + df["staysinweekendnights"]
    else:
        df["total_nights"] = pd.NA

    # total guests
    needed = {"adults", "children", "babies"}
    if needed.issubset(df.columns):
        df["total_guests"] = df["adults"] + df["children"] + df["babies"]
    else:
        df["total_guests"] = pd.NA

    return df