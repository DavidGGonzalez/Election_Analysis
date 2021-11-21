# Goals
# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Import all required modules
import csv
import os

# Set a variable to hold the name and path of the files to read from and write to
file_to_read = os.path.join("Resources","election_results.csv")
file_to_write = os.path.join("Analysis","election_analysis.txt")
# Total Votes casted
total_votes = 0

# Candidate Optiosn list
candidate_options = []

# Declare a Candidates votes dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the Election results CSV file
with open(file_to_read,'r') as election_data:

    # Read file content
    file_reader = csv.reader(election_data)
    
    # Set the file in the 2nd row so we do not read the titles as records
    # Read and print header's row
    headers = next(election_data)
    print(headers)

    # Print each row
    for row in file_reader:
        # Increment the total number of votes
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add candidate name to the candidate list
            candidate_options.append(row[2])

            # Start tracking candidate's votes
            candidate_votes[candidate_name] = 0

        # Increment the total number of votes for the current candidate
        candidate_votes[candidate_name] += 1

# Now we need to calculate the percentage of votes per candidate
for candidate_name in candidate_votes:
    # Retrieve the number of votes
    votes = candidate_votes[candidate_name]

    # Calculate the percentage
    vote_percentage = float(votes) / float(total_votes) * 100

    if votes > winning_count:
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

    # Print the candidate and the percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

winning_candidate_summary = (
    f"------------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------------------------\n")

# Now I'll read the results in the election_analysis.txt
with open(file_to_write,"w") as analysis_data:
    election_results = (
        f"\nElection Results\n"
        f"------------------------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"------------------------------------------\n"
    )
    print(election_results)
    # Save this to the election_analysis.txt file
    analysis_data.write(election_results)

    # Now write candidates, votes and votes percentage
    for candidate_name in candidate_votes:
        analysis_data.write(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})")


    # Write Winning summary to close this case
    analysis_data.write(winning_candidate_summary)
    print(winning_candidate_summary)



