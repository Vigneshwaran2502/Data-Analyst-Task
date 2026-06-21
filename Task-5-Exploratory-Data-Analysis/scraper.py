import requests
from bs4 import BeautifulSoup
import csv 

url = "https://www.amazon.in/s?k=phones&crid=9OFY3HRF57XJ&sprefix=phones%2Caps%2C886&ref=nb_sb_noss_2"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# --- FINAL CODE ---

# 1. Create a list to hold all our data
data_list = []

# 2. Find all product "cards" using the most common Amazon class
products = soup.find_all("div", class_="s-result-item")

print(f"Found {len(products)} products on the page.") # Test line

# 3. Loop through each product
for product in products:
    
    # 4. Find the data using the classes YOU found
    
    # Name:
    name_element = product.find("h2", class_="a-size-medium a-spacing-none a-color-base a-text-normal")
    
    # Price:
    price_element = product.find("span", class_="a-price-whole")
    
    # Rating:
    rating_element = product.find("span", class_="a-icon-alt")

    # 5. Clean the data
    name = name_element.text.strip() if name_element else "N/A"
    price = price_element.text.strip() if price_element else "N/A"
    rating = rating_element.text.strip() if rating_element else "N/A"

    # 6. Add to our list, only if it's a real product
    if name != "N/A" and price != "N/A":
        data_list.append([name, price, rating])
        print(f"Found: {name}, {price}, {rating}") # Test line

# 7. Save the data to a CSV file
csv_headers = ["Product Name", "Price", "Rating"]

with open("scraped_products.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers) # Write the header
    writer.writerows(data_list)   # Write all the product data

print("---------------------------------")
print(f"Scraping complete! Saved {len(data_list)} products to scraped_products.csv")