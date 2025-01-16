# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
input_path = os.path.join("resources", "budget_data.cvs")
output_path = os.path.join("analysis", "budget_analysis.text")


# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
net_change_list = []
month_list = []
greatest_increase = ['', 0]
greatest_decrease = ['',0]



# Open and read the csv
with open(file_to_load) as financial_data:
    os.chdir(os.path.dirname(os.path.realpath(_file_)))
    with open(Imput_path) as csv_file:
        reader = csv.reader(csv_file)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
first_row = next(reader)

    # Track the total and net change
total_months += 1
total_net += int(first_row[1])
previous_net = int(first_row[1])

    # Process each row of data
for row in reader:
        total_months += 1
        total_net += int(row[1])
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
