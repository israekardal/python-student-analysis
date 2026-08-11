import pandas as pd

# Load the student dataset
data = pd.read_csv("students.csv")

# Display the first rows
print(data.head())

# Display basic information
print("\nDataset information:")
print(data.info())
