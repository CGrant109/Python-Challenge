import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

#lists
total_votes = []
individual_votes = {}
winner = []
candidate_list = ["Charles Casper Stockham: ","Diana Degett: ","Raymon_Anthony Doane: "]









#open and read csv
with open(election_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    #skipping header so not counted as value

    csv_header = next(csv_file)
    for row in csvreader:

        #add the total votes cast
        total_votes.append(row[0])
    



    


#to find each candidate vote count, we need to create a for loop
#for loop such act as (an n + 1) + (n) until it reaches a new candidate name





    


    


#complete a list of candidates who received votes
#we want to make lists of each invidual candidate, with their vote count
#store it in a dictionary, so we can go line by line and find average and sum of their votes

 












print("Financial Analysis")
print("----------------------")
print(f'Total Votes: {len(total_votes)}')
print("----------------------")





