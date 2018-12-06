#This script analyses the file election_data.csv in the Resources folder
import os
import csv
#Set the file path for import
source_path = os.path.join('Resources', 'election_data.csv')

#Read the csv file into a dataset
with open(source_path, newline='') as f:
    dataset = csv.reader(f, delimiter=',')

#Create place holders for the data output
    candidates = [] #Will hold unique list of all candidates
    votes_per_candidate = [] #Will hold the total votes per candidate
    percentages = [] #Will hold the percentage of total votes per candidate
    total_votes = 0 #Will iterate through data and total number of votes
    output_lines = [] #Will hold formatted output data for each candidate

    for row in dataset:
        total_votes += 1
        #If a candidate has not yet been added to the list, add them
        if row[2] not in candidates:
            candidates.append(row[2])
            votes_per_candidate.append(1)
        #Otherwise, add one for the candidate in the same index in the votes list
        else:
            votes_per_candidate[candidates.index(row[2])] += 1
   
    #After totals have been calculated, determine the percentage of votes per candidate
    for item in candidates:
        pct = (votes_per_candidate[candidates.index(item)] * 100/total_votes)
        pct = format(pct, '.3f') #Formats to three decimals
        percentages.append(pct)
   
    #Return the name of the candidate with max votes
    winner = candidates[votes_per_candidate.index(max(votes_per_candidate))]
    
    #Zip up the three lists for easier output
    election_results=zip(candidates, percentages, votes_per_candidate)
   
    #Format each item in the zipped list into a new list
    for i in election_results:
        output_lines.append(i[0] + ": " + str(i[1]) + "% (" + str(i[2]) + ")")
    output_lines.pop(0)
    #Print the formatted data to the terminal
    output1 = (f"Election Results\n-------------------------\nTotal Votes: {total_votes}\n-------------------------\n")
    output2 = (f"-------------------------\nWinner: {winner}\n-------------------------\n")

    print(output1)
    print(*output_lines, sep='\n')
    print(output2)

    with open('election_results.txt', 'w') as f:
        f.write(output1)
        for line in output_lines:
            f.write(line + '\n')
        f.write(output2)
        f.close()