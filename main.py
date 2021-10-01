import csv
import os

csvpath = os.path.join('Resources','election_data.csv')
x = 0 
candidates_list = []
counts = []
percents = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)

    for row in csvreader:
        x += 1

        if row[2] not in candidates_list:
            candidates_list.append(row[2])
            counts.append(0)
    
        for i in range(len(candidates_list)):
                if row[2] == candidates_list[i]:
                    counts[i] += 1



print('Total Votes '+ str(x-1))

for i in range(len(candidates_list)):
    percents.append(100*counts[i]/(x-1))
    print(candidates_list[i] + ' '+ str(percents[i])+'%' + ' ('+str(counts[i])+ ')')

winner_count = 0
winner = ''

for i in range(len(counts)):
    if counts[i] > winner_count:
        winner_count = counts[i]
        winner = candidates_list[i]

print('Winner: '+ winner)

output = os.path.join('output.txt')

with open (output, 'w') as textfile:
    textfile.write(f"Total Votes: {x-1}")
    textfile.write('\n')
    for i in range(len(candidates_list)):
        textfile.write(f"{candidates_list[i]} {percents[i]}% ({counts[i]})")
        textfile.write('\n')
    textfile.write(f"Winner: {winner}")
    