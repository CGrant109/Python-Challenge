import os
import csv
#Used for printing the analysis onto a txt file
import sys

budget_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store data
date = []
profit_loss = []
total = 0
month_change = []
biggest_increase = []
biggest_decrease = []



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
        

#defining the budget csv as f, to create a for loop that provides each monthly change
with open(budget_csv) as f:
    lines = f.readlines()

#finding the month change by creating a for loop
    month_change = [ int(profit_loss[x]) - int(profit_loss[x-1]) for x in range(1,len(profit_loss))]

 #indentifying the biggest increase and decrease montly change via max/min    
    biggest_increase = max(month_change)
    biggest_decrease = min(month_change)






print("Financial Analysis")
print("----------------------")
#total months
print(f'Total Months: {len(date)}')
total = sum(profit_loss)
#sum of profit/losses
print(f'Total: ${total}')

#the list of month-over-month changes: print(month_change)
#print the average of the changes
print(f"Average Change: ${round(sum(month_change)/len(month_change),2)}")

print("Greatest Increase in Profits: ", max(month_change))

print("Greatest decrease in Profits: ", min(month_change))


#Zip lists together
cleaned_csv = zip(date, profit_loss)

# Set variable for output file
output_file = os.path.join("budget_final.txt")

#Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

#pushing the results to a txt file format
sys.stdout = open("budget_final.txt", "w")

print("Financial Analysis")
print("----------------------")
print(f'Total Months: {len(date)}')
print(f'Total: ${total}')
print(f"Average Change: ${round(sum(month_change)/len(month_change),2)}")
print("Greatest Increase in Profits: ", max(month_change))
print("Greatest decrease in Profits: ", min(month_change))

sys.stdout.close()


















        
    


 


