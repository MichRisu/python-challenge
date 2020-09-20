# Import the os and csv 
import os
import csv

# Create file path to access the file
csvpath = os.path.join('usc-la-data-pt-07-2020-u-c', 'O3-Python', 'Homework', 'Instructions','PyBank', 'Resources', 'budget_data.csv')

#Read using CSV module
with open(csvpath) as csvfile:
    pyBank_reader = csv.reader(csvfile, delimiter=',')
    print(pyBank_reader)