{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f8397f6f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "PROJECT_ROOT: /Users/arushisingh/pds-2025-opioids-straight-as-7\n",
      "CLEAN DIR: /Users/arushisingh/pds-2025-opioids-straight-as-7/00_data/clean\n",
      "PROCESSED DIR: /Users/arushisingh/pds-2025-opioids-straight-as-7/00_data/processed\n"
     ]
    }
   ],
   "source": [
    "# CELL 1: imports and paths\n",
    "\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from pathlib import Path\n",
    "\n",
    "# Assume this notebook is in `notebooks/` – go up one level to repo root\n",
    "PROJECT_ROOT = Path(\"..\").resolve()\n",
    "\n",
    "DATA_CLEAN = PROJECT_ROOT / \"00_data\" / \"clean\"\n",
    "DATA_PROCESSED = PROJECT_ROOT / \"00_data\" / \"processed\"\n",
    "\n",
    "# States in our analysis\n",
    "KEEP_STATES = [\"FL\", \"GA\", \"AL\", \"SC\", \"WA\", \"CO\", \"ID\", \"OR\"]\n",
    "\n",
    "print(\"PROJECT_ROOT:\", PROJECT_ROOT)\n",
    "print(\"CLEAN DIR:\", DATA_CLEAN)\n",
    "print(\"PROCESSED DIR:\", DATA_PROCESSED)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f244980e",
   "metadata": {},
   "outputs": [],
   "source": [
    "# CELL 2: helper functions\n",
    "\n",
    "\n",
    "def std_state_abbrev(s: pd.Series) -> pd.Series:\n",
    "    \"\"\"Standardize state abbreviations (upper + strip).\"\"\"\n",
    "    return s.astype(str).str.upper().str.strip()\n",
    "\n",
    "\n",
    "def std_county(c: pd.Series) -> pd.Series:\n",
    "    \"\"\"Standardize county names so they match across datasets.\"\"\"\n",
    "    return (\n",
    "        c.astype(str)\n",
    "        .str.upper()\n",
    "        .str.strip()\n",
    "        .str.replace(\" COUNTY\", \"\", regex=False)\n",
    "        .str.replace(\" PARISH\", \"\", regex=False)\n",
    "        .str.replace(\" BOROUGH\", \"\", regex=False)\n",
    "        .str.replace(\" CENSUS AREA\", \"\", regex=False)\n",
    "    )"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "862b791c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Population columns: ['SUMLEV', 'REGION', 'DIVISION', 'STATE', 'COUNTY', 'STNAME', 'CTYNAME', 'ESTIMATESBASE2000', 'POPESTIMATE2001', 'POPESTIMATE2002', 'POPESTIMATE2003', 'POPESTIMATE2004', 'POPESTIMATE2005', 'POPESTIMATE2006', 'POPESTIMATE2007', 'POPESTIMATE2008', 'POPESTIMATE2009', 'CENSUS2010POP', 'POPESTIMATE2010', 'STATE_FIPS', 'COUNTY_FIPS', 'FIPS', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015', 'STATE_ABBR']\n",
      "Population shape BEFORE reshape: (3112, 28)\n",
      "Year columns detected: ['POPESTIMATE2001', 'POPESTIMATE2002', 'POPESTIMATE2003', 'POPESTIMATE2004', 'POPESTIMATE2005', 'POPESTIMATE2006', 'POPESTIMATE2007', 'POPESTIMATE2008', 'POPESTIMATE2009', 'POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']\n",
      "Population shape AFTER reshape + filter: (5220, 4)\n"
     ]
    },
    {
     "data": {
      "application/vnd.microsoft.datawrangler.viewer.v0+json": {
       "columns": [
        {
         "name": "index",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "state",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "county",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "year",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "population",
         "rawType": "int64",
         "type": "integer"
        }
       ],
       "ref": "2f09e20b-a8b8-45a8-a7b4-80116d3dbb00",
       "rows": [
        [
         "15560",
         "AL",
         "AUTAUGA",
         "2006",
         "51328"
        ],
        [
         "15561",
         "AL",
         "BALDWIN",
         "2006",
         "168121"
        ],
        [
         "15562",
         "AL",
         "BARBOUR",
         "2006",
         "27861"
        ],
        [
         "15563",
         "AL",
         "BIBB",
         "2006",
         "22099"
        ],
        [
         "15564",
         "AL",
         "BLOUNT",
         "2006",
         "55485"
        ]
       ],
       "shape": {
        "columns": 4,
        "rows": 5
       }
      },
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>state</th>\n",
       "      <th>county</th>\n",
       "      <th>year</th>\n",
       "      <th>population</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>15560</th>\n",
       "      <td>AL</td>\n",
       "      <td>AUTAUGA</td>\n",
       "      <td>2006</td>\n",
       "      <td>51328</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15561</th>\n",
       "      <td>AL</td>\n",
       "      <td>BALDWIN</td>\n",
       "      <td>2006</td>\n",
       "      <td>168121</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15562</th>\n",
       "      <td>AL</td>\n",
       "      <td>BARBOUR</td>\n",
       "      <td>2006</td>\n",
       "      <td>27861</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15563</th>\n",
       "      <td>AL</td>\n",
       "      <td>BIBB</td>\n",
       "      <td>2006</td>\n",
       "      <td>22099</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15564</th>\n",
       "      <td>AL</td>\n",
       "      <td>BLOUNT</td>\n",
       "      <td>2006</td>\n",
       "      <td>55485</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      state   county  year  population\n",
       "15560    AL  AUTAUGA  2006       51328\n",
       "15561    AL  BALDWIN  2006      168121\n",
       "15562    AL  BARBOUR  2006       27861\n",
       "15563    AL     BIBB  2006       22099\n",
       "15564    AL   BLOUNT  2006       55485"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# CELL 3: load county population (wide -> long)\n",
    "\n",
    "pop_path = DATA_CLEAN / \"county_population_2000_2015.csv\"\n",
    "pop_wide = pd.read_csv(pop_path)\n",
    "\n",
    "print(\"Population columns:\", list(pop_wide.columns))\n",
    "print(\"Population shape BEFORE reshape:\", pop_wide.shape)\n",
    "\n",
    "# ------------------------------------------------------------------\n",
    "# 1. Identify the year-specific columns (POPESTIMATEYYYY)\n",
    "# ------------------------------------------------------------------\n",
    "year_cols = [c for c in pop_wide.columns if c.startswith(\"POPESTIMATE\")]\n",
    "print(\"Year columns detected:\", year_cols)\n",
    "\n",
    "if not year_cols:\n",
    "    raise ValueError(\"No POPESTIMATE* columns found – check the population file.\")\n",
    "\n",
    "# ------------------------------------------------------------------\n",
    "# 2. Melt wide -> long: one row per county-year\n",
    "# ------------------------------------------------------------------\n",
    "id_vars = [\n",
    "    \"STATE\",  # numeric state code\n",
    "    \"COUNTY\",  # numeric county code\n",
    "    \"STNAME\",  # state name\n",
    "    \"CTYNAME\",  # county name\n",
    "    \"STATE_ABBR\",  # two-letter state abbrev (this is gold)\n",
    "    \"FIPS\",  # full county FIPS if present\n",
    "]\n",
    "\n",
    "id_vars = [c for c in id_vars if c in pop_wide.columns]  # keep only existing\n",
    "\n",
    "pop_long = pop_wide.melt(\n",
    "    id_vars=id_vars,\n",
    "    value_vars=year_cols,\n",
    "    var_name=\"year_var\",\n",
    "    value_name=\"population\",\n",
    ")\n",
    "\n",
    "# Extract year from 'POPESTIMATEYYYY'\n",
    "pop_long[\"year\"] = pop_long[\"year_var\"].str.extract(r\"(\\d{4})\").astype(int)\n",
    "\n",
    "# ------------------------------------------------------------------\n",
    "# 3. Standardize to common column names: state, county, year, population\n",
    "# ------------------------------------------------------------------\n",
    "pop = pop_long.rename(\n",
    "    columns={\n",
    "        \"STATE_ABBR\": \"state\",\n",
    "        \"CTYNAME\": \"county\",\n",
    "    }\n",
    ")\n",
    "\n",
    "# If STATE_ABBR isn't there for some reason, fall back to STNAME\n",
    "if \"state\" not in pop.columns:\n",
    "    pop = pop.rename(columns={\"STNAME\": \"state\"})\n",
    "\n",
    "# Keep just what we need\n",
    "pop = pop[[\"state\", \"county\", \"year\", \"population\"]].copy()\n",
    "\n",
    "# ------------------------------------------------------------------\n",
    "# 4. Standardize keys and filter years + states\n",
    "# ------------------------------------------------------------------\n",
    "pop[\"state\"] = std_state_abbrev(pop[\"state\"])\n",
    "pop[\"county\"] = std_county(pop[\"county\"])\n",
    "pop[\"year\"] = pop[\"year\"].astype(int)\n",
    "\n",
    "# Keep project years and states\n",
    "pop = pop[(pop[\"year\"] >= 2006) & (pop[\"year\"] <= 2015)]\n",
    "pop = pop[pop[\"state\"].isin(KEEP_STATES)].copy()\n",
    "\n",
    "print(\"Population shape AFTER reshape + filter:\", pop.shape)\n",
    "pop.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "0e935d6b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mortality columns: Index(['county', 'county_code', 'year', 'drug/alcohol_induced_cause',\n",
      "       'drug/alcohol_induced_cause_code', 'deaths', 'state'],\n",
      "      dtype='object')\n",
      "Mortality shape BEFORE cleaning: (6300, 7)\n",
      "Mortality shape AFTER filter: (1281, 7)\n"
     ]
    },
    {
     "data": {
      "application/vnd.microsoft.datawrangler.viewer.v0+json": {
       "columns": [
        {
         "name": "index",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "county",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "county_code",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "year",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "drug/alcohol_induced_cause",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "drug/alcohol_induced_cause_code",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "drug_deaths",
         "rawType": "float64",
         "type": "float"
        },
        {
         "name": "state",
         "rawType": "object",
         "type": "string"
        }
       ],
       "ref": "3ee92c50-b11b-4262-9884-761f2fa259d9",
       "rows": [
        [
         "0",
         "BALDWIN",
         "1003",
         "2009",
         "Drug poisonings (overdose) Unintentional (X40-X44)",
         "D1",
         "29.0",
         "AL"
        ],
        [
         "1",
         "CALHOUN",
         "1015",
         "2009",
         "Drug poisonings (overdose) Unintentional (X40-X44)",
         "D1",
         "12.0",
         "AL"
        ],
        [
         "2",
         "ETOWAH",
         "1055",
         "2009",
         "Drug poisonings (overdose) Unintentional (X40-X44)",
         "D1",
         "14.0",
         "AL"
        ],
        [
         "3",
         "HOUSTON",
         "1069",
         "2009",
         "Drug poisonings (overdose) Unintentional (X40-X44)",
         "D1",
         "10.0",
         "AL"
        ],
        [
         "4",
         "JEFFERSON",
         "1073",
         "2009",
         "Drug poisonings (overdose) Unintentional (X40-X44)",
         "D1",
         "80.0",
         "AL"
        ]
       ],
       "shape": {
        "columns": 7,
        "rows": 5
       }
      },
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>county</th>\n",
       "      <th>county_code</th>\n",
       "      <th>year</th>\n",
       "      <th>drug/alcohol_induced_cause</th>\n",
       "      <th>drug/alcohol_induced_cause_code</th>\n",
       "      <th>drug_deaths</th>\n",
       "      <th>state</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>BALDWIN</td>\n",
       "      <td>1003</td>\n",
       "      <td>2009</td>\n",
       "      <td>Drug poisonings (overdose) Unintentional (X40-...</td>\n",
       "      <td>D1</td>\n",
       "      <td>29.0</td>\n",
       "      <td>AL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>CALHOUN</td>\n",
       "      <td>1015</td>\n",
       "      <td>2009</td>\n",
       "      <td>Drug poisonings (overdose) Unintentional (X40-...</td>\n",
       "      <td>D1</td>\n",
       "      <td>12.0</td>\n",
       "      <td>AL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>ETOWAH</td>\n",
       "      <td>1055</td>\n",
       "      <td>2009</td>\n",
       "      <td>Drug poisonings (overdose) Unintentional (X40-...</td>\n",
       "      <td>D1</td>\n",
       "      <td>14.0</td>\n",
       "      <td>AL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>HOUSTON</td>\n",
       "      <td>1069</td>\n",
       "      <td>2009</td>\n",
       "      <td>Drug poisonings (overdose) Unintentional (X40-...</td>\n",
       "      <td>D1</td>\n",
       "      <td>10.0</td>\n",
       "      <td>AL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>JEFFERSON</td>\n",
       "      <td>1073</td>\n",
       "      <td>2009</td>\n",
       "      <td>Drug poisonings (overdose) Unintentional (X40-...</td>\n",
       "      <td>D1</td>\n",
       "      <td>80.0</td>\n",
       "      <td>AL</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      county  county_code  year  \\\n",
       "0    BALDWIN         1003  2009   \n",
       "1    CALHOUN         1015  2009   \n",
       "2     ETOWAH         1055  2009   \n",
       "3    HOUSTON         1069  2009   \n",
       "4  JEFFERSON         1073  2009   \n",
       "\n",
       "                          drug/alcohol_induced_cause  \\\n",
       "0  Drug poisonings (overdose) Unintentional (X40-...   \n",
       "1  Drug poisonings (overdose) Unintentional (X40-...   \n",
       "2  Drug poisonings (overdose) Unintentional (X40-...   \n",
       "3  Drug poisonings (overdose) Unintentional (X40-...   \n",
       "4  Drug poisonings (overdose) Unintentional (X40-...   \n",
       "\n",
       "  drug/alcohol_induced_cause_code  drug_deaths state  \n",
       "0                              D1         29.0    AL  \n",
       "1                              D1         12.0    AL  \n",
       "2                              D1         14.0    AL  \n",
       "3                              D1         10.0    AL  \n",
       "4                              D1         80.0    AL  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# CELL 4: load mortality (df_overdose_cleaned.csv)\n",
    "\n",
    "mort_path = DATA_CLEAN / \"df_overdose_cleaned.csv\"\n",
    "mort = pd.read_csv(mort_path)\n",
    "\n",
    "print(\"Mortality columns:\", mort.columns)\n",
    "print(\"Mortality shape BEFORE cleaning:\", mort.shape)\n",
    "\n",
    "# Rename columns to standard names\n",
    "rename_map_mort = {\n",
    "    \"state\": \"state\",\n",
    "    \"county\": \"county\",\n",
    "    \"year\": \"year\",\n",
    "    \"deaths\": \"drug_deaths\",\n",
    "}\n",
    "mort = mort.rename(columns=rename_map_mort)\n",
    "\n",
    "# Standardize\n",
    "mort[\"state\"] = std_state_abbrev(mort[\"state\"])\n",
    "mort[\"county\"] = std_county(mort[\"county\"])\n",
    "mort[\"year\"] = mort[\"year\"].astype(int)\n",
    "\n",
    "# Filter to 2006–2015 & project states\n",
    "mort = mort[(mort[\"year\"] >= 2006) & (mort[\"year\"] <= 2015)]\n",
    "mort = mort[mort[\"state\"].isin(KEEP_STATES)].copy()\n",
    "\n",
    "print(\"Mortality shape AFTER filter:\", mort.shape)\n",
    "mort.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "78d9b6d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ARCOS columns: Index(['state', 'county', 'year', 'total_grams', 'total_pills', 'total_mme',\n",
      "       'n_transactions'],\n",
      "      dtype='object')\n",
      "ARCOS shape BEFORE cleaning: (7078, 7)\n",
      "ARCOS shape AFTER filter: (5066, 7)\n"
     ]
    },
    {
     "data": {
      "application/vnd.microsoft.datawrangler.viewer.v0+json": {
       "columns": [
        {
         "name": "index",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "state",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "county",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "year",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "total_grams",
         "rawType": "float64",
         "type": "float"
        },
        {
         "name": "total_pills",
         "rawType": "float64",
         "type": "float"
        },
        {
         "name": "total_mme",
         "rawType": "float64",
         "type": "float"
        },
        {
         "name": "n_transactions",
         "rawType": "int64",
         "type": "integer"
        }
       ],
       "ref": "d60256ba-e8a4-4c21-8a33-f3ae833dfcc1",
       "rows": [
        [
         "0",
         "AL",
         "AUTAUGA",
         "2006",
         "16491.87966482",
         "2402543.97",
         "19461888.846481506",
         "9389"
        ],
        [
         "1",
         "AL",
         "AUTAUGA",
         "2007",
         "18270.377233611",
         "2720626.32",
         "21401308.88344",
         "9758"
        ],
        [
         "2",
         "AL",
         "AUTAUGA",
         "2008",
         "20230.535383711",
         "2933776.4",
         "23820056.325099494",
         "8789"
        ],
        [
         "3",
         "AL",
         "AUTAUGA",
         "2009",
         "22818.802738168",
         "3230753.3",
         "26829984.9374405",
         "9043"
        ],
        [
         "4",
         "AL",
         "AUTAUGA",
         "2010",
         "23748.835466422",
         "3269461.2",
         "28283805.114221506",
         "9455"
        ]
       ],
       "shape": {
        "columns": 7,
        "rows": 5
       }
      },
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>state</th>\n",
       "      <th>county</th>\n",
       "      <th>year</th>\n",
       "      <th>total_grams</th>\n",
       "      <th>total_pills</th>\n",
       "      <th>total_mme</th>\n",
       "      <th>n_transactions</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AL</td>\n",
       "      <td>AUTAUGA</td>\n",
       "      <td>2006</td>\n",
       "      <td>16491.879665</td>\n",
       "      <td>2402543.97</td>\n",
       "      <td>1.946189e+07</td>\n",
       "      <td>9389</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AL</td>\n",
       "      <td>AUTAUGA</td>\n",
       "      <td>2007</td>\n",
       "      <td>18270.377234</td>\n",
       "      <td>2720626.32</td>\n",
       "      <td>2.140131e+07</td>\n",
       "      <td>9758</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AL</td>\n",
       "      <td>AUTAUGA</td>\n",
       "      <td>2008</td>\n",
       "      <td>20230.535384</td>\n",
       "      <td>2933776.40</td>\n",
       "      <td>2.382006e+07</td>\n",
       "      <td>8789</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AL</td>\n",
       "      <td>AUTAUGA</td>\n",
       "      <td>2009</td>\n",
       "      <td>22818.802738</td>\n",
       "      <td>3230753.30</td>\n",
       "      <td>2.682998e+07</td>\n",
       "      <td>9043</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AL</td>\n",
       "      <td>AUTAUGA</td>\n",
       "      <td>2010</td>\n",
       "      <td>23748.835466</td>\n",
       "      <td>3269461.20</td>\n",
       "      <td>2.828381e+07</td>\n",
       "      <td>9455</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  state   county  year   total_grams  total_pills     total_mme  \\\n",
       "0    AL  AUTAUGA  2006  16491.879665   2402543.97  1.946189e+07   \n",
       "1    AL  AUTAUGA  2007  18270.377234   2720626.32  2.140131e+07   \n",
       "2    AL  AUTAUGA  2008  20230.535384   2933776.40  2.382006e+07   \n",
       "3    AL  AUTAUGA  2009  22818.802738   3230753.30  2.682998e+07   \n",
       "4    AL  AUTAUGA  2010  23748.835466   3269461.20  2.828381e+07   \n",
       "\n",
       "   n_transactions  \n",
       "0            9389  \n",
       "1            9758  \n",
       "2            8789  \n",
       "3            9043  \n",
       "4            9455  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# CELL 5: load cleaned ARCOS county-year aggregates\n",
    "\n",
    "arcos_path = DATA_PROCESSED / \"arcos_county_year.csv\"\n",
    "arcos = pd.read_csv(arcos_path)\n",
    "\n",
    "print(\"ARCOS columns:\", arcos.columns)\n",
    "print(\"ARCOS shape BEFORE cleaning:\", arcos.shape)\n",
    "\n",
    "# Standardize keys\n",
    "arcos[\"state\"] = std_state_abbrev(arcos[\"state\"])\n",
    "arcos[\"county\"] = std_county(arcos[\"county\"])\n",
    "arcos[\"year\"] = arcos[\"year\"].astype(int)\n",
    "\n",
    "# Filter to project states and years\n",
    "arcos = arcos[arcos[\"state\"].isin(KEEP_STATES)].copy()\n",
    "arcos = arcos[(arcos[\"year\"] >= 2006) & (arcos[\"year\"] <= 2015)]\n",
    "\n",
    "print(\"ARCOS shape AFTER filter:\", arcos.shape)\n",
    "arcos.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "f8c3d316",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Panel shape after merges: (5220, 8)\n"
     ]
    },
    {
     "data": {
      "application/vnd.microsoft.datawrangler.viewer.v0+json": {
       "columns": [
        {
         "name": "index",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "state",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "county",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "year",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "population",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "total_pills",
         "rawType": "float64",
         "type": "float"
        },
        {
         "name": "total_mme",
         "rawType": "float64",
         "type": "float"
        },
        {
         "name": "drug_deaths",
         "rawType": "float64",
         "type": "float"
        }
       ],
       "ref": "f7a56a87-3bfa-46b4-9670-f42f8ad59335",
       "rows": [
        [
         "0",
         "AL",
         "AUTAUGA",
         "2006",
         "51328",
         "2402543.97",
         "19461888.846481506",
         null
        ],
        [
         "1",
         "AL",
         "BALDWIN",
         "2006",
         "168121",
         "6941338.55",
         "59596364.6092135",
         "11.0"
        ],
        [
         "2",
         "AL",
         "BARBOUR",
         "2006",
         "27861",
         "860359.38",
         "6411106.884712",
         null
        ],
        [
         "3",
         "AL",
         "BIBB",
         "2006",
         "22099",
         "800364.0",
         "6845391.383209",
         null
        ],
        [
         "4",
         "AL",
         "BLOUNT",
         "2006",
         "55485",
         "1353317.3",
         "11340324.4449675",
         null
        ]
       ],
       "shape": {
        "columns": 7,
        "rows": 5
       }
      },
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>state</th>\n",
       "      <th>county</th>\n",
       "      <th>year</th>\n",
       "      <th>population</th>\n",
       "      <th>total_pills</th>\n",
       "      <th>total_mme</th>\n",
       "      <th>drug_deaths</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AL</td>\n",
       "      <td>AUTAUGA</td>\n",
       "      <td>2006</td>\n",
       "      <td>51328</td>\n",
       "      <td>2402543.97</td>\n",
       "      <td>1.946189e+07</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AL</td>\n",
       "      <td>BALDWIN</td>\n",
       "      <td>2006</td>\n",
       "      <td>168121</td>\n",
       "      <td>6941338.55</td>\n",
       "      <td>5.959636e+07</td>\n",
       "      <td>11.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AL</td>\n",
       "      <td>BARBOUR</td>\n",
       "      <td>2006</td>\n",
       "      <td>27861</td>\n",
       "      <td>860359.38</td>\n",
       "      <td>6.411107e+06</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AL</td>\n",
       "      <td>BIBB</td>\n",
       "      <td>2006</td>\n",
       "      <td>22099</td>\n",
       "      <td>800364.00</td>\n",
       "      <td>6.845391e+06</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AL</td>\n",
       "      <td>BLOUNT</td>\n",
       "      <td>2006</td>\n",
       "      <td>55485</td>\n",
       "      <td>1353317.30</td>\n",
       "      <td>1.134032e+07</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  state   county  year  population  total_pills     total_mme  drug_deaths\n",
       "0    AL  AUTAUGA  2006       51328   2402543.97  1.946189e+07          NaN\n",
       "1    AL  BALDWIN  2006      168121   6941338.55  5.959636e+07         11.0\n",
       "2    AL  BARBOUR  2006       27861    860359.38  6.411107e+06          NaN\n",
       "3    AL     BIBB  2006       22099    800364.00  6.845391e+06          NaN\n",
       "4    AL   BLOUNT  2006       55485   1353317.30  1.134032e+07          NaN"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# CELL 6: build master county-year panel\n",
    "\n",
    "# Start with population as backbone\n",
    "panel = pop.copy()\n",
    "\n",
    "# Merge ARCOS shipments\n",
    "panel = panel.merge(\n",
    "    arcos[[\"state\", \"county\", \"year\", \"total_pills\", \"total_mme\", \"n_transactions\"]],\n",
    "    on=[\"state\", \"county\", \"year\"],\n",
    "    how=\"left\",\n",
    "    validate=\"1:1\",\n",
    ")\n",
    "\n",
    "# Merge mortality\n",
    "panel = panel.merge(\n",
    "    mort[[\"state\", \"county\", \"year\", \"drug_deaths\"]],\n",
    "    on=[\"state\", \"county\", \"year\"],\n",
    "    how=\"left\",\n",
    "    validate=\"1:1\",\n",
    ")\n",
    "\n",
    "print(\"Panel shape after merges:\", panel.shape)\n",
    "panel[\n",
    "    [\"state\", \"county\", \"year\", \"population\", \"total_pills\", \"total_mme\", \"drug_deaths\"]\n",
    "].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ea981acf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.microsoft.datawrangler.viewer.v0+json": {
       "columns": [
        {
         "name": "index",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "state",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "county",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "year",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "mme_per_capita",
         "rawType": "float64",
         "type": "float"
        },
        {
         "name": "overdoses_per_100k",
         "rawType": "float64",
         "type": "float"
        }
       ],
       "ref": "db00d4a5-4fde-4060-aed4-134206c0dbdd",
       "rows": [
        [
         "0",
         "AL",
         "AUTAUGA",
         "2006",
         "379.1670987858772",
         null
        ],
        [
         "1",
         "AL",
         "BALDWIN",
         "2006",
         "354.4849519644393",
         "6.542906597034279"
        ],
        [
         "2",
         "AL",
         "BARBOUR",
         "2006",
         "230.1104369804386",
         null
        ],
        [
         "3",
         "AL",
         "BIBB",
         "2006",
         "309.7602327349201",
         null
        ],
        [
         "4",
         "AL",
         "BLOUNT",
         "2006",
         "204.38540947945393",
         null
        ]
       ],
       "shape": {
        "columns": 5,
        "rows": 5
       }
      },
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>state</th>\n",
       "      <th>county</th>\n",
       "      <th>year</th>\n",
       "      <th>mme_per_capita</th>\n",
       "      <th>overdoses_per_100k</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AL</td>\n",
       "      <td>AUTAUGA</td>\n",
       "      <td>2006</td>\n",
       "      <td>379.167099</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AL</td>\n",
       "      <td>BALDWIN</td>\n",
       "      <td>2006</td>\n",
       "      <td>354.484952</td>\n",
       "      <td>6.542907</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AL</td>\n",
       "      <td>BARBOUR</td>\n",
       "      <td>2006</td>\n",
       "      <td>230.110437</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AL</td>\n",
       "      <td>BIBB</td>\n",
       "      <td>2006</td>\n",
       "      <td>309.760233</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AL</td>\n",
       "      <td>BLOUNT</td>\n",
       "      <td>2006</td>\n",
       "      <td>204.385409</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  state   county  year  mme_per_capita  overdoses_per_100k\n",
       "0    AL  AUTAUGA  2006      379.167099                 NaN\n",
       "1    AL  BALDWIN  2006      354.484952            6.542907\n",
       "2    AL  BARBOUR  2006      230.110437                 NaN\n",
       "3    AL     BIBB  2006      309.760233                 NaN\n",
       "4    AL   BLOUNT  2006      204.385409                 NaN"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# CELL 7: handle missing shipments + feature engineering basics\n",
    "\n",
    "# Overdose deaths: keep NaN as \"censored / missing\" – your prof warned about this!\n",
    "panel[\"missing_deaths\"] = panel[\"drug_deaths\"].isna().astype(int)\n",
    "\n",
    "# --- per capita metrics ---\n",
    "panel[\"mme_per_capita\"] = panel[\"total_mme\"] / panel[\"population\"]\n",
    "panel[\"pills_per_capita\"] = panel[\"total_pills\"] / panel[\"population\"]\n",
    "panel[\"overdoses_per_100k\"] = (panel[\"drug_deaths\"] / panel[\"population\"]) * 100_000\n",
    "\n",
    "# log transforms (add 1 to avoid log(0))\n",
    "panel[\"log_mme_per_capita\"] = np.log1p(panel[\"mme_per_capita\"])\n",
    "panel[\"log_overdoses_per_100k\"] = np.log1p(panel[\"overdoses_per_100k\"])\n",
    "\n",
    "panel[[\"state\", \"county\", \"year\", \"mme_per_capita\", \"overdoses_per_100k\"]].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "cfb09bf1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.microsoft.datawrangler.viewer.v0+json": {
       "columns": [
        {
         "name": "index",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "state",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "county",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "year",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "group_FL",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "group_WA",
         "rawType": "object",
         "type": "string"
        },
        {
         "name": "treated",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "post",
         "rawType": "int64",
         "type": "integer"
        },
        {
         "name": "t_minus_policy",
         "rawType": "float64",
         "type": "float"
        }
       ],
       "ref": "c15ffb26-f687-426c-9624-9532f670bf8f",
       "rows": [
        [
         "0",
         "AL",
         "AUTAUGA",
         "2006",
         "control_FL",
         "other",
         "0",
         "0",
         null
        ],
        [
         "1",
         "AL",
         "BALDWIN",
         "2006",
         "control_FL",
         "other",
         "0",
         "0",
         null
        ],
        [
         "2",
         "AL",
         "BARBOUR",
         "2006",
         "control_FL",
         "other",
         "0",
         "0",
         null
        ],
        [
         "3",
         "AL",
         "BIBB",
         "2006",
         "control_FL",
         "other",
         "0",
         "0",
         null
        ],
        [
         "4",
         "AL",
         "BLOUNT",
         "2006",
         "control_FL",
         "other",
         "0",
         "0",
         null
        ]
       ],
       "shape": {
        "columns": 8,
        "rows": 5
       }
      },
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>state</th>\n",
       "      <th>county</th>\n",
       "      <th>year</th>\n",
       "      <th>group_FL</th>\n",
       "      <th>group_WA</th>\n",
       "      <th>treated</th>\n",
       "      <th>post</th>\n",
       "      <th>t_minus_policy</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>AL</td>\n",
       "      <td>AUTAUGA</td>\n",
       "      <td>2006</td>\n",
       "      <td>control_FL</td>\n",
       "      <td>other</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>AL</td>\n",
       "      <td>BALDWIN</td>\n",
       "      <td>2006</td>\n",
       "      <td>control_FL</td>\n",
       "      <td>other</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>AL</td>\n",
       "      <td>BARBOUR</td>\n",
       "      <td>2006</td>\n",
       "      <td>control_FL</td>\n",
       "      <td>other</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>AL</td>\n",
       "      <td>BIBB</td>\n",
       "      <td>2006</td>\n",
       "      <td>control_FL</td>\n",
       "      <td>other</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>AL</td>\n",
       "      <td>BLOUNT</td>\n",
       "      <td>2006</td>\n",
       "      <td>control_FL</td>\n",
       "      <td>other</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  state   county  year    group_FL group_WA  treated  post  t_minus_policy\n",
       "0    AL  AUTAUGA  2006  control_FL    other        0     0             NaN\n",
       "1    AL  BALDWIN  2006  control_FL    other        0     0             NaN\n",
       "2    AL  BARBOUR  2006  control_FL    other        0     0             NaN\n",
       "3    AL     BIBB  2006  control_FL    other        0     0             NaN\n",
       "4    AL   BLOUNT  2006  control_FL    other        0     0             NaN"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# CELL 8: treatment + control groups + DiD helpers\n",
    "\n",
    "# Which rows are from FL vs WA?\n",
    "panel[\"is_FL\"] = (panel[\"state\"] == \"FL\").astype(int)\n",
    "panel[\"is_WA\"] = (panel[\"state\"] == \"WA\").astype(int)\n",
    "\n",
    "# Group labels for plotting\n",
    "FL_CONTROLS = [\"GA\", \"AL\", \"SC\"]\n",
    "WA_CONTROLS = [\"CO\", \"ID\", \"OR\"]\n",
    "\n",
    "panel[\"group_FL\"] = np.where(\n",
    "    panel[\"state\"] == \"FL\",\n",
    "    \"treated_FL\",\n",
    "    np.where(panel[\"state\"].isin(FL_CONTROLS), \"control_FL\", \"other\"),\n",
    ")\n",
    "\n",
    "panel[\"group_WA\"] = np.where(\n",
    "    panel[\"state\"] == \"WA\",\n",
    "    \"treated_WA\",\n",
    "    np.where(panel[\"state\"].isin(WA_CONTROLS), \"control_WA\", \"other\"),\n",
    ")\n",
    "\n",
    "# Generic treated + post indicators\n",
    "panel[\"treated\"] = panel[\"state\"].isin([\"FL\", \"WA\"]).astype(int)\n",
    "\n",
    "# Policy years\n",
    "FL_POLICY_YEAR = 2010\n",
    "WA_POLICY_YEAR = 2012\n",
    "\n",
    "panel[\"post\"] = np.where(\n",
    "    ((panel[\"state\"] == \"FL\") & (panel[\"year\"] >= FL_POLICY_YEAR))\n",
    "    | ((panel[\"state\"] == \"WA\") & (panel[\"year\"] >= WA_POLICY_YEAR)),\n",
    "    1,\n",
    "    0,\n",
    ")\n",
    "\n",
    "# Event time relative to policy (for treated states only)\n",
    "panel[\"t_minus_policy\"] = np.where(\n",
    "    panel[\"state\"] == \"FL\",\n",
    "    panel[\"year\"] - FL_POLICY_YEAR,\n",
    "    np.where(panel[\"state\"] == \"WA\", panel[\"year\"] - WA_POLICY_YEAR, np.nan),\n",
    ")\n",
    "\n",
    "# Fixed-effects helpers\n",
    "panel[\"county_fe\"] = panel[\"state\"] + \"_\" + panel[\"county\"]\n",
    "panel[\"year_fe\"] = panel[\"year\"]\n",
    "\n",
    "panel[\n",
    "    [\n",
    "        \"state\",\n",
    "        \"county\",\n",
    "        \"year\",\n",
    "        \"group_FL\",\n",
    "        \"group_WA\",\n",
    "        \"treated\",\n",
    "        \"post\",\n",
    "        \"t_minus_policy\",\n",
    "    ]\n",
    "].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "604a9818",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Saved:\n",
      " - /Users/arushisingh/pds-2025-opioids-straight-as-7/00_data/processed/master_county_year_panel.csv\n",
      " - /Users/arushisingh/pds-2025-opioids-straight-as-7/00_data/processed/master_county_year_panel.parquet\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "(5220, 23)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# CELL 9: save master panel\n",
    "\n",
    "out_csv = DATA_PROCESSED / \"master_county_year_panel.csv\"\n",
    "out_parquet = DATA_PROCESSED / \"master_county_year_panel.parquet\"\n",
    "\n",
    "panel.to_csv(out_csv, index=False)\n",
    "panel.to_parquet(out_parquet, index=False)\n",
    "\n",
    "print(\"Saved:\")\n",
    "print(\" -\", out_csv)\n",
    "print(\" -\", out_parquet)\n",
    "panel.shape"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.18"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
