import os

import csv

budget_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
date = []
profit_loss = []
total = 0
month_change = []
previous_value = 0





# Open and read csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skipping header so not counted as a month
    csv_header = next(csvreader)
    for row in csvreader:

        #add month
        date.append(row[0])
        #add profit/loss
        profit_loss.append(int(row[1]))
        #find difference of month over month, and then find average






#total months
print(f'Total Months: {len(date)}')
total = sum(profit_loss)
#sum of profit/losses
print(f'Total: ${total}')

print(f'Average Change: ${month_change}')


# find the difference and store as a list, we'll find the sum the of the list
#  and / by the length of said list (to find the average)
#change in profit/loss over entire time period:





    

# # Zip lists together
# cleaned_csv = zip(date, profit_loss)

# for month in cleaned_csv:
#         count(month)
#         print(month)


# # Set variable for output file
# output_file = os.path.join("budget_final.csv")

# #  Open the output file
# with open(output_file, "w") as datafile:
#     writer = csv.writer(datafile)

























        
    


 


