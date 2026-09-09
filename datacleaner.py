import pandas as pd
import openpyxl
# Load the dataset into a Pandas DataFrame
file_path = "Distillation Column Dataset.xlsx"  
df = pd.read_excel(file_path)

# Print the first 10 rows
print("--- First 10 Rows ---")
print(df.head(10))

# Check DataFrame info and null values
print("\n--- DataFrame Info ---")
df.info()

# Summary statistics (min, max, mean, etc.) for each sensor
print("\n--- Summary Statistics ---")
print(df.describe())


# ==========================================
# Phase 3: Data Cleaning
# ==========================================

# List columns to remove (constant sensors, alternative target, and timestamp)
columns_to_remove = [
    "Sensor9",
    "Sensor10",
    "Sensor16",
    "MoleFractionHX",
    "Time",
]

# Permanently drop the columns from the DataFrame
df.drop(columns=columns_to_remove, inplace=True)

# Verify the updated shape of the DataFrame
print("\n--- Final DataFrame Shape ---")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
