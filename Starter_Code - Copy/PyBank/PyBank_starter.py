# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
filepath = "Resources/budget_data.csv"
file_to_output = "analysis/budget_analysis.txt" 


# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
last_month_profit = 0
curr_month_profit = 0
total_change = 0

max_change = 0
max_month = ""
min_change = 0
min_month = ""

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list


    # Track the total and net change


    # Process each row of data
    for row in reader:
        print (row)
        # Track the total


        # Track the net change


        # Calculate the greatest increase in profits (month and amount)


        # Calculate the greatest decrease in losses (month and amount)



# Calculate the average net change across the months


# Generate the output summary


# Print the output


# Write the results to a text file
#with open(file_to_output, "w") as txt_file:
    #txt_file.write(output)
