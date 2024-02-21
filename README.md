# Financial Analysis and Vote Analysis #

## Contents: ##

This repository contains two python scripts. 

[![image] (Images/revenue-per-lead.png)]

The first script, analyze_bank.py, contains code
to  summarize corporate performance by month over multiple years. It counts the total number of records in the source file (ignoring header lines), determines the total change, determines
Average change from previous month, and tracks and stores the best and worst month. Results are written to the screen and to a text file.

The first script is stored in the PyBank subdirectory. The results file is stored in the analysis subdirectory below PyBank. The source data are stored in the Resources subdirectory below PyBank.


The second python script, countVote.py, reviews vote data from a source CSV file, counts the votes by candidates, reports out the results including total votes, votes per candidate, and percentage vote by candidate rounded to three decimal places. At the end, it determines the winner of the election. If the contest ended in a tie, it will not list any winners and will just announce that it is a tie. Results are written to the screen and to a results file.

The second script is stored in the PyPoll subdirectory. The results file is stored in the analysis subdirectory below PyPoll. The source data are stored in the Resources subdirectory below PyPoll.


## Code Sources ##

The code for the loop in the vote counter that adds the vote counts into a dictionary was based upon a routine provided by instructor Kevin Lee in an extra session at the end of class
demonstrating how to populate a dictionary from a csv file.
