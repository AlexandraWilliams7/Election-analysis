#add our dependencies
import csv
import os

#assign a variable to load a file from a path. 
file_to_load = os.path.join("Resources", "election_results.csv")
#assign a varible to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Options and votes
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers= next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print Candidate name from each row
        candidate_name = row[2] 
        # If the candidate does not match any existing candidates
        # add iit to the candidate list. 
        if candidate_name not in candidate_options: 
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # tracking candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to the candidate's count. 
        candidate_votes[candidate_name] += 1
        
# Save the results to oue text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
     # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)
    # Iterate through the candidate list for votes.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print each candidate, their voter count, and percentage to the
        # terminal.
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # Print each candidate's voter count and percentage
        print(candidate_results)
        # Save results to text file
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning Candidate's results to terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    # Save the winning results
    txt_file.write(winning_candidate_summary)








