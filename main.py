import csv
import os

csvpath = os.path.join('Resources','budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    x = 0 
    total_profit = 0
    monthly_profit = []
    months = []

    for row in csvreader:
        if row[0] != "" and row[1] != "Profit/Losses":
            x += 1
            total_profit += int(row[1])
            monthly_profit.append(row[1])

        months.append(row[0])

    changes = []
    change = 0
    
    for i in range(len(monthly_profit)-1):
        change = int(monthly_profit[i+1])-int(monthly_profit[i])
        changes.append(change)

    total_changes = 0
    greatest_increase = 0 
    greatest_increase_month = 'NA'
    greatest_decrease_month = 'NA'
    greatest_decrease = 0 

    for j in range(len(changes)):
        total_changes += changes[j]
        if changes[j] > greatest_increase:
            greatest_increase = changes[j]
            greatest_increase_month = months[j]
        
        if changes [j] < greatest_decrease:
            greatest_decrease = changes[j]
            greatest_decrease_month = changes[j]
    
    average = total_changes/(x-1)

print('There are a total of '+ str(x) + ' number of months included in this dataset.')
print('Your net profit/losses is '+ str(total_profit)+'.')

print('The average change was '+ str(average) + '.')

print('Greatest decrease in profits: '+ str(greatest_decrease_month) +' ($' + str(greatest_decrease) +').')
print('Greatest increase in profits: '+ str(greatest_increase_month) +' ($' + str(greatest_increase) +').')

output = os.path.join('output.txt')

with open (output, 'w') as textfile:
    textfile.write(f"There are a total of {x} number of months included in this dataset.")
    textfile.write('\n')
    textfile.write(f"Your net profit/losses is {total_profit}.")
    textfile.write('\n')
    textfile.write(f"The average change was {average}.")
    textfile.write('\n')
    textfile.write(f"Greatest decrease in profits: {greatest_decrease_month} ${greatest_decrease})")
    textfile.write('\n')
    textfile.write(f"Greatest increase in profits: {greatest_increase_month} ${greatest_increase})")
    textfile.write('\n')
    
   