# Task 8: Simple Sales Dashboard Design

This repository contains the deliverables for Task 8 of the Data Analyst Internship with Elevate Labs. [cite_start]The objective of this task was to build a simple, interactive sales dashboard using Tableau. [cite: 5, 7]

## 🎯 Objective

[cite_start]The goal was to create a basic interactive dashboard to visualize sales performance by product, region, and month using the provided Superstore dataset. [cite: 7, 12]

## 🛠️ Tools Used

* **Tableau:** Used for all data visualization and dashboard creation. [cite: 9]
* **Dataset:** `Sample - Superstore.csv` (Columns used: `Order Date`, `Region`, `Category`, `Sales`). [cite: 12]

##  deliverables

This repository includes:

1.  **Dashboard Screenshot (`Dashboard 1.png`):** An image export of the final interactive dashboard. [cite: 14]
2.  **Insights File (`insights.txt`):** A text file containing 3-4 key insights derived from the dashboard. [cite: 15]
3.  **Dataset (`.csv`):** The raw data file used for the analysis.
4.  **README (`.md`):** This file, explaining the project.

## 📁 Tableau Workbook (`task 8.twb`)

**File:** `task 8.twb` — Tableau Workbook (XML)

**Created with:** Tableau Desktop (please replace with the exact version you used)

**Includes:**
- Dashboard: "Sales Dashboard" — combines the Line Chart (Sales by Month), Bar Chart (Sales by Region), and Pie Chart (Sales by Category).
- Worksheets: e.g., `Line_Sales_Month`, `Bar_Sales_Region`, `Pie_Sales_Category` (sheet names may vary).
- Data source: `Sample - Superstore.csv` (embedded or referenced externally).
- Filters / Actions: Region filter implemented as a dashboard action (select a bar to filter other views).
- Calculated fields and formatting: Month-Year parsing, Total Sales aggregation, custom color palette for regions/categories.

**How to open & use:**
1. Open Tableau Desktop.
2. File → Open → select `task 8.twb`.
3. If Tableau prompts for the data source, point it to `Sample - Superstore.csv` in this repository.
4. Interact with the dashboard by selecting regions on the bar chart or using filters to update charts.

**Notes:**
- `.twb` is not packaged — it references external data. To share a single portable file, save as `.twbx` (File → Export Packaged Workbook).
- Update this README if you change the workbook name, sheet names, or Tableau version.


## 📊 Dashboard Visuals

The final dashboard includes the following components:

* **Line Chart:** Sales over Months [cite: 18]
* **Bar Chart:** Sales by Region [cite: 19]
* **Pie Chart:** Sales by Category (as a substitute for the Donut Chart) [cite: 20]
* **Interactive Filter:** The dashboard is filtered by `Region`. [cite_start]Clicking a region on the bar chart filters the line chart and pie chart accordingly. [cite: 22]

## 💡 Key Insights

*(This is where you should copy and paste the 3-4 insights you wrote in your `insights.txt` file. Here are some examples based on the dataset.)*

* **Insight 1:** The **West** region consistently had the highest sales, while the **South** region had the lowest.
* **Insight 2:** The **"Technology"** category is the highest-grossing category, followed by "Furniture."
* **Insight 3:** There is a recurring sales peak in the months of **November** and **December** each year, likely due to holiday shopping.