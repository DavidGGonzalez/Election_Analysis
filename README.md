# Election Audit
## Overview
A colorado Board of Elections employee gave me the following task to complete the congressional election audit of a recent local congressional election.

1. Calculate the Total number of votes cast.
2. Get a complete list of counties where votes were cast.
3. Calculate the total number of votes on each county.
4. Calculate the percentage of votes for each county.
4. Get a complete list of candidates who received votes.
5. Calculate the total number of votes each candidate received.
6. Calculate the percentage of votes each candidate won.
7. Determine the winner of the election based on popular vote.
8. Write all election results to the ***election_results.txt*** file so it can be distribute.

## Resouces
- Data Source: a `CSV` file called ***election_results.csv***
- Software: Python 3.9.9, Visual Code: 1.62.3

## Audit Results
The ananlysis of the election show that:
### Total votes
__369,711__

### County votes
- Jefferson: __10.5%__ (38,855)
- Denver: __82.8%__ (306,055)
- Arapahoe: __6.7%__ (24,801)

### Largets county turnout
- __Denver__

### Candidates and votes cast along with their percentage
- Charles Casper Stockham: __3.1%__ (11,606)
- Diana DeGette: __3.1%__ (11,606)
- Raymon Anthony Doane: __3.1%__ (11,606)

### Winning Candidate
* Winner: __Diana DeGette__
* Winning Vote Count: __272,892__
* Winning Percentage: __73.8%__

![Election Analysis Results](/Resources/Election_Analysis_Results.png)

## Audit Summary
It is clear that this process could be used to audit any other election process, changes might be required to accomodate for other file names and/or location, perhaps to standarize the `CSV` file structure to facilitate the use of this tool, otherwise it might require a reformat so the process runs correctly.
