#Imports and Variables
#-----------------------------------------------------------------
import os
import csv
votes = []
candidates = []
candidatestats = []
polls = []
winner = ""
count = 0
#Path to data file
csvpath = os.path.join('..','Resources', 'election_data.csv')
#Path to output file
outputpath = os.path.join('..','Outputs','election_results.txt')
#-----------------------------------------------------------------


#Reading CSV and Manipulating Data
#-----------------------------------------------------------------
with open(csvpath) as election_data_file:
    election_data = csv.reader(election_data_file, delimiter=',')
    election_data_header = next(election_data)
    for row in election_data:
        votes.append(row[2])
    totvotes = len(votes)
    candidates = set(votes)

def polling(totvotes,candidates,count,candidatestats,polls):
    for candidate in candidates:
        for vote in votes:
            if candidate == vote: 
                count+=1
        percentage = round(((count/totvotes)*100),3)
        candidatestats=[candidate,percentage,count]
        polls.append(candidatestats)
        count=0
        percentage=0
        candidatestats=[]
    return polls
    
#-----------------------------------------------------------------


#Printing results to Terminal and Output File
#-----------------------------------------------------------------
print()
print("Election Results")
print("---------------------------")

#The total number of votes cast
print("Total Votes: " + str(totvotes))
print("---------------------------")

#Printing the rest:
polling(totvotes,candidates,count,candidatestats,polls)
polls.sort(key=lambda x: x[1], reverse=True)
for stats in polls:
    print(stats[0]+': '+str(stats[1])+'% ('+str(stats[2])+')')
print("---------------------------")
winnerstats=[]
winnerstats = polls[0]
print("Winner: " + winnerstats[0])
print("---------------------------")
print()

#Printing to output file:
with open(outputpath,'w') as output:
    output.write("Election Results\n")
    output.write("---------------------------\n")
    output.write("Total Votes: " + str(totvotes)+'\n')
    output.write("---------------------------\n")
    for ostats in polls:
        output.write(ostats[0]+': '+str(ostats[1])+'% ('+str(ostats[2])+')\n')
    output.write("---------------------------\n")
    output.write("Winner: " + winnerstats[0]+'\n')
    output.write("---------------------------\n")

#-----------------------------------------------------------------