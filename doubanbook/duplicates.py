import json
import pandas as pd

# Load the JSON file
file_path = '/Users/williamma/Desktop/doubanbook/new.json'  # Replace with your JSON file path
with open(file_path, 'r') as file:
    data = json.load(file)

# Convert JSON data to a DataFrame
df = pd.DataFrame(data)

# Find duplicates based on all columns
duplicates = df[df.duplicated()]

# Alternatively, to find duplicates based on specific columns, use:
# duplicates = df[df.duplicated(subset=['column1', 'column2'])]

# Display the duplicate rows
print("Duplicate Rows:")
print(duplicates)

# Optionally, save the duplicates to a new JSON file
duplicates.to_json('duplicates.json')
