import csv
import os
#dir(csv)

#Open the data file
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

#Total votes variable
total_votes = 0

# Candidate Options list
candidate_options = []

# Dictonary for candidate votes
candidate_votes = {}

with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Read and print the header row.
    headers = next(file_reader)
    print(headers)
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
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name]
    vote_percentage = float(votes)/float(total_votes)*100
    print(f"{candidate_name}: received {round(vote_percentage, 2)}% of the vote.")

#Data needed
#1 Total number of votes cast
#2 Complete list of candidates
#3 Percentage of votes for each candidate
#4 Total number of votes for each candidate
#5 Winner of election based on popular vote


#Write down the names of all the candidates
#Add a vote count for each candidate
#Get the total votes for each candidate
#Get the total votes cast for the election


# Using the open() function with the "w" mode we will write data to the file.
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in this Election\n----------------\nArapahoe\nDenver\nJefferson")