# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
candidate = ""
# Define lists and dictionaries to track candidate names and vote counts
candidates = []
votes = [0,0,0]
voteperc = []
n = 0 #iterator for later
# Winning Candidate and Winning Count Tracker
winner = ""
maxvotes = 0
# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(".", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate in candidates:
            pass
        else:
            candidates.append(candidate)

        # Add a vote to the candidate's count
        for i in range(len(candidates)):     # adds votes for each candidate, only iterates as many times as there are candidates, ensures candidates get their own votes
            if candidate == candidates[i]:
                votes[i] += 1
    print("\n")
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    print("Election Results")
    print("-------------------------")
    print("Election Results", file = txt_file)                       # all here print to terminal and then output file
    print("-------------------------", file = txt_file)
    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    print(f"Total Votes: {total_votes}", file = txt_file)
    print("-------------------------", file = txt_file)
    # Loop through the candidates to determine vote percentages and identify the winner
    for i in candidates:
        voteperc.append(((votes[n])/(total_votes))*100)
        # Update the winning candidate if this one has more votes
        if n == 0:
            winner = candidates[n]
        else:
            if voteperc[n] > voteperc[n-1]:
                winner = candidates[n]
        # Print and save each candidate's vote count and percentage
        print(f"{candidates[n]}: {voteperc[n]} ({votes[n]})")
        print(f"{candidates[n]}: {voteperc[n]} ({votes[n]})", file = txt_file)
        n += 1

    # Generate and print the winning candidate summary
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
    print("-------------------------", file = txt_file)
    print(f"Winner: {winner}", file = txt_file)
    print("-------------------------", file = txt_file)
    # Save the winning candidate summary to the text file