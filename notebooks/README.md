# 📓 Jupyter Notebooks: Exploratory Data Analysis (EDA)

This directory contains all exploratory and analytical notebooks for the BSW0 Solar Data Challenge. The focus is on profiling, cleaning, and analyzing solar irradiance data from Benin, Sierra Leone, and Togo, followed by a comparative analysis across the three countries.

---

## 📁 Notebook Contents

| File Name                  | Description |
|---------------------------|-------------|
| `benin_eda.ipynb`         | Country-level EDA for Benin: includes summary statistics, missing value analysis, outlier detection (Z-scores), cleaning, and visualizations. |
| `sierra_leone_eda.ipynb`  | Same process applied to Sierra Leone data. |
| `togo_eda.ipynb`          | Same process applied to Togo data. |
| `compare_countries.ipynb` | Aggregates cleaned data from all three countries. Includes side-by-side metric comparisons (GHI, DNI, DHI), statistical tests (ANOVA and Kruskal-Wallis), and summarized insights. |

---

## 🧪 Country-Specific EDA Approach

Each individual country notebook follows this structure:

1. **Data Loading**  
2. **Profiling**  
   - `describe()`  
   - Missing value report  
3. **Outlier Detection**  
   - Z-score method on key metrics (GHI, DNI, DHI, ModA, ModB, WS, WSgust)  
4. **Cleaning**  
   - Median imputation or row filtering  
5. **Visualizations**  
   - Time series plots (GHI, DNI, DHI, Tamb)  
   - Correlation heatmap  
   - Scatter plots (e.g., WS vs GHI, RH vs Tamb)  
   - Cleaning impact on ModA/ModB  
   - Bubble charts and wind analysis  
6. **Export**  
   - Cleaned dataset saved to `../data/<country>_clean.csv`

---

## 📊 Cross-Country Comparison (`compare_countries.ipynb`)

This notebook merges the cleaned datasets and compares the solar potential between Benin, Sierra Leone, and Togo.

**Key Components:**

- **Metric Comparison:**  
  Boxplots for GHI, DNI, DHI by country  
  Summary table (mean, median, std deviation)  

- **Statistical Analysis:**  
  One-way ANOVA and Kruskal–Wallis test to check if GHI differences are statistically significant  

- **Insights Summary:**  
  A concise 3-bullet summary highlights which country stands out and why  

- **Visual Summary (Bonus):**  
  Bar chart ranking countries by average GHI

---

## ⚠️ Notes

- Raw and cleaned `.csv` files are stored in the `../data/` folder and excluded via `.gitignore`
- All notebooks assume environment setup and package installation have been completed from the root directory

```bash
pip install -r ../requirements.txt
````

---

## 📌 Reproducibility

Run the country notebooks (`*_eda.ipynb`) first to generate cleaned datasets, then run `compare_countries.ipynb` to perform cross-country analysis.
