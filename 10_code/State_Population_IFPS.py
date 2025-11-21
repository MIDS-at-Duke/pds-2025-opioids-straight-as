# set environment
import pandas as pd
from pathlib import Path

# paths
BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "00_data" / "raw" / "population.csv.gz"
OUTPUT_PATH = BASE_DIR / "00_data" / "clean" / "state_population_clean.csv"


def main():
    # ------------------------------------------------------------------
    # 1. Load raw data
    # ------------------------------------------------------------------
    df = pd.read_csv(INPUT_PATH)
    print(f"Raw data shape: {df.shape}")

    # quick look at the raw data
    print("\n[Raw data head]")
    print(df.head())

    # ------------------------------------------------------------------
    # 2. Keep only the columns we need and check basic quality
    # ------------------------------------------------------------------
    df = df[["YEAR", "STATEFIP", "PERWT"]].copy()

    # ensure PERWT is numeric
    df["PERWT"] = pd.to_numeric(df["PERWT"], errors="coerce")

    # check missing values (we confirmed there are no missing values)
    print("\n[Missing values]")
    print(df.isna().sum())

    # ------------------------------------------------------------------
    # 3. Select treatment and control states
    # ------------------------------------------------------------------
    florida_group = [12]  # FL
    florida_controls = [13, 45, 37]  # GA, SC, NC
    washington_group = [53]  # WA
    washington_controls = [41, 30, 8]  # OR, MT, CO

    selected_fips = (
        florida_group + florida_controls + washington_group + washington_controls
    )

    df = df[df["STATEFIP"].isin(selected_fips)]

    print("\n[Data shape after filtering selected states]")
    print(df.shape)
    print("\n[Filtered data head]")
    print(df.head())

    # ------------------------------------------------------------------
    # 4. Basic analysis – check whether the sample is reasonable
    # ------------------------------------------------------------------
    print("\n[Sample size by state (STATEFIP)]")
    print(df["STATEFIP"].value_counts())

    print("\n[Sample size by state and year]")
    print(df.groupby(["STATEFIP", "YEAR"]).size())

    # ------------------------------------------------------------------
    # 5. Aggregate to state–year level
    # ------------------------------------------------------------------
    state_year = df.groupby(["STATEFIP", "YEAR"], as_index=False).agg(
        POP=("PERWT", "sum")
    )

    print("\n[State-year shape]")
    print(state_year.shape)
    print("\n[State-year head]")
    print(state_year.head())

    # ------------------------------------------------------------------
    # 6. Average population by state across all years
    #    (to check for imbalance we might need to address later)
    # ------------------------------------------------------------------
    avg_pop_by_state = (
        state_year.groupby("STATEFIP")["POP"]
        .mean()
        .reset_index()
        .rename(columns={"POP": "AVG_POP"})
        .sort_values("AVG_POP", ascending=False)
    )

    print("\n[Average population by state across all years]")
    print(avg_pop_by_state)

    # ------------------------------------------------------------------
    # 7. Save cleaned state-year file
    # ------------------------------------------------------------------
    state_year.to_csv(OUTPUT_PATH, index=False)
    print(f"\nCleaned data saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
