# Import os and csv to start reading the csv file.
import os 
import csv

# Create the path to access the file
csvpath = os.path.join('Resources', 'budget_data.csv')

#Create empty lists
months = []
profit_losses = []
monthly_change = []

# Read using CSV module
with open(csvpath) as csvfile:

    # Set the variable and the delimiter
    pyBank_reader = csv.reader(csvfile, delimiter=',')
    # Set for loops to go back to top
    next(pyBank_reader)
    
    # Count total months in list
    for row in pyBank_reader:  
        months.append(row[0])
        profit_losses.append(int(row[1]))
    total_months = len(months)
    
    # Calculate net total amount of "Profit/Losses" over the entire period 
    net_total = sum(profit_losses)

    # Caluculate average of the changes in "Profit/Losses" over the entire period   
    for row in range(1, len(profit_losses)):
        monthly_change.append((int(profit_losses[row]) - int(profit_losses[row-1])))
    average_changes = sum(monthly_change)/(total_months)
    
    #Find the max profits, min losses and their dates
    max_profits = max(monthly_change)
    min_losses = min(monthly_change)

    max_month = months[monthly_change.index(max_profits) +1] 
    min_month = months[monthly_change.index(min_losses) + 1]
  
    # Print to terminal the results
    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_changes}")
    print(f"Greatest Increase in Profits: {max_month} (${max_profits})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_losses})")
    
    # Output to file
    file = open('Financial_Analysis.txt', 'w')
    file.write("Financial Analysis")
    file.write("---------------------------")
    file.write(f"Total Months: {total_months}")
    file.write(f"Total: ${net_total}")
    file.write(f"Average Change: ${average_changes}")
    file.write(f"Greatest Increase in Profits: {max_month} (${max_profits})")
    file.write(f"Greatest Decrease in Profits: {min_month} (${min_losses})")
    file.close()