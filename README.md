
# Opioid Policy Impact Analysis — Florida & Washington  
### IDS 720 · Practicing Data Science · Fall 2025  
### Group: Straight As  
Arushi Singh · Yifei (Rosella) Zheng · Sung‑Tse (Jay) Wu  

---

## 📌 Project Overview

Over the past two decades, the U.S. opioid crisis has intensified, evolving from prescription‑driven misuse to widespread harm from illicit opioids. In response, many states enacted policies aimed at reducing excessive prescribing.

This project evaluates the **causal impact** of two major state‑level interventions:

- **Florida (2010):** Pill‑mill crackdown + physician dispensing ban + PDMP requirements  
- **Washington (2012):** Opioid prescribing guidelines  

We measure how these interventions affected:

- **MME per capita opioid shipments**  
- **Opioid overdose mortality (per 100k)**  

To do this, we construct a harmonized **county‑year panel** dataset and apply:

1. **Pre‑Post analyses**  
2. **Difference‑in‑Differences (DiD)** models  

---

## 📂 Data Sources

Our final panel integrates three datasets:

### **1. ARCOS / Washington Post Opioid Shipments (2006–2019)**
- Shipment‑level data on oxycodone & hydrocodone  
- Aggregated to county‑year MME totals  
- Converted to **MME per capita**

### **2. CDC Multiple Cause of Death (2003–2015)**
- Opioid‑related overdose deaths  
- Includes ICD‑10 codes X40–X44, X60–X64, X85, Y10–Y14  
- Suppression for small counties → led to population cutoff decisions

### **3. Census / IPUMS Population Estimates**
- County‑level populations  
- Used to normalize shipments & mortality

---

## 🧹 Data Processing & Feature Construction

### **Harmonization**
- Merge datasets using **5‑digit FIPS codes**
- Construct:
  - `mme_per_capita = total_mme / population`
  - `overdoses_per_100k = deaths / population * 100000`

### **Missing Data Handling**
We tested 6 strategies:
- drop  
- mean  
- median  
- forward fill (ffill)  
- backward fill (bfill)  
- interpolate  

**bfill** was selected for final reporting due to stability around policy years.

### **Population Cutoff**
Mortality suppression required removing counties with < **10,000 population**, shown in the draft report’s Population Cutoff analysis (Fig. 1).  

---

## 🧪 Methods

### **1. Pre‑Post Analysis**
We examine within‑state trends before and after each policy year to identify:
- Trend breaks  
- Immediate vs. gradual responses  
- Slope changes  

### **2. Difference‑in‑Differences**
Model:

```
y_s,t = α_s + λ_t + β(Post × Treat) + ε_s,t
```

Treatment states:
- FL (policy year 2010)
- WA (policy year 2012)

Control states selected for geographic and market similarity:
- FL controls: GA, AL, SC  
- WA controls: OR, ID, CO  

Outcome variables:
- **MME per capita**  
- **Overdoses per 100k**

---

## 📊 Key Results

### **Florida**
- Large, sharp decrease in opioid shipments immediately after 2010  
- Overdose mortality also begins declining several years post‑policy  
- DiD estimates consistently negative across NaN strategies  
- Interpretation: Florida’s enforcement‑heavy intervention was highly effective

### **Washington**
- Modest declines in shipments before flattening  
- Overdose mortality shows weak or inconsistent improvements  
- DiD estimates are small and near zero  
- Interpretation: Non‑binding guidelines had limited impact without enforcement mechanisms

---

## 📁 Repository Structure

```
├── data/
│   ├── raw/
│   ├── processed/
│
├── notebooks/
│   ├── 01_arcos_chunking_merge.ipynb
│   ├── 02_mortality_merge.ipynb
│   ├── 03_construct_outcomes.ipynb
│   ├── 04_pre_post.ipynb
│   ├── 05_did_analysis.ipynb
│
├── figures/
│   ├── FL_prepost.png
│   ├── WA_prepost.png
│   ├── FL_DID.png
│   ├── WA_DID.png
│
└── README.md
```

---

## 🚀 Reproducing the Analysis

### **1. Download required datasets**
As noted in the paper (§A.1, Table 2):
- ARCOS shipments  
- CDC MCOD mortality  
- Census / IPUMS population  

### **2. Run data engineering notebooks**
1. Build `arcos_county_year.parquet`  
2. Merge mortality & population  
3. Construct per‑capita outcomes  

### **3. Run modeling notebooks**
- Pre‑post figures  
- DiD regression tables  
- Sensitivity analyses (all NaN strategies)

---

## ⚠️ Assumptions and Limitations

### **Parallel Trends**
The credibility of DiD relies on pre‑policy similarity between treatment & control state trends:
- FL shows good alignment  
- WA shows mild divergence → interpret results cautiously  

### **Data Limitations**
- Mortality suppression in sparsely populated counties introduces noise  
- Shipment data only captures legal, prescription opioids  
- External shocks (DEA enforcement, fentanyl waves) may influence outcomes  

### **Interpretation Boundaries**
Causality applies to *policy effects*, not the mechanisms behind them.

---

## 📝 Conclusion

Florida’s 2010 policy produced dramatic and sustained reductions in both opioid shipments and downstream mortality. Washington’s guideline‑oriented approach generated smaller, short‑term effects that did not substantially alter long‑run trends.

The findings reinforce a key insight for policymakers:

> **High‑intensity, enforcement‑based interventions produce larger immediate impacts, while guideline‑based approaches may require additional support to be effective.**

---

## 👥 Authors  
Arushi Singh  
Yifei (Rosella) Zheng  
Sung‑Tse (Jay) Wu  

IDS 720 — Practicing Data Science  
Duke University (Fall 2025)

---

*Draft report source: see uploaded submission PDF.*  
