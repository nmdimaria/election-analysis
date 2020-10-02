import csv
import os
#dir(csv)

#Open the data file
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Data needed
#1 Total number of votes cast
#2 Complete list of candidates
#3 Percentage of votes for each candidate
#4 Total number of votes for each candidate
#5 Winner of election based on popular vote

#Total votes variable
total_votes = 0

# Candidate Options list
candidate_options = []

# Dictonary for candidate votes
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Read and print the header row.
    headers = next(file_reader)
# Print each row in the CSV file.
    for row in file_reader:
        total_votes += 1
#Candidate list
        candidate_name = row[2]
# Add the candidate name to the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
        # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
# Print vote percentage for each candidate
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = votes/total_votes*100
    
# Determine winning vote count and candidate
# 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)


# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in this Election\n----------------\nArapahoe\nDenver\nJefferson")