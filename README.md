# 📊 Measuring the Pulse of Prosperity — An Index of Economic Freedom Analysis

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=matplotlib&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Netlify](https://img.shields.io/badge/Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white)

> **Live Demo** 👉 [pulseofprosperity.netlify.app](https://pulseofprosperity.netlify.app)

---

## 📌 Project Overview

A comprehensive **data analysis and visualization project** studying the relationship between **Economic Freedom** and **National Prosperity** across countries. Using the Heritage Foundation's Index of Economic Freedom dataset, this project employs Python data science tools and Multiple Linear Regression to uncover how policy pillars (Rule of Law, Government Size, Regulatory Efficiency, Open Markets) drive GDP per capita, sovereign credit ratings, and foreign investment inflows.

The project delivers an interactive **Prosperity Predictor Playground** — a web dashboard where users can simulate economic policies using sliders and see predicted prosperity outcomes in real time.

---

## ✨ Key Features

### 📈 Data Analysis Pipeline (Python)
- **Exploratory Data Analysis** — Freedom vs GDP scatter plots, regional comparisons, correlation heatmaps
- **Multiple Linear Regression** — Predicts GDP per capita from 4 freedom pillars
- **Global Rankings** — Top 10 freest vs most repressed economies
- **Regional Comparisons** — Freedom scores across Asia, Europe, Americas, Middle East, etc.
- **Correlation Analysis** — Heatmap showing inter-pillar relationships

### 🖥️ Interactive Web Dashboard
- **4 Pillars Explained** — Rule of Law, Government Size, Regulatory Efficiency, Open Markets
- **Analysis Tabs** — Freedom vs GDP scatter, regional bar charts, correlation heatmap, rankings table
- **Prosperity Predictor Playground** — Drag sliders and click "Run Economic Simulation" to predict:
  - Economic Freedom Index Score & Prosperity Category
  - GDP per Capita estimate
  - Investment Confidence Index
  - Sovereign Credit Rating (AAA to D)
  - Expected FDI (Foreign Direct Investment) inflow
  - Innovation Capacity

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Data analysis & regression pipeline |
| Pandas | Data loading, cleaning & manipulation |
| NumPy | Numerical computations |
| Matplotlib / Seaborn | Charts and visualizations |
| Scikit-learn | Multiple Linear Regression model |
| HTML5 / CSS3 / JS | Interactive web dashboard |
| Netlify | Live deployment |

---

## 📂 Project Structure

```
Measuring-the-pulse-of-prosperity/
├── economic_freedom_analysis.py       # Full Python data analysis pipeline
├── requirements.txt                   # Python dependencies
├── Datasets/                          # Economic Freedom dataset (CSV)
├── Assets/                            # Supporting visuals and references
├── Output Screenshots/                # Generated chart screenshots
├── Results/                           # Analysis result files
├── Project Reports & Video Demonstration/
├── Tableau Dashboard and Story/       # Tableau visualizations (PDF & screenshots)
├── Task 1/                            # Phase 1 analysis notebooks
└── web/
    ├── index.html                     # Main dashboard page
    ├── styles.css                     # Premium dark-themed styling
    ├── script.js                      # Regression-based simulation engine
    └── results/                       # Generated charts for the web dashboard
```

---

## 🚀 Getting Started

### View Live Dashboard
Open: [pulseofprosperity.netlify.app](https://pulseofprosperity.netlify.app)

### Run Python Analysis Pipeline Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/Bhavya-Sree-K/Measuring-the-pulse-of-prosperity---An-index-of-economic-freedom-analysis.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the analysis:
   ```bash
   python economic_freedom_analysis.py
   ```

### Run Web Dashboard Locally
Open `web/index.html` in your browser — no build step needed!

---

## 📊 Key Findings

| Finding | Insight |
|---------|---------|
| Top Freest Countries | Singapore, Switzerland, Ireland, New Zealand |
| High Freedom → High GDP | Countries with freedom score >75 average $45,000+ GDP per capita |
| Regulatory Efficiency Impact | Strongest individual predictor of economic growth |
| Repressed Economies | Average GDP per capita below $5,000 |

---

## 🏫 Academic Context

This project was developed as part of the **B.Tech Data Science & Analytics** curriculum at P.Tech (2nd Year). It demonstrates applied data science skills including:
- Statistical data analysis
- Regression modelling
- Data visualization with Python and Tableau
- Full-stack web development for data storytelling

---

## 👩‍💻 Developer

**Bhavya Sree K**
- 🔗 Portfolio: [bhavyasreekportfoilo.netlify.app](https://bhavyasreekportfoilo.netlify.app)
- 🐙 GitHub: [github.com/Bhavya-Sree-K](https://github.com/Bhavya-Sree-K)

---

## 📄 License

This project is open source and available for educational and academic purposes.