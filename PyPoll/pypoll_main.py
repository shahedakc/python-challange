#pypoll hw

import csv

#the csv and the py code was stored in the same folder

file = ('election_data.csv')
exfile = ('final_election.txt') 

#variables

total_votes = 0
candi_unique = []
candi_votes = []
percent = []
max_votes = candi_votes[0]
max_index = 0


with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)


    for r in csvreader:
        total_votes = total_votes + 1
        
        candi_in = (r[2]) 
        
        if candi_in in candi_unique:
            candi_index = candi_unique.index(candi_in)
            candi_votes[candi_index] = candi_votes[candi_index] + 1
        else:
            candi_unique.append(candi_in)
            candi_votes.append(1)

#find the percent of votes for each candidate

for x in range(len(candi_unique)):
    vote_pct = round(candi_votes[x]/total_votes*100, 2)
    percent.append(vote_pct)
    
    if candi_votes[x] > max_votes:
        max_votes = candi_votes[x]
        max_index = x

election_winner = candi_unique[max_index] 

#print results on terminal

print('Election Results')
print(f'Total Votes: {total_votes}')

for x in range(len(candi_unique)):
    print(f'{candi_unique[x]} : {percent[x]}% ({candi_votes[x]})')

print(f'Election winner: {election_winner.upper()}')

#print results on a text file 

with open(output_file, "w", newline="") as datafile:
    datafile.write('Election Results\n')
    
    datafile.write(f'Total Votes: {total_votes}\n')
   
    for x in range(len(candi_unique)):
        datafile.write(f'{candi_unique[x]} : {percent[x]}% ({candi_votes[x]})\n')
    
    datafile.write(f'Election winner: {election_winner.upper()}\n')
    
    
