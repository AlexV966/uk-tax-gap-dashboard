# UK Tax Gap vs Income Dashboard (2006–2024)

An interactive dashboard exploring the relationship between median annual earnings and the UK's tax gap over nearly two decades. Built with Python, Plotly, and Dash.

## 📊 What Is This?

This project visualizes UK government data on two key metrics:

- **Median Annual Earnings** – What full-time employees in Great Britain earn on average each year (from ONS ASHE survey)
- **Total Tax Gap** – The difference between taxes the UK government *should* collect and what it *actually* collects (from HMRC estimates)

The dashboard lets you explore patterns, spot trends, and dig into the year-by-year changes. Spoiler: there's a loose correlation, but it's more interesting than that.

## 🎯 Key Features

- **Interactive Scatter Plot** – Click to colour points by:
  - Year (see the timeline at a glance)
  - Income growth (year-on-year %)
  - Tax gap growth (year-on-year %)
  
- **Sortable Data Table** – Browse, filter, and sort the full cleaned dataset

- **Insights Panel** – Pre-written analysis covering:
  - What the axes represent
  - Overall trends
  - Notable outliers (2020's COVID spike, 2014's anomaly)
  - Conclusions and next steps

- **Clean, Professional Design** – Responsive layout that works on desktop and mobile

## 🚀 Getting Started

### Prerequisites

You'll need Python 3.7+ and pip installed.

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/uk-tax-gap-dashboard.git
   cd uk-tax-gap-dashboard
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Dashboard

```bash
python Dashboard.py
```

Then open your browser to **http://127.0.0.1:8050/** and explore!

Press `Ctrl+C` to stop the server.

## 📁 Project Structure

```
uk-tax-gap-dashboard/
├── Dashboard.py                 # Main Dash application
├── dashboard_data.csv           # Cleaned dataset (2006–2024)
├── Data_Cleaning_HMRC.ipynb     # Jupyter notebook with data prep logic
├── Data_Dictionary.csv          # Column descriptions and data types
├── README.md                    # This file
└── requirements.txt             # Python dependencies
```

## 📋 Data Dictionary

### Columns in `dashboard_data.csv`

| Column | Type | Description |
|--------|------|-------------|
| `year` | Integer | Tax year (e.g., 2006 = 2006/07) |
| `median_annual_earnings_gbp` | Float | Median annual gross earnings (£), full-time employees, Great Britain (Source: ONS ASHE survey) |
| `total_tax_gap_bn` | Float | Total UK tax gap (£bn) – the difference between tax owed and tax collected (Source: HMRC) |
| `income_yoy_pct` | Float | Year-on-year % change in median earnings. NaN for 2006 (baseline year) |
| `taxgap_yoy_pct` | Float | Year-on-year % change in total tax gap. NaN for 2006 (baseline year) |

## 💡 What the Data Shows

**The Big Picture:**  
As earnings have grown from ~£19.5k (2006) to ~£31.6k (2024), the tax gap has roughly doubled from ~£32.5bn to ~£46.8bn. But it's not a perfect relationship—some years are interesting outliers.

**Notable Observations:**
- **2020 spike** – Tax gap jumped to £38.5bn despite earnings barely moving. Likely reflects COVID disruption to tax collection and businesses.
- **2022–2024 surge** – Post-pandemic wage recovery and accelerating tax gap. Income YoY % hit 7.08% in 2024; tax gap relatively flat.
- **Austerity years (2010–2012)** – Earnings barely budged and the tax gap was smallest. Dark purple on the income growth chart.
- **2014 anomaly** – Tax gap jumps to £36.5bn while earnings remained modest. Worth investigating further.

## 🔬 Data Sources

- **Earnings data:** Office for National Statistics (ONS) – Annual Survey of Hours and Earnings (ASHE)
- **Tax gap data:** HM Revenue & Customs (HMRC) – Annual tax gap estimates

## 🛠️ How It Works

1. **Data Loading** – `Dashboard.py` reads the cleaned CSV
2. **Table Prep** – Column names are formatted for readability (underscores → spaces, title case)
3. **Interactivity** – Dash callback listens for changes to the radio buttons and redraws the scatter plot
4. **Rendering** – Plotly generates the interactive chart; DataTable provides sorting/filtering

## 📝 Data Cleaning

See `Data_Cleaning_HMRC.ipynb` for the full data preparation workflow, including:
- Source data import
- Missing value handling
- Year-on-year % calculations
- Validation checks

## 🚧 Known Limitations

- **Missing 2011 data** – Not included in the dataset
- **2024 is preliminary** – The most recent year may be subject to revision
- **Causation unclear** – The correlation doesn't prove earnings *cause* the tax gap (or vice versa)

## 💬 Next Steps / Ideas

- Add more HMRC tax-gap breakdowns (income tax, VAT, PAYE, self-assessment, etc.)
- Include macro indicators (unemployment, GDP growth, inflation)
- Time-series forecasting for future tax gap trends
- Regional breakdowns (Scotland, Northern Ireland, etc.)

## 📄 License

This project is provided as-is for educational and analytical purposes. The underlying data is public and sourced from ONS and HMRC.

## ✉️ Questions?

If you spot errors, have questions, or want to collaborate, feel free to open an issue or get in touch.

---

**Built with:** Python • Pandas • Plotly • Dash  
**Last updated:** 2024
