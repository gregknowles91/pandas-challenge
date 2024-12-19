# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path
file_path = os.path.join("analysis", "election_analysis.txt")
# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate_votes = {}
candidates = []

# Define lists and dictionaries to track candidate names and vote counts


# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = [2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
           candidates.append(candidate_name)
           candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )

    # Write the total vote count to the text file
    with open(file_path, "w") as txt_file:
        txt_file.write(content)

print(f"Total vote count written to {file_path}")

    # Loop through the candidates to determine vote percentages and identify the winner
for candidate in candidates:

        # Get the vote count and calculate the percentage
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage

        # Print and save each candidate's vote count and percentage
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(candidate_results, end="")
        txt_file.write(candidate_results)

    # Generate and print the winning candidate summary
winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.3f}%\n"
        f"-------------------------\n"
    )
print(winning_candidate_summary, end="")
txt_file.write(winning_candidate_summary)

    # Save the winning candidate summary to the text file
with open("election_analysis.txt","w") as txt_file:
        txt_file.write(analysis_content)
print(f"Election analysis saved to {file_path}")