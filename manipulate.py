import pandas as pd

# Load the CSV file
file_path = 'data/iris.csv'
df = pd.read_csv(file_path)

# Remove the last 10 rows
df = df[:-10]

# Save the modified DataFrame back to the same file
df.to_csv(file_path, index=False)

print(f"Updated file saved to {file_path}")
