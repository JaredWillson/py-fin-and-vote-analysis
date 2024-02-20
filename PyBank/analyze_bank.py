# First we'll import the osd module so we can create file paths and the module for reading CSV's
import os
# We will also import the csv module to help us read text files
import csv

# Store the file path associated with our data file into a variable
budget_file = os.path.join('.', 'Resources', 'budget_data.csv')

# First, we need to open the file in read mode
with open(budget_file,'r') as budget:

    # So, the files is open, but not in a text form that is readable to use, so...
    csv_reader = csv.reader(budget, delimiter=',')
    line_count = 1
    greatest_increase = -1000000000 
    greatest_decrease = 1000000000
    prior_month = 0
    greatest_month = ''

    # Now, let's create a 'for' loop to run through all the lines
    for row in csv_reader:
        # We are going to loop through all the CSV lines and keep a running total of transactions
        # We will also count up the total rows, but we need to skip the first row since it is a header
        #  Note for later improvement... I'm not accounting for the possibility that all months are negative
        #     or that all months might be positive. For calculating greatest/worst months assuming a mix.
        if line_count == 1: # This is our header line--we just increment the line counter and move on
            line_count = line_count + 1
        # For our first month, there will be no prior month calculations, so we just ineed to update 
        # our running total profit/loss and then set the prior month starting value for the next row
        elif line_count == 2: 
            totvalue = int(row[1])
            monthly_change = 0
            total_change = 0
            prior_month = int(row[1]) #Sets our first 'prior month' value for all future rows
            line_count = line_count + 1
        else:
            # Now we need to calculate the change from the prior month's profit or loss...
            # Because we are on the third line, so we HAVE a change from the prior month
            # So, we'll start by calculating our monthly_change
            monthly_change = int(row[1]) - prior_month
            if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                greatest_month = row[0]
            if monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                worst_month = row[0]
            # Now we need to reset our prior month for the next row calculations
            total_change = total_change + monthly_change # This is our running total on monthly change
            prior_month = int(row[1]) # This resets our monthly change for the next loop
            totvalue = totvalue + int(row[1]) # Running total on profit and loss
            line_count = line_count +1
            # Now we need to calculate the average change
            # We take the total change dividied by the number of months that had a prior month
            # Which is three less than our current row count
            average_change = round((float(total_change))/(float(line_count-3)), 2)
    print()
    print('Financial Analysis')
    print('--------------------------')
    # To calculate total months, we use our current line count (which has been incremented one past
    # the end of our data) and subtract out two--one for incrementing past the end, one for the header
    print(f'Total Months: {line_count - 2}') #We are subtracting two since the header row doesn't count
    print(f'Total:  ${totvalue}') #Prints the running total
    print(f'Average Change: {average_change}')
    print(f'Greatest Increase in Profits: {greatest_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {worst_month} (${greatest_decrease})')
    print()
