#pybank hw 
import csv

file = ("budget_data.csv")
exfile = ("final_budget_data.txt")

# variables 
months = []
profit = []
change = []
 
with open(file, newline="", encoding="utf-8") as budget:
    csvreader = csv.reader(budget,delimiter=",") 
    header = next(csvreader)  

    
    for r in csvreader: 
        months.append(r[0])
        profit.append(int(r[1]))

    
    for i in range(len(profit)-1):
        change.append(profit[i+1]-profit[i])
        
# Obtain the max and min of the the montly profit 
inc = max(change)
dec = min(change)

inc = change.index(max(change)) + 1
dec = change.index(min(change)) + 1 

# Print 
print("Financial Analysis")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change)/len(change),2)}")
print(f"Greatest Increase in Profits: {months[inc]} (${(str(inc))})")
print(f"Greatest Decrease in Profits: {months[dec]} (${(str(dec))})")

#print financial analysis on text doc
with open(exfile,"w") as file:  

    file.write("Financial Analysis")
    file.write(f"Total Months: {len(months)}")
    file.write("\n")
    file.write(f"Total: ${sum(profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(change)/len(change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {months[inc]} (${(str(inc))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {months[dec]} (${(str(inc))})")