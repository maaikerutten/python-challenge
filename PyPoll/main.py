# Import os mudule and module for reading CSV files 
import os
import csv

# Import the Pandas library
import pandas as pd

# Path to collect data from the Resources folder and read csv
election_data_df = pd.read_csv('C:\\Users\\maaik\\USCLOS201811DATA3\\03_python\\homework\\Instructions\\PyPoll\\Resources\\election_data.csv')

# print the head of the data frame
election_data_df.head(10)

# total number of votes
total_votes = election_data_df['Voter ID'].count()

print (total_votes)

# list of candidates 
list_candidates = election_data_df.Candidate.unique()

print(list_candidates)

# % of votes per candidate & total number of votes per candidate

votes_candidate = election_data_df.groupby('Candidate').size().to_frame('counts')
votes_candidate['perc_candidate']= votes_candidate['counts']/votes_candidate['counts'].sum()

print(votes_candidate)

# election winner via popular vote
winner = election_data_df['Candidate'].value_counts().idxmax()

print(winner)

# results, every record on new line, rounded 2 decimals for average and 0 decimals for max in min
results = ("Election Results \n"
+ "-------------------------------\n"
+ "Total Votes: " + str(total_votes) + "\n" 
+ "-------------------------------\n"     
+ str(votes_candidate)  + "\n"            
+ "-------------------------------\n"
+ "Winner: " + winner + "\n"
+ "--------------------------------\n") 

print(results)

# export results to text file and close file
text_file = open ("Election_Results_PyPoll.txt", "w")
text_file.write(results)
text_file.close()