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



print(total_votes)
print(candidate_options)
print(candidate_votes)

# with open(file_to_write,"w") as analysis_data:
#     print(analysis_data)


