/*
Project: Retail Business Performance & Profitability Analysis
Description: SQL Logic used to extract insights for the analysis.
*/

-- 1. Data Cleaning: Identifying Null values in Sales
-- Objective: Ensure data integrity before analysis
SELECT * FROM Retail_Sales_Data 
WHERE Sales IS NULL;

-- 2. Category Performance Analysis
-- Objective: Calculate Sales, Profit, and Margins to find profit-draining categories
SELECT 
    Category,
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit,
    (SUM(Profit) / SUM(Sales)) * 100 AS Profit_Margin_Percentage
FROM Retail_Sales_Data
GROUP BY Category
ORDER BY Total_Profit DESC;

-- 3. Regional Profitability Check
-- Objective: Compare performance across regions to identify weak spots
SELECT 
    Region,
    Category,
    SUM(Profit) AS Total_Profit
FROM Retail_Sales_Data
GROUP BY Region, Category
ORDER BY Region, Total_Profit ASC;

-- 4. Discount Impact Analysis
-- Objective: Identify transactions where high discounts led to losses
SELECT 
    Transaction_ID,
    Category,
    Discount,
    Profit
FROM Retail_Sales_Data
WHERE Discount > 0.2 AND Profit < 0;