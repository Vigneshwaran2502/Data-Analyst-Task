# Task 4: SQL & Database Management in PostgreSQL

This repository contains the completed project for Task 4 of the Data Analyst Internship, focusing on database management, SQL querying, and query optimization using PostgreSQL.

## 📝 Objective

The goal of this task was to import a real-world dataset into a PostgreSQL database, write complex SQL queries to answer business questions, and then analyze and optimize a slow query to improve database performance.

## 🛠️ Tools Used

* **Database:** PostgreSQL
* **Database Tool:** pgAdmin 4
* **Report Generation:** Microsoft Word / Google Docs

## 📊 Project Steps

1.  **Database & Table Setup:** A new database (`sales_db`) and table (`auto_sales`) were created in PostgreSQL.
2.  **Data Import & Cleaning:** The `Auto Sales data.csv` was imported. The `ORDERDATE` column was initially a `VARCHAR` with a `DD/MM/YYYY` format and was successfully transformed into a proper `DATE` type using SQL commands.
3.  **Business Analysis Queries:** Wrote SQL queries to find:
    * Total Sales by Product Line
    * Average Order Value
    * Customer Segmentation (High/Medium/Low Value)
4.  **Query Optimization:**
    * Used `EXPLAIN ANALYZE` to find a query that was using a slow **`Seq Scan`** (Sequential Scan).
    * Created a **`CREATE INDEX`** command on the `CUSTOMERNAME` column.
    * Ran `EXPLAIN ANALYZE` again to prove the query was now using a much faster **`Index Scan`**.

## 💡 Key Findings

* **Business Insights:** 'Classic Cars' is the most valuable product line by sales. The average order value and customer spending segments were successfully identified.
* **Optimization Success:** The query to find a customer by name was dramatically improved.
    * **Before Index:** `Seq Scan` with an execution time of **0.589 ms**.
    * **After Index:** `Index Scan` with an execution time of **0.063 ms** (nearly 10x faster).

## 📂 Files in this Repository

1.  **`task4_queries.sql` (Deliverable 1):** The complete SQL script containing all commands used for table creation, data cleaning, analysis, and optimization.
2.  **`Task 4 Report.pdf` (Deliverable 2):** The final PDF report containing screenshots of the business query results and the "Before vs. After" optimization analysis.
3.  **`Auto Sales data.csv`:** The raw dataset used for this project.