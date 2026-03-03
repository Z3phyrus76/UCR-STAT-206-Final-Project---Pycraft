"""
data_io.py

Purpose:
Handles loading raw hotel booking data from CSV files.

What this file does:
- Reads H1.csv and H2.csv from the data folder
- Adds a hotel_type label (Resort or City)
- Combines both datasets into one DataFrame
- Returns the full dataset

Why it exists:
Keeps all data loading logic separate from modeling or cleaning.
"""

import pandas as pd
from pathlib import Path

def load_hotel_data():
    project_root = Path(__file__).resolve().parents[1]
    data_dir = project_root / "data"

    h1 = pd.read_csv(data_dir / "H1.csv")
    h2 = pd.read_csv(data_dir / "H2.csv")

    h1["hotel_type"] = "Resort"
    h2["hotel_type"] = "City"

    df = pd.concat([h1, h2], ignore_index=True)
    return df