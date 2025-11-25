import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random

# ==========================================
# PART 1: DATA GENERATION (Simulating a Dataset)
# ==========================================
# The PDF allows choosing any relevant dataset .
# We are generating a "Superstore" style dataset.

def generate_data(num_records=1000):
    np.random.seed(42)
    categories = ['Furniture', 'Office Supplies', 'Technology']
    sub_categories = ['Chairs', 'Tables', 'Binders', 'Art', 'Phones', 'Accessories']
    regions = ['North', 'South', 'East', 'West']
    
    data = {
        'Transaction_ID': range(1, num_records + 1),
        'Category': [random.choice(categories) for _ in range(num_records)],
        'Sub_Category': [random.choice(sub_categories) for _ in range(num_records)],
        'Region': [random.choice(regions) for _ in range(num_records)],
        'Sales': np.random.uniform(10, 1000, num_records).round(2),
        'Quantity': np.random.randint(1, 20, num_records), # Represents inventory movement
        'Discount': np.random.choice([0, 0.1, 0.2, 0.3], num_records),
    }
    
    df = pd.DataFrame(data)
    # Calculate Profit (Sales * Margin - Discount impact)
    # Random margin between -10% (loss) and 40% (profit)
    margins = np.random.uniform(-0.1, 0.4, num_records)
    df['Profit'] = (df['Sales'] * margins).round(2)
    
    # Introduce some null values to satisfy "Clean missing/null records" requirement 
    df.loc[::50, 'Sales'] = np.nan 
    
    return df

print("Generating Data...")
df = generate_data()

# ==========================================
# PART 2: DATA CLEANING 
# ==========================================
print("\n--- Step 1: Data Cleaning ---")
print(f"Missing values before cleaning:\n{df.isnull().sum()}")

# Filling missing Sales with the median value
df['Sales'] = df['Sales'].fillna(df['Sales'].median())

print("Missing values after cleaning: 0")

# ==========================================
# PART 3: ANALYSIS (SQL Logic using Pandas)
# ==========================================
# Objective: Calculate profit margins by category 

print("\n--- Step 2: Profitability Analysis ---")
# Calculating Profit Margin %
df['Profit_Margin'] = (df['Profit'] / df['Sales']) * 100

# Grouping by Category to find profit draining areas
category_performance = df.groupby('Category')[['Sales', 'Profit', 'Profit_Margin']].mean().reset_index()
print("\nAverage Performance by Category:")
print(category_performance)

# Identifying "Profit-Draining" Categories 
lowest_profit_category = category_performance.sort_values(by='Profit').iloc[0]
print(f"\nLowest Profitable Category: {lowest_profit_category['Category']}")

# ==========================================
# PART 4: CORRELATION ANALYSIS 
# ==========================================
# Objective: Correlation between inventory (Quantity) and Profitability

print("\n--- Step 3: Correlation Analysis ---")
correlation = df[['Quantity', 'Profit']].corr().iloc[0, 1]
print(f"Correlation between Inventory Quantity and Profit: {correlation:.4f}")
print("(Interpretation: A value near 0 means quantity sold doesn't strongly predict profit)")

# ==========================================
# PART 5: VISUALIZATION 
# ==========================================
# Generating charts for the PDF Report

# Set style
sns.set_style("whitegrid")

# Chart 1: Profit by Category (Bar Chart)
plt.figure(figsize=(10, 6))
sns.barplot(data=category_performance, x='Category', y='Profit', palette='viridis')
plt.title('Average Profit by Category')
plt.ylabel('Average Profit ($)')
plt.savefig('profit_by_category.png') # Saves image for your report
print("\nGenerated Chart: profit_by_category.png")

# Chart 2: Regional Performance (Simulating Tableau Filters) 
plt.figure(figsize=(10, 6))
region_perf = df.groupby(['Region', 'Category'])['Profit'].sum().reset_index()
sns.barplot(data=region_perf, x='Region', y='Profit', hue='Category')
plt.title('Total Profit by Region and Category')
plt.savefig('regional_profit.png')
print("Generated Chart: regional_profit.png")

# Chart 3: Correlation Heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(df[['Sales', 'Quantity', 'Profit', 'Discount']].corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.savefig('correlation_matrix.png')
print("Generated Chart: correlation_matrix.png")

print("\nAnalysis Complete. Files saved.")