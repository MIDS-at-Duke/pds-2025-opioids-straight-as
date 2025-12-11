import pandas as pd
from pathlib import Path

# Where raw txt files were stored
# RAW_PATH = "/Users/rosellazheng/Desktop/US_VitalStatistics/"
# pattern = RAW_PATH + "Underlying Cause of Death, 20*.txt"

# files = glob.glob(pattern)
# print("Found files:", files)  # All are in there

# Combine all years
# df = pd.concat((pd.read_csv(f, sep="\t") for f in files), ignore_index=True)

# Quick clean of column names
# df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Save into project repo so everyone else can load this CSV
# OUTPUT = "/Users/rosellazheng/Desktop/idsproject/vital_stats_2003_2015.csv"
# df.to_csv(OUTPUT, index=False)

# print("Saved clean CSV to:", OUTPUT)

OUTPUT_URL = "https://raw.githubusercontent.com/MIDS-at-Duke/pds-2025-opioids-straight-as/refs/heads/Rosella/00_data/clean/vital_stats_2003_2015.csv?token=GHSAT0AAAAAADPWOMOTQLLGJB7AKHY64TO22J3I7IQ"
# Load the data once
df = pd.read_csv(OUTPUT_URL, dtype=str)
print(f"Raw data shape: {df.shape}")  # e.g., (57436, 8)
# Quick look at columns (optional, can be commented out)
print(df.columns.unique())

# --------------------------------------------------------------------
# 1. Drop rows with non-NA notes (these are the "weird notes" rows)
# --------------------------------------------------------------------
df_clean = df[df["notes"].isna()].copy()  # .copy() avoids SettingWithCopyWarning
print("Rows after dropping notes:", len(df_clean))  # expected: 57241
assert len(df_clean) == 57241, f"Row count mismatch after notes filter: {len(df_clean)}"

# Drop notes and year_code columns
df_clean = df_clean.drop(columns=["notes", "year_code"])
print(df_clean.columns)
print(df_clean.head())

# ---------------------------------------------------
# 2. Split county into county + state
# ---------------------------------------------------
df_clean[["county", "state"]] = df_clean["county"].str.split(", ", expand=True)
# print(df_clean.head())
print("Rows after county/state split:", len(df_clean))  # sanity check
# here we can change both county_code and year into int
df_clean.dtypes

# ---------------------------------------------------
# 3. Check categories for drug/alcohol induced cause
# ---------------------------------------------------
print(df_clean["drug/alcohol_induced_cause"].unique())

# Keep only unintentional drug poisonings (X40–X44)
df_overdose = df_clean[
    df_clean["drug/alcohol_induced_cause"]
    == "Drug poisonings (overdose) Unintentional (X40-X44)"
].copy()

df_overdose

print(
    "Rows after filtering unintentional overdoses:", len(df_overdose)
)  # expected: 7573
assert (
    len(df_overdose) == 7573
), f"Row count mismatch after overdose filter: {len(df_overdose)}"
# Confirm only D1 in cause code
print(df_overdose["drug/alcohol_induced_cause_code"].unique())

# ---------------------------------------------------
# 4. Exclude Alaska
# ---------------------------------------------------
df_overdose = df_overdose[df_overdose["state"] != "AK"].copy()
print("Rows after dropping AK:", len(df_overdose))  # expected: 7538
assert (
    len(df_overdose) == 7538
), f"Row count mismatch after dropping AK: {len(df_overdose)}"
df_overdose

# ---------------------------------------------------
# 5. Fix dtypes
# ---------------------------------------------------
df_overdose["deaths"] = pd.to_numeric(df_overdose["deaths"], errors="coerce").astype(
    "Int64"
)

df_overdose["county"] = df_overdose["county"].astype("string")
df_overdose["county_code"] = pd.to_numeric(
    df_overdose["county_code"], errors="coerce"
).astype("Int64")

df_overdose["drug/alcohol_induced_cause"] = df_overdose[
    "drug/alcohol_induced_cause"
].astype("string")

df_overdose["drug/alcohol_induced_cause_code"] = df_overdose[
    "drug/alcohol_induced_cause_code"
].astype("string")

df_overdose["year"] = pd.to_numeric(df_overdose["year"], errors="coerce").astype(
    "Int64"
)
df_overdose["state"] = df_overdose["state"].astype("string")

print("Rows after dtype fixes:", len(df_overdose))  # should still be 7538
assert len(df_overdose) == 7538, "Row count changed during dtype conversion!"

df_overdose

# Optional checks
print(df_overdose["drug/alcohol_induced_cause"].unique())
print(df_overdose.dtypes)

# ---------------------------------------------------
# 6. Restrict to overlapping years with teammate data
#    (2006–2015)
# ---------------------------------------------------
df_overdose = df_overdose[
    (df_overdose["year"] >= 2006) & (df_overdose["year"] <= 2015)
].copy()

print("Rows after restricting to 2006~2015:", len(df_overdose))  # expected: 6300
assert (
    len(df_overdose) == 6300
), f"Row count mismatch after year filter: {len(df_overdose)}"
# Quick sanity check by state
print(df_overdose["state"].value_counts())
print(df_overdose["state"].value_counts().sum())

# ---------------------------------------------------
# 7. Save cleaned overdose dataset to project repo
# ---------------------------------------------------

# Save relative to project (not your Desktop)
# OUTPUT2 = Path("00_data/clean/df_overdose_cleaned.csv")
# OUTPUT2.parent.mkdir(parents=True, exist_ok=True)
# df_overdose.to_csv(OUTPUT2, index=False)
# print(f"Saved cleaned overdose CSV to: {OUTPUT2}")
