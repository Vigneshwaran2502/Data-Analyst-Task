import pandas as pd

file_name = 'output_adjusted.xlsx'

try:
    df = pd.read_excel(file_name)
    print(f"✅ Successfully loaded the dataset: '{file_name}'\n")
except FileNotFoundError:
    print(f"❌ Error: The file '{file_name}' was not found.")
    print("Please make sure the Python script and the Excel file are in the same folder.")
    exit()

print("--- 1. First 5 Rows of the Dataset ---")
print("This shows the column names and the type of data in them.")
print(df.head())
print("-" * 50)

print("\n--- 2. Data Summary and Missing Values ---")
print("Pay attention to 'Non-Null Count' to find columns with missing data.")
df.info()
print("-" * 50)

print("\n--- 3. Check for Duplicate Rows ---")
duplicate_count = df.duplicated().sum()
if duplicate_count > 0:
    print(f"Found {duplicate_count} duplicate rows that need to be removed.")
else:
    print("No duplicate rows found.")
print("-" * 50)

print("\n--- 4. Statistics for Numerical Columns ---")
print("This helps identify outliers or strange values (e.g., an impossible year).")
print(df.describe())
print("-" * 50)

print("\n✅ Initial analysis complete. You can now use this information for the cleaning step.")