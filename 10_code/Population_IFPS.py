# set environment
import pandas as pd

# set the path
PATH = "../00_data/raw/population.csv.gz"
OUTPUT_PATH = "../00_data/clean/state_population_clean.csv"

# load the data
df = pd.read_csv(PATH)

# choose the data we need to use
df = df[["YEAR", "STATEFIP", "PERWT"]]

# catgorize groups for future use
florida_group = [12]  # FL
florida_controls = [13, 45, 37]  # GA, SC, NC
washington_group = [53]  # WA
washington_controls = [41, 30, 8]  # OR, MT, CO

# select states
selected_fips = (
    florida_group + florida_controls + washington_group + washington_controls
)
df = df[df["STATEFIP"].isin(selected_fips)]

# group the data to (state, year)
state_year = df.groupby(["STATEFIP", "YEAR"]).agg(POP=("PERWT", "sum")).reset_index()

# output file for future use
state_year.to_csv(OUTPUT_PATH, index=False)
print(f"Cleaned data saved to: {OUTPUT_PATH}")
