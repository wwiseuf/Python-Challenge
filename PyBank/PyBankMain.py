import os
import csv
import statistics

PyBankcsv = os.path.join("Resources/PyBank.csv")



# Lists to store data
Total_Months = []
Total_Net = []
Average_Changes = []
GreatestIncreaseAmount = []
GreatestDecreaseAmount = []


# open
with open(PyBankcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader, None)

    for row in csvreader:
       
        # Add Total Months
        Total_Months.append(row[0])
       
        # Total Net Price
        Total_Net.append(int(row[1]))
    
    # average change
    for x in range(len(Total_Net)-1):
        Average_Changes.append(Total_Net[x+1]-Total_Net[x])

       
       
        GreatestIncrease = max(Average_Changes)
        GreatestDecrease = min(Average_Changes)


# Get the min/max change
GreatestIncreaseAmount = (Average_Changes.index(GreatestIncrease)) + 1
GreatestDecreaseAmount = (Average_Changes.index(GreatestDecrease)) + 1 


# Print loop info
print("Financial Analysis")
print("==========================")
print(Total_Months, Total_Net)
print(len(Total_Months))
print(sum(Total_Net))
print(f"Average Change: {round(sum(Average_Changes)/len(Average_Changes),2)}")
print(f"GreatestIncrease change: {Total_Months[GreatestIncreaseAmount]} (${((GreatestIncrease))})")
print(f"GreatestDecrease change: {Total_Months[GreatestDecreaseAmount]} (${((GreatestDecrease))})")


# export,  print & add line break
output_file = os.path.join("Analysis/Results.txt") 

with open(output_file, "w") as Results:

    Results.write( f"Financial Analysis\n"
                   f"==========================\n"
                   f"{Total_Months} | {Total_Net}\n"
                   
                   f"{len(Total_Months)}\n"
                   
                   f"{sum(Total_Net)}\n"
                   
                   f"Average Change: {round(sum(Average_Changes)/len(Average_Changes),2)}\n"
                   
                   f"GreatestIncrease change: {Total_Months[GreatestIncreaseAmount]} (${((GreatestIncrease))})\n"
                   
                   f"GreatestDecrease change: {Total_Months[GreatestDecreaseAmount]} (${((GreatestDecrease))})\n"
                   
                   f"Does my Company Qualify for a Government Bail out?"
)