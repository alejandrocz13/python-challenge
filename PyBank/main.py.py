# import modules
import os
import csv

# import the path and define it as a variable
# open the csv file with the permissions
PyBank = os.path.join(".", "resources", "budget_data.csv")

# define variables to hold values, and empty lists to hold strings, read rows and output them at the end
months_total = []
net_total = []
profits = []
monthYear = []
change = 0
value = 0
net_total = 0
months_total = 0
average = 0

with open(PyBank, "r", encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
#  read after first row, and be able to track the average change later
    first_row = next(csvreader)
    value = int(first_row[1])

# Define the operations of the variables    
    for row in csvreader:
        monthYear.append(row[0])
        
        net_total += int(row[1])
        months_total = months_total + 1

        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])

    average = sum(profits) / len(profits)

    great_increase = max(profits)
    great_index = profits.index(great_increase)
    great_date = monthYear[great_index]

    great_decrease = min(profits)
    worst_index = profits.index(great_decrease)
    worst_date = monthYear[worst_index]

# print the results to the Terminal
print("Financial Analysis for PyBank")
print("-------------------------------------")
print(f"Total months: {str(months_total)}")
print(f"Total: ${str(net_total)}")
print(f"Average Change: ${str(round(average, 2))}")
print(f"Greatest increase in Profits: {str(great_date)} (${str(great_increase)})")
print(f"Greatest decrease in Profits: {str(worst_date)} (${str(great_decrease)})")


# export to text file
output = open("PyBank Text Output.txt", "w")

line1 = ("Financial Analysis for PyBank")
line2 = ("-------------------------------------")
line3 = str(f"Total months: {str(months_total)}")
line4 = str(f"Total: ${str(net_total)}")
line5 = str(f"Average Change: ${str(round(average, 2))}")
line6 = str(f"Greatest increase in Profits: {str(great_date)} (${str(great_increase)})")
line7 = str(f"Greatest decrease in Profits: {str(worst_date)} (${str(great_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))