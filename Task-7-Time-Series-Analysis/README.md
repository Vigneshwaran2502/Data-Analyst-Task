# Task 7: Time Series Analysis & Forecasting

This repository contains the completed project for Task 7 of the Data Analyst Internship. The objective was to analyze and forecast the `AirPassengers.csv` dataset using time series modeling.

## 🛠️ Tools and Libraries Used

* **Python**
* **Jupyter Notebook**
* **Pandas** (for data loading and manipulation)
* **Matplotlib & Seaborn** (for visualization)
* **Statsmodels** (specifically for `seasonal_decompose`, `adfuller` test, and `SARIMAX` model)

## 📊 Analysis & Modeling Process

1.  **Load & Prepare:** The `AirPassengers.csv` data was loaded. The 'Month' column was correctly parsed as a datetime object and set as the index for the time series.
2.  **Visualize & Decompose:** The data was plotted, revealing a clear upward **Trend** (more passengers over time) and a strong yearly **Seasonality** (peaks in summer). This was confirmed using `seasonal_decompose`.
3.  **Check for Stationarity:** The Augmented Dickey-Fuller (ADF) test was performed. The p-value was greater than 0.05, confirming the data was non-stationary and required differencing.
4.  **Build SARIMA Model:** A Seasonal ARIMA (SARIMA) model was chosen because it is specifically designed to handle both trend and seasonality. The model was built with `order=(1, 1, 1)` and `seasonal_order=(1, 1, 1, 12)` to account for the 12-month cycle.
5.  **Forecast:** The fitted model was used to generate a 36-month (3-year) forecast.

## 💡 Results

The final SARIMA model successfully captured the long-term upward trend and the repeating yearly seasonal patterns of the air passenger data. The resulting forecast (as seen in the notebook) accurately projects this complex behavior into the future.

## 📂 Files in this Repository

* **`Task-7-Time-Series-Analysis.ipynb` (Deliverable):** The complete Jupyter Notebook containing all the Python code, analysis, visualizations, and summary report.
* **`AirPassengers.csv`:** The raw dataset used for the analysis.