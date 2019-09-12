import os
import csv

PyPoll = os.path.join(".", "resources", "election_data.csv")

# define variables and lists to hold values
Candidates = []
votes_received = []
percent_received = []
total_votes = 0


with open(PyPoll, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] not in Candidates:
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            votes_received.append(1)
        else:
            index = Candidates.index(row[2])
            votes_received[index] += 1
    
    for votes in votes_received:
        percentage = (votes / total_votes) * 100
        percentage = round(percentage)
        percentage = "%.3f%%" % percentage
        percent_received.append(percentage)

    winner = max(votes_received)
    index = votes_received.index(winner)
    winner_candidate = Candidates[index]

# Print results into the Terminal
print("Election Results")
print("------------------------")
print(f"Total votes: {str(total_votes)}")
print("------------------------")
for i in range (len(Candidates)):
    print(f"{Candidates[i]}: {str(percent_received[i])} ({str(votes_received[i])})")
print("------------------------")
print(f"Winner: {winner_candidate}")
print("------------------------")


# Export the output to .txt file
output = open("PyPoll output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(Candidates)):
    line = str(f"{Candidates[i]}: {str(percent_received[i])} ({str(votes_received[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winner_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))

