# First we'll import the os module so we can create file paths and the module for managing CSV's
import os
import csv

# Store the file path associated with our data file into a variable
budget_file = os.path.join("Resources", "budget_data.csv")

# First, we need to open the file in read mode
with open(budget_file,'r') as budget:

    # So, the files is open, but not in a text form that is readable to use, so...
    csv_reader = csv.reader(budget, delimiter=',')
    # Our file has a header row, so we need to move past that
    csv_header = next(csv_reader)
    line_count = 1
    prior_month = 0

    # Now, let's create a 'for' loop to run through all the lines
    for row in csv_reader:
        # We are going to loop through all the CSV data lines and keep a running total of transactions
        # We will also count up the total rows so we can calculate an average
        # Note that for our first line, we won't have prior month calculations, we we just need to
        # update our running total profit/loss and then set the prior month starting value for the next row
        if line_count == 1:
            totvalue = int(row[1])
            monthly_change = 0
            total_change = 0
            prior_month = int(row[1]) #Sets our first 'prior month' value for all future rows
            line_count = line_count + 1
        else:
            # Now that we are past the first month, we need to calculate the change from the prior month's profit or loss...
            # So, we'll start by calculating our monthly_change
            monthly_change = int(row[1]) - prior_month
            # Now we need to see if this is our greatet monthly change to date...
            # If it is our first past through (second row), then it is necessarily our greatest monthly change since it's our only monthl change
            # so we can just set it as such; for all later rows, we will need to compare it to our 'leader in the clubhouse'
            if line_count == 2: 
                greatest_increase = monthly_change
                greatest_decrease = monthly_change
                greatest_month = row[0]
                worst_month = row[0]
            else:
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
            # Which is two less than our current row count since we have incremented our counter one past our last row,
            # and our first row of data doesn't count since it had no "prior month" record
            average_change = round((float(total_change))/(float(line_count-2)), 2)
    print()
    print('Financial Analysis')
    print('--------------------------')
    # To calculate total months, we use our current line count (which has been incremented one past
    # the end of our data) and subtract out two--one for incrementing past the end, one for the header
    print(f'Total Months: {line_count - 1}') #We are subtracting one since we have incremented our counter past the number of data lines
    print(f'Total:  ${totvalue}') #Prints the running total
    print(f'Average Change: {average_change}')
    print(f'Greatest Increase in Profits: {greatest_month} (${greatest_increase})')
    print(f'Greatest Decrease in Profits: {worst_month} (${greatest_decrease})')
    print()
   
# We have written the results to the terminal, but we also need to create a file that contains the same information
# First, we need to use the 'os' module to specify the relative file path and name
output_file = os.path.join("analysis", "results.txt")

# Now we will open the file, but using "write" mode instead of the default "read"
# I am not using any of the 'CSV' module tools since this is a text file result, not a comma delimited file
# We will just report the same "print" instructions as above, but with a "write" instruction instead
# As usual, we want to make sure the file automatically closes when we are done, so we are using the 'with' form
# Unlike with the 'print' statements above, there is no automatic new line when writing, so the backslash 'n' telles
# Python to add a carriage return at the end of each line
with open(output_file, 'w') as results_file:

    results_file.write('Financial Analysis\n')
    results_file.write('--------------------------\n')
    results_file.write(f'Total Months: {line_count - 1}\n')
    results_file.write(f'Total:  ${totvalue}\n')
    results_file.write(f'Average Change: {average_change}\n')
    results_file.write(f'Greatest Increase in Profits: {greatest_month} (${greatest_increase})\n')
    results_file.write(f'Greatest Decrease in Profits: {worst_month} (${greatest_decrease})')