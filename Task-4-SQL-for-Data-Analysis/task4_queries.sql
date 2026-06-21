
-- Task 4: SQL & Database Management

-- Step 1: Clean up and create the table
DROP TABLE IF EXISTS auto_sales CASCADE;

CREATE TABLE auto_sales (
    ORDERNUMBER INT,
    QUANTITYORDERED INT,
    PRICEEACH FLOAT,
    ORDERLINENUMBER INT,
    SALES FLOAT,
    ORDERDATE VARCHAR(20),
    DAYS_SINCE_LASTORDER INT,
    STATUS VARCHAR(50),
    PRODUCTLINE VARCHAR(100),
    MSRP INT,
    PRODUCTCODE VARCHAR(50),
    CUSTOMERNAME VARCHAR(255),
    PHONE VARCHAR(50),
    ADDRESSLINE1 VARCHAR(255),
    CITY VARCHAR(100),
    POSTALCODE VARCHAR(50),
    COUNTRY VARCHAR(100),
    CONTACTLASTNAME VARCHAR(100),
    CONTACTFIRSTNAME VARCHAR(100),
    DEALSIZE VARCHAR(50)
);



-- Step 2: Fix the date column after import
ALTER TABLE auto_sales ADD COLUMN order_date_temp DATE;

UPDATE auto_sales
SET order_date_temp = to_date(ORDERDATE, 'DD/MM/YYYY');

ALTER TABLE auto_sales DROP COLUMN ORDERDATE;

ALTER TABLE auto_sales RENAME COLUMN order_date_temp TO ORDERDATE;

-- Step 3: Business Analysis Queries

-- Query 1: Total Sales by Product
SELECT
    PRODUCTLINE,
    SUM(SALES) AS TotalSales
FROM
    auto_sales
GROUP BY
    PRODUCTLINE
ORDER BY
    TotalSales DESC;

-- Query 2: Average Order Value
SELECT
    AVG(OrderTotal) AS AverageOrderValue
FROM (
    SELECT
        ORDERNUMBER,
        SUM(SALES) AS OrderTotal
    FROM
        auto_sales
    GROUP BY
        ORDERNUMBER
) AS OrderSummaries;

-- Query 3: Customer Segmentation
SELECT
    CUSTOMERNAME,
    SUM(SALES) AS TotalSpent,
    CASE
        WHEN SUM(SALES) > 100000 THEN 'High Value'
        WHEN SUM(SALES) > 50000  THEN 'Medium Value'
        ELSE 'Low Value'
    END AS CustomerSegment
FROM
    auto_sales
GROUP BY
    CUSTOMERNAME
ORDER BY
    TotalSpent DESC;

-- Step 4: Query Optimization Analysis

-- Analysis "Before" Index:
EXPLAIN ANALYZE
SELECT * FROM auto_sales WHERE CUSTOMERNAME = 'Euro+ Shopping Channel';

-- Creating the Index:
CREATE INDEX idx_customername ON auto_sales(CUSTOMERNAME);

-- Analysis "After" Index:
EXPLAIN ANALYZE
SELECT * FROM auto_sales WHERE CUSTOMERNAME = 'Euro+ Shopping Channel';