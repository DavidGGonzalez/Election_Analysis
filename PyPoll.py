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
         print(row[0])


with open(file_to_write,"w") as analysis_data:
    print(analysis_data)


