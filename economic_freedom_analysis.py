import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
try:
    import seaborn as sns
    SEABORN_AVAILABLE = True
except ImportError:
    SEABORN_AVAILABLE = False

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(BASE_DIR, "Datasets", "index_of_economic_freedom.xlsx")
RESULTS_DIR = os.path.join(BASE_DIR, "Results")
WEB_RESULTS_DIR = os.path.join(BASE_DIR, "web", "results")

os.makedirs(RESULTS_DIR, exist_ok=True)
os.makedirs(WEB_RESULTS_DIR, exist_ok=True)

def run_analysis():
    print("--------------------------------------------------")
    print("Economic Freedom & Prosperity Data Analysis")
    print("--------------------------------------------------")
    
    # 1. Load Dataset
    if not os.path.exists(DATASET_PATH):
        print(f"Error: Dataset not found at {DATASET_PATH}")
        return
        
    print(f"Loading dataset from: {DATASET_PATH}")
    df = pd.read_excel(DATASET_PATH)
    
    # Clean Column Names (strip whitespace and special characters)
    df.columns = [c.strip().replace('\ufeff', '') for c in df.columns]
    
    # List of 12 Economic Freedom pillars
    freedom_pillars = [
        "Property Rights", "Judical Effectiveness", "Government Integrity",
        "Tax Burden", "Govt Spending", "Fiscal Health",
        "Business Freedom", "Labor Freedom", "Monetary Freedom",
        "Trade Freedom", "Investment Freedom", "Financial Freedom"
    ]
    
    # Check if required columns are present
    available_pillars = [col for col in freedom_pillars if col in df.columns]
    print(f"Available freedom pillars: {len(available_pillars)} / 12")
    
    # Convert columns to numeric, coercing errors
    numeric_cols = available_pillars + ["2022 Score", "GDP per Capita (PPP)", "Unemployment (%)", "Inflation (%)"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
    # Drop rows where Overall Score or Country Name is missing
    df = df.dropna(subset=["Country Name", "2022 Score"])
    
    print(f"Successfully loaded and cleaned {len(df)} country records.")

    # 2. Extract Rankings & Statistics
    # Top 10 Free Countries
    top_10 = df.nlargest(10, "2022 Score")[["Country Name", "Region", "2022 Score"]].to_dict(orient="records")
    
    # Bottom 10 Repressed Countries
    bottom_10 = df.nsmallest(10, "2022 Score")[["Country Name", "Region", "2022 Score"]].to_dict(orient="records")
    
    # Regional Scores
    regional_scores = df.groupby("Region")["2022 Score"].mean().round(2).to_dict()
    
    # Correlations with GDP per Capita
    correlations = {}
    if "GDP per Capita (PPP)" in df.columns:
        # Calculate correlation with freedom score
        gdp_col = df["GDP per Capita (PPP)"]
        for col in available_pillars:
            valid_data = df[[col, "GDP per Capita (PPP)"]].dropna()
            if len(valid_data) > 5:
                corr_val = np.corrcoef(valid_data[col], valid_data["GDP per Capita (PPP)"])[0, 1]
                correlations[col] = round(float(corr_val), 3)
                
    # 3. Save results.json
    results = {
        "summary": {
            "total_countries": len(df),
            "average_score": round(float(df["2022 Score"].mean()), 2),
            "median_score": round(float(df["2022 Score"].median()), 2)
        },
        "top_10_countries": top_10,
        "bottom_10_countries": bottom_10,
        "regional_averages": regional_scores,
        "prosperity_correlations": correlations
    }
    
    # Save to Results/ and web/results/
    for folder in [RESULTS_DIR, WEB_RESULTS_DIR]:
        with open(os.path.join(folder, "results.json"), "w") as f:
            json.dump(results, f, indent=4)
            
    print("Generated results.json successfully.")

    # 4. Generate Visualization Charts
    print("Generating analysis charts...")
    
    # Chart 1: Freedom vs GDP Scatter Plot
    if "GDP per Capita (PPP)" in df.columns:
        plt.figure(figsize=(9, 6))
        # Drop rows missing GDP
        scatter_data = df.dropna(subset=["2022 Score", "GDP per Capita (PPP)"])
        x = scatter_data["2022 Score"]
        y = scatter_data["GDP per Capita (PPP)"]
        
        plt.scatter(x, y, color='#06b6d4', alpha=0.7, edgecolors='none', s=50)
        
        # Fit regression line
        if len(x) > 5:
            m, b = np.polyfit(x, y, 1)
            x_range = np.linspace(x.min(), x.max(), 100)
            plt.plot(x_range, m*x_range + b, color='#8b5cf6', lw=2.5, label=f'Trend Line (R = {round(np.corrcoef(x, y)[0,1], 2)})')
            
        plt.title('Economic Freedom Score vs. GDP per Capita (PPP)', fontsize=13, fontweight='bold', pad=15)
        plt.xlabel('Economic Freedom Score (0 - 100)', fontsize=10, fontweight='bold')
        plt.ylabel('GDP per Capita (PPP, USD)', fontsize=10, fontweight='bold')
        plt.grid(True, linestyle=':', alpha=0.6)
        plt.legend()
        plt.tight_layout()
        
        plt.savefig(os.path.join(RESULTS_DIR, "freedom_vs_gdp_scatter.png"), dpi=300)
        plt.savefig(os.path.join(WEB_RESULTS_DIR, "freedom_vs_gdp_scatter.png"), dpi=300)
        plt.close()

    # Chart 2: Regional Average Scores
    if len(regional_scores) > 0:
        plt.figure(figsize=(9, 5))
        regions = list(regional_scores.keys())
        scores = list(regional_scores.values())
        
        # Color palette
        colors = ['#8b5cf6', '#06b6d4', '#10b981', '#f59e0b', '#ef4444', '#6b7280']
        bars = plt.bar(regions, scores, color=colors[:len(regions)], width=0.5)
        
        plt.title('Average Economic Freedom Score by Region', fontsize=13, fontweight='bold', pad=15)
        plt.ylabel('Average Score', fontsize=10, fontweight='bold')
        plt.ylim(0, 100)
        
        # Add labels on top of bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2.0, height + 2, f'{height}', ha='center', va='bottom', fontweight='bold')
            
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.xticks(rotation=15)
        plt.tight_layout()
        
        plt.savefig(os.path.join(RESULTS_DIR, "regional_comparison.png"), dpi=300)
        plt.savefig(os.path.join(WEB_RESULTS_DIR, "regional_comparison.png"), dpi=300)
        plt.close()

    # Chart 3: Correlation Matrix
    if len(available_pillars) > 0 and SEABORN_AVAILABLE:
        plt.figure(figsize=(10, 8))
        corr_cols = available_pillars + (["GDP per Capita (PPP)"] if "GDP per Capita (PPP)" in df.columns else [])
        corr_matrix = df[corr_cols].corr()
        
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5, cbar=True)
        plt.title('Correlation Matrix: Economic Freedoms vs. GDP per Capita', fontsize=13, fontweight='bold', pad=15)
        plt.tight_layout()
        
        plt.savefig(os.path.join(RESULTS_DIR, "correlation_heatmap.png"), dpi=300)
        plt.savefig(os.path.join(WEB_RESULTS_DIR, "correlation_heatmap.png"), dpi=300)
        plt.close()
    else:
        # Fallback plot if seaborn is not available
        plt.figure(figsize=(10, 6))
        if correlations:
            pillars_names = list(correlations.keys())
            corr_values = list(correlations.values())
            
            y_pos = np.arange(len(pillars_names))
            plt.barh(y_pos, corr_values, color='#06b6d4', edgecolor='none', height=0.6)
            plt.yticks(y_pos, pillars_names, fontsize=9, fontweight='bold')
            plt.xlabel('Correlation Coefficient with GDP per Capita', fontsize=10, fontweight='bold')
            plt.title('Correlation between Individual Freedoms & GDP per Capita', fontsize=13, fontweight='bold', pad=15)
            plt.grid(axis='x', linestyle='--', alpha=0.5)
            plt.xlim(-0.2, 1.0)
            plt.tight_layout()
            
            plt.savefig(os.path.join(RESULTS_DIR, "correlation_heatmap.png"), dpi=300)
            plt.savefig(os.path.join(WEB_RESULTS_DIR, "correlation_heatmap.png"), dpi=300)
            plt.close()

    print("Charts generated successfully.")
    print("--------------------------------------------------")
    print("Analysis Process Complete!")

if __name__ == "__main__":
    run_analysis()
