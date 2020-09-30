import csv
import os
#dir(csv)

#Open the data file
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")
with open(file_to_load) as election_data:

# Read the file object with the reader function.
    file_reader = csv.reader(election_data)
# Read and print the header row.
    headers = next(file_reader)
    print(headers)

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