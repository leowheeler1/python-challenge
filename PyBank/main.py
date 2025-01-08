# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
totalmoney = 0
# Add more variables to track other necessary financial data
currmonth = ""                          # tracks month for biggest increase/decrease
currmoney = 0                           # tracks current profit/loss
netchange = 0                           # tracks net changer
n = 1                                   # iteration for length of data (total months)
bigchange = 0                           # keeps track of biggest gain
bigmonth = ""
smallchange = 0                         # keeps track of biggest loss
smallmonth = ""
lastmoney = 0                           # previous amount for net change
net_change_list = []                    # list of net changes for average change

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
    # Process each row of data
    for row in reader:
        currmonth = row[0]               # current month
        currmoney = int(row[1])          # current profit/loss
        # Track the total
        totalmoney += int(currmoney)

        # Track the net change
        netchange = currmoney - lastmoney
        net_change_list.append(netchange)

        if currmoney > bigchange:         # keeps track of largest month (biggest gain)
            bigchange = currmoney
            bigmonth = row[0]
        elif currmoney < smallchange:     # keeps track of smallest month (biggest loss)
            smallchange = currmoney
            smallmonth = row[0]

        lastmoney = currmoney             # previous value for net change
        n += 1                            # iteration




# Calculate the average net change across the months
ovrnetchange = (sum(net_change_list)/n)

# Generate the output summary
output = [
    "Financial Analysis",
    "-----------------------",
    f"Total Months: {n}",
    f"Total: {totalmoney}",
    f"Greatest Increase in Profits: {bigmonth} ({bigchange})",
    f"Greatest Decrease in Profits: {smallmonth} ({smallchange})"]


# Print the output
for i in range(6):
    print(output[i])

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    for i in range(6):
        if i == 5:
            txt_file.write(output[5])          # skips the new line for the last row of data
        else:
            txt_file.write(output[i] + "\n")   # adds a new line so that the text is readable
