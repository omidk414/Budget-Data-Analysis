# Import Pandas Package
import pandas as pd
import os

# Read in csv file from the Resources folder
file_path = pd.read_csv("Resources/budget_data.csv")

# Store the total number of months
total_months = len(file_path)

# Calculate Net total amount by accessing the Profit/Losses Column from the csv
net_total = file_path["Profit/Losses"].sum()

# The changes in Profit/Losses
changes = file_path["Profit/Losses"].diff()

# Calculate the average change
average_change = changes.mean()

# Find the greatest increase in profits using the Date column from the csv
greatest_increase = file_path.loc[changes == changes.max(), "Date"].iloc[0]

# Find the greatest decrease in profits using the Date column from the csv
greatest_decrease = file_path.loc[changes == changes.min(), "Date"].iloc[0]

# Create the output string
output = (
    "Financial Analysis\n\n"
    "----------------------------\n\n"
    f"Total Months: {total_months}\n\n"
    f"Total: ${net_total}\n\n"
    f"Average Change: ${average_change:.2f}\n\n"
    f"Greatest Increase in Profits: {greatest_increase} (${changes.max():.0f})\n\n"
    f"Greatest Decrease in Profits: {greatest_decrease} (${changes.min():.0f})"
)

# Print the output
print(output)

# Analysis folder path for the output file
output_folder = "Analysis"

# Define the output path
output_file = os.path.join(output_folder, "budget_data_analysis.txt")

# Exporting results to a text file
with open(output_file, "w") as text_file:
    text_file.write(output)