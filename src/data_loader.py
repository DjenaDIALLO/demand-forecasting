"""Utilities for loading and preparing the Air Passengers dataset."""

from pathlib import Path

import pandas as pd

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "air_passengers.csv"


def load_air_passengers(path: Path = DATA_PATH) -> pd.DataFrame:
    """Load the Air Passengers dataset, indexed by month.

    Args:
        path: Path to the raw CSV file (columns: year, month, passengers).

    Returns:
        DataFrame indexed by monthly date, with a single 'passengers' column.
    """
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(
        df["year"].astype(str) + "-" + df["month"], format="%Y-%B"
    )
    return df.set_index("date")[["passengers"]]
