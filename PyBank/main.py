import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")
result_path = os.path.join("analysis", "budget_analysis.txt")
# Variables
flag_previous = 0
change = 0
# output
total_number_month = 0
net_total_profit = 0
change_profit = 0
total_change_profit = 0
greatest_inc = ["", 0]
greatest_dec = ["", 0]

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    for row in csvreader:
        total_number_month += 1
        net_total_profit += int(row[1])
        change = int(row[1]) - flag_previous
        if flag_previous == 0:
            change = 0
        flag_previous = int(row[1])
        change_profit += change

        # increase
        if change > int(greatest_inc[1]):
            greatest_inc[0] = row[0]
            greatest_inc[1] = change
        # decrease
        if change < int(greatest_dec[1]):
            greatest_dec[0] = row[0]
            greatest_dec[1] = change

    total_change_profit = change_profit / (total_number_month - 1)
    #console output
    print('Financial Analysis:')
    print('-----------------------------------')
    print('Total Months:'+str(total_number_month))
    print('Total:'+str(net_total_profit))
    print('Average Change: $'+str(total_change_profit))
    print('Greatest Increase in Profits:' +
          greatest_inc[0]+' - '+str(greatest_inc[1]))
    print('Greatest Decrease in Profits:' +
          greatest_inc[0]+' - '+str(greatest_dec[1]))
    #write to file
    with open(result_path, "w") as results:
        results.write('Financial Analysis:')
        results.write('\n-----------------------------------')
        results.write('\nTotal Months:'+str(total_number_month))
        results.write('\nTotal:'+str(net_total_profit))
        results.write('\nAverage Change: $'+str(total_change_profit))
        results.write('\nGreatest Increase in Profits: ' +
                      greatest_inc[0]+' - '+str(greatest_inc[1]))
        results.write('\nGreatest Decrease in Profits: ' +
                      greatest_inc[0]+' - '+str(greatest_dec[1]))
