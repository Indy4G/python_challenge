#Imports and Variables
#-----------------------------------------------------------------
import os
import csv
mons = []
prof = []
netprof = 0
netprofchange = 0
netprofchangeavg = 0
maxprof = 0
maxprofmon = ""
maxloss = 0
maxlossmon = ""
#Path to data file
csvpath = os.path.join('..','Resources', 'budget_data.csv')
#Path to output file
outputpath = os.path.join('..','Outputs','finantial_analysis.txt')
#-----------------------------------------------------------------


#Reading CSV and Manipulating Data
#-----------------------------------------------------------------
with open(csvpath) as budget_data_file:
    budget_data = csv.reader(budget_data_file, delimiter=',')
    budget_data_header = next(budget_data)
    for row in budget_data:
        mons.append(row[0])
        netprof+=int(row[1])
        prof.append(int(row[1]))
    
    for i in range(len(mons)-1):
        netprofchange+=(prof[i+1]-prof[i])
        if (prof[i+1]-prof[i])>maxprof:
            maxprof=prof[i+1]-prof[i]
            maxprofmon=mons[i+1]
        elif (prof[i+1]-prof[i])<maxloss:
            maxloss=prof[i+1]-prof[i]
            maxlossmon=mons[i+1]
    netprofchangeavg+=(netprofchange/(len(mons)-1))
#-----------------------------------------------------------------


#Printing results to Terminal and Output File
#-----------------------------------------------------------------
print()
print("Finantial Analysis")
print("---------------------------")

# The total number of months included in the dataset
print("Total # of Months: " + str(len(mons)))

# The net total amount of "Profit/Losses" over the entire period
print("Net Total Profit: $" + str(netprof))

# The average of the changes in "Profit/Losses" over the entire period
print("Average Monthly Change in Profit/Loss: $" + str(round(netprofchangeavg,2)))

# The greatest increase in profits (date and amount) over the entire period
print("Month of Greatest Profit: " + maxprofmon + " $" + str(maxprof))

# The greatest decrease in losses (date and amount) over the entire period
print("Month of Greatest Loss: " + maxlossmon + " $" + str(maxloss))

#To output file:
with open(outputpath,'w') as output:
    output.write("Finantial Analysis\n")
    output.write("-------------------------------\n")
    output.write("Total # of Months: " + str(len(mons))+'\n')
    output.write("Net Total Profit: $" + str(netprof)+'\n')
    output.write("Average Monthly Change in Profit/Loss: $" + str(round(netprofchangeavg,2))+'\n')
    output.write("Month of Greatest Profit: " + maxprofmon + " $" + str(maxprof)+'\n')
    output.write("Month of Greatest Loss: " + maxlossmon + " $" + str(maxloss)+'\n')
#-----------------------------------------------------------------