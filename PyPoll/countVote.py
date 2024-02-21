# We will start by bringing in the modules we need for 'relative paths' and for 'csv file manipulation'
import os
import csv

# Now, let's define our (currently empty) vote counter dictionary...
votesDict={}

# Now, we will specify the path to the file that is storing our data
votesFile = os.path.join('Resources', 'election_data.csv')

# Next, we open the file in read mode
with open(votesFile,'r') as votes:
    csvReaderBot = csv.reader(votes, delimiter=',')

    # We need to move past our first row...
    csv_header = next(csvReaderBot)
    # And set a starting vote count...
    voteCount = 0

    # Now we will read through all the rows in the vote tally file.
    # First, we increment our total vote count by one for each row
    # as we will need the total vote count to determine percentages at the end
    # If we find a name in the third column that is not yet in our dictionary--a new vote getter
    # We assign that name a vote
    # If that name was already in our dictionary (from one or more previous lines), we add one more to their vote tally.
    for row in csvReaderBot:
         voteCount = voteCount+1
         name=row[2]
         if name in votesDict:
               votesDict[name] = votesDict[name]+1
         else:
               votesDict[name] = 1
    
output_file = os.path.join("analysis", "voteResults.txt")

# We have read in our total counts and associated each count with a name in our dictionary...
# Now we need to tabulate our results and write them out to the terminal and to a results file
# First, we open our results file using a 'with' statement so it will close automatically
with open(output_file, 'w') as results:
    
    # Now we will print out the results. 
    print()
    print('Election Results')
    print('-------------------------')

    # voteCount was the variable storing our line total (and thus our total votes cast)
    print(f'Total Votes:  {voteCount}')
    print('-------------------------')
    results.write('Election Results\n')
    results.write('-------------------------\n')
    results.write(f'Total Votes:  {voteCount}\n')
    results.write('-------------------------\n')

    # Now we need to both print out each name and their count and also calculate a winner in the same for loop
    # We will start by setting a variable 'greatestCount' to a value of zero
    # Then, as we read out each entry in the dictionary, we will compare the count to the current greatest value
    # And if it is bigger, we will set that person as our current leader
    # Else, move on to the next candidate
    greatestCount = 0
    for name in votesDict.keys():
        print(f'{name}: {(votesDict[name]/voteCount)*100:.3f}% ({votesDict[name]})')
        results.write(f'{name}: {(votesDict[name]/voteCount)*100:.3f}% ({votesDict[name]})\n')
        # Now, we check to see if this candidate has more votes than the highest previous candidate
        if votesDict[name] > greatestCount:
            greatestCount = votesDict[name]
            winner = name
        # Note that there is a remote chance of a tie.  In this case we would not want to declare a winner
        # so we set our 'winner' variable to the string value 'Tie'
        elif votesDict[name] == greatestCount:
            winner = 'Tie!'
    print('-------------------------')
    print(f'Winner: {winner}')
    print('-------------------------')
    results.write('-------------------------\n')
    results.write(f'Winner: {winner}\n')
    results.write('-------------------------')