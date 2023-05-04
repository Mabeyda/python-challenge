import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")
result_path = os.path.join("analysis", "election_analysis.txt")
#variables
votes = []
flag_winner = 0
#output
total_votes = 0
winner = ''
percentages = []
with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total_votes +=1
        votes.append(row[2])
canditates = ['Diana DeGette', 'Charles Casper Stockham', 'Raymon Anthony Doane']
total_candidates = len(canditates)
#Totals        
for canditate in canditates:
    count = 0    
    for vote in votes:
        if vote==canditate:
            count+=1
    percentage = count/total_votes # average      
    total = [canditate,percentage,count]
    if count>flag_winner:
        flag_winner = count
        winner = canditate
    percentages.append(total)  

print('Election Results')
print('-----------------')
print('Total Votes: '+str(total_votes))
print('-----------------')
for per in percentages:
    print(per[0]+':'+str(round(per[1]*100,3))+' ('+str(per[2])+')')
print('-----------------')
print('Winner: '+winner)
 #write to file
with open(result_path, "w") as results:
    results.write('\nElection Results')
    results.write('\n-----------------')
    results.write('\nTotal Votes: '+str(total_votes))
    results.write('\n-----------------')
    for per in percentages:
        results.write('\n'+per[0]+':'+str(round(per[1]*100,3))+' ('+str(per[2])+')')
    results.write('\n-----------------')
    results.write('\nWinner: '+winner)




