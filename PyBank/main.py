# import modules
import os, csv

# create path to read from and write to
csvpath = os.path.join('Resources', 'budget_data.csv')
txtpath = 'analysis.txt'

# open csv file
with open(csvpath, 'r') as csvfile:
    # creates a csv reader
    reader = csv.reader(csvfile, delimiter=',')

    # skip the header
    next(reader)

    # set the default value of the following to 0 or an empty string
    total_months, total_budget = 0, 0
    greatest_inc, greatest_dec = 0, 0
    inc_month, dec_month = '', ''

    # read through each line of the csv file
    for line in reader:
        
        # convert the change of budget from string to int
        change = int(line[1])
        print(change)

        # add 1 to total month while reading each line
        total_months += 1

        # add the month's budget to the total
        total_budget += change

        # check if current month's profit is greater than the previous greatest increase
        if change>greatest_inc:

            # if so, update the value and the month to current ones
            greatest_inc = change
            inc_month = line[0]

        # check if current month's profit is lower than the previous greatest decrease
        if change<greatest_dec:

            # if so, update the value and the month to current ones
            greatest_dec = change
            dec_month = line[0]

    # calculate the average of change and round it to 2 decimal places
    average_change = round(total_budget / total_months, 2)

    # print out the results to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_budget}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {inc_month} (${greatest_inc})")
    print(f"Greatest Decrease in Profits: {dec_month} (${greatest_dec})")

# open(create) the text file and write the results
with open(txtpath, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_budget}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits: {inc_month} (${greatest_inc})\n")
    txtfile.write(f"Greatest Decrease in Profits: {dec_month} (${greatest_dec})\n")
        

