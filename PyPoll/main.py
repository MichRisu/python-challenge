# Import os and csv to start reading the csv file.
import os
import csv

# Create the path to access the file
csvpath = os.path.join('Resources', 'election_data.csv')

# Create empty lists 
candidates = []
vote_number = []
percent_votes = []

# Set up counter for total votes
total_votes = 0

# Read using CSV module
with open(csvpath, newline = "") as csvfile:
    # Set the variable and the delimiter
    PyPoll_reader = csv.reader(csvfile, delimiter = ",")
    # Skip header
    PyPoll_header = next(PyPoll_reader)
    # Create a loop 
    for row in PyPoll_reader:
        # Iterate through the list to count the total votes (will go to empty list)
        total_votes += 1 
        # Look in third column, add any new candidate names to empty list, and the vote count.
        # If name is in list already, count the vote.
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            vote_number.append(1)
        
        else:
            index = candidates.index(row[2])
            vote_number[index] += 1    
    # Calculate the percentages
    for votes in vote_number:
        percentage = (votes/total_votes) * 100
        percentage = "%.3f%%" % percentage
        # f makes it a floating number and the .3 is the number of decimals after the .
        percent_votes.append(percentage)
    

    
    # Find the winning candidate
    winner = max(vote_number)
    index = vote_number.index(winner)
    winning_candidate = candidates[index]


    #  Displaying results
print("Election Results")
print("---------------------------")
print(f"Total Votes: {(total_votes)}")
print("---------------------------")
# Use range to print each candidate
for i in range(len(candidates)):
    print(f"{candidates[i]}: {(percent_votes[i])} ({(vote_number[i])})")
print("---------------------------")
print(f"Winner: {winning_candidate}")
print("---------------------------")

# Output text to file.
with open('Election_Results.txt', 'w') as text_file:
    print("Election Results", file=text_file)
    print("---------------------------", file=text_file)
    print(f"Total Votes: {(total_votes)}", file=text_file)
    print("---------------------------", file=text_file)
    # Use range to print each candidate
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {(percent_votes[i])} ({(vote_number[i])})", file=text_file)
    print("---------------------------", file=text_file)
    print(f"Winner: {winning_candidate}", file=text_file)
    print("---------------------------", file=text_file)