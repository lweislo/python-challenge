import os
import csv
import logging
from statistics import mean

filepath = os.path.join("Resources", "budget_data.csv")

with open(filepath, newline='') as csvfile:

    # reading in the data to variable csvreader with delimiter comma
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row first
    csv_header = next(csvreader)

    #Set up the starting values for our statistics
    month_count = 0
    net_total = 0
    net_change = []
    change_month = []
    last_value = 0

    for row in csvreader:

        budget = int(row[1])
        month_count += 1
        #Calculate the total budgets in the dataset on a rolling basis
        net_total = net_total + budget
        
        #Calculate the difference between current value and previous value
        if last_value != 0:
            month_data = (budget - last_value)
        #append the net change to the list
            net_change.append(month_data)
        #append the current month
            change_month.append(row[0])
        #now set the current budget to last_value to compare in the next iteration
        last_value = budget
    #Calculate the average budget, max and min changes and grab the month
    #using the same index as net_change on the change_month list
    avg_change = round(sum(net_change)/(month_count - 1), 2)
    max_profit = max(net_change)
    max_position = change_month[net_change.index(max(net_change))]
    min_profit = min(net_change)
    min_position = change_month[net_change.index(min(net_change))]
    
   #Prepare the file for output 
    #output_path = os.path.join("..", "output", "budget.txt")
    with open('budget.txt', 'w') as f:
    
        output = (f"""Financial Analysis \n--------------------\nTotal Months: {month_count} \nTotal: ${net_total} \nAverage Change: $ {avg_change} \nGreatest Increase in Profits: {max_position} (${max_profit}) \nGreatest Decrease in Profits: {min_position} (${min_profit}) \n """)

        print(output)
        f.write(output)
    
        f.close()
