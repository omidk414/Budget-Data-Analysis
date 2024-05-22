# Import necessary packages
import pandas as pd
import os

# Read the CSV file
file_path = pd.read_csv("Resources/election_data.csv")

# Calculate total number of votes cast
total_votes = len(file_path)

# Initialize an empty dictionary to store candidate votes
candidate_votes = {}

# Loop through each row in the DataFrame using conditional checks 
for candidate in file_path["Candidate"]:
    if candidate in candidate_votes:
        candidate_votes[candidate] += 1
    else:
        candidate_votes[candidate] = 1

# Find the winner of the election based on popular vote
winner_votes = 0
winner = ""
for candidate, votes in candidate_votes.items():
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Print Statements
output = (
    "Election Results\n\n"
    "-------------------------\n\n"
    f"Total Votes: {total_votes}\n\n"
    "-------------------------\n\n"
)

# Loop through each candidate and iterate over the keys
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n\n"

# Add the winner to the output
output += (
    "-------------------------\n\n"
    f"Winner: {winner}\n\n"
    "-------------------------\n\n"
)

# Print the output
print(output)

# Specify the output folder
output_folder = "Analysis"

# Write results to text file
output_file_path = os.path.join(output_folder, "election_data_analysis.txt")
with open(output_file_path, "w") as text_file:
    # Write the output to the text file
    text_file.write(output)
