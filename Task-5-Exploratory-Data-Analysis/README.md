# Task 5: Web Scraping E-Commerce Data

This repository contains the completed project for Task 5 of the Data Analyst Internship, which focuses on web scraping.

## 📝 Objective

The goal of this task was to build a Python script to scrape product data from a live e-commerce website (Amazon) and save the extracted data into a structured CSV file.

## 🛠️ Tools Used

* **Python**
* **Requests** (Library to fetch the website's HTML)
* **BeautifulSoup** (Library to parse the HTML and find data)
* **CSV** (Library to write the data to a file)

## ⚙️ How it Works

The `scraper.py` script performs the following steps:

1.  **Sends a Request:** It sends an HTTP GET request to an Amazon search results page for "phones," using a `User-Agent` header to mimic a real browser.
2.  **Parses HTML:** It uses `BeautifulSoup` to parse the raw HTML returned by the server.
3.  **Finds Data:** It loops through all the product containers (identified by the `s-result-item` class) on the page.
4.  **Extracts Details:** For each product, it finds and extracts the **Product Name**, **Price**, and **Rating** by searching for their specific HTML tags and class names.
5.  **Saves to CSV:** It writes all the collected data into the `scraped_products.csv` file, with headers for each column.

## 📂 Files in this Repository

1.  **`scraper.py` (Deliverable 1):** The Python script that contains all the code to perform the web scraping.
2.  **`scraped_products.csv` (Deliverable 2):** The final output file containing the scraped data for product names, prices, and ratings.