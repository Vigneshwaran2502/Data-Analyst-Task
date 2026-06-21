import pandas as pd

file_name = 'output_adjusted.xlsx'
try:
    df = pd.read_excel(file_name)
    print(f"✅ Successfully loaded '{file_name}' for final formatting.\n")
except FileNotFoundError:
    print(f"❌ Error: The file '{file_name}' was not found.")
    exit()

df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
print("✅ Converted 'date_added' column to datetime format.")

df.columns = df.columns.str.lower().str.replace(' ', '_')
print("✅ Standardized all column headers.")

print("\n--- Summary of Final Formatted Data ---")
df.info()

cleaned_file_name = 'netflix_cleaned.csv'
df.to_csv(cleaned_file_name, index=False)

print(f"\n🎉 Task complete! The final formatted data has been saved to '{cleaned_file_name}'.")