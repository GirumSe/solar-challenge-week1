# ☀️ Solar Data Streamlit Dashboard

This dashboard is developed as part of the BSW0 Solar Data Challenge to provide interactive visualization and comparative analysis of solar irradiance metrics across Benin, Sierra Leone, and Togo.

---

## 🚧 Development Process

The dashboard was developed incrementally following modular and version-controlled practices:

1. **Project Setup**
   - Created a separate branch: `dashboard-dev`
   - Initialized folder structure under `app/` and `scripts/`

2. **Basic UI**
   - Added a Streamlit layout with a title, sidebar, and placeholder text.

3. **Interactive Components**
   - Added sidebar widgets to select countries and solar metrics (GHI, DNI, DHI).

4. **Data Loading**
   - Implemented dynamic CSV loading from the `data/` directory via a utility function (`load_clean_data`) in `app/utils.py`.

5. **Visualization**
   - Developed a reusable boxplot function (`plot_boxplot`) using Seaborn.
   - Displayed selected metric distributions interactively based on user inputs.

6. **Documentation**
   - Created this README to explain usage and deployment steps.
   - Ensured CSV files are excluded via `.gitignore`.

---

## 🚀 Usage Instructions

### ✅ Prerequisites

- Python 3.10+
- Packages in `requirements.txt` must be installed.

### 📦 Installation

From the root directory:

```bash
pip install -r requirements.txt
````

Ensure cleaned data files (`benin_clean.csv`, `sierra_leone_clean.csv`, `togo_clean.csv`) are placed inside the `data/` directory.

### ▶️ Running the App Locally

From the root of the project:

```bash
streamlit run app/main.py
```

You will be able to:

* Select countries to compare (Benin, Sierra Leone, Togo)
* Choose a solar metric (GHI, DNI, DHI)
* View boxplots that compare the selected metric across the chosen countries

---

## ☁️ Deployment

The dashboard can be deployed on [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Connect your GitHub repo
2. Select `app/main.py` as the entry point
3. Set Python version and install requirements from `requirements.txt`
4. Upload cleaned data files to the hosted environment (if required)

---

## 📁 File Structure

```
app/
├── __init__.py
├── main.py       # Main dashboard UI
├── utils.py      # Data loading and visualization functions

scripts/
├── __init__.py
└── README.md     # This documentation file
```

---

## 📌 Notes

* Cleaned data files are **not committed** to GitHub and are ignored via `.gitignore`
* All dashboard logic is implemented in code only; no data is bundled or exposed

