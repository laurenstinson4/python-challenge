import os
import csv

#Path to collect data from Resources folder
PyBank_path = os.path.join('Resources', 'budget_data.csv')

#Print header on analysis screen
print("Financial Analysis")
print("-----------------------------")

#Open text file
text_file = open("Financial Analysis.txt", "w")

# Read in the CSV file
with open(PyBank_path) as csvfile:

	#Split the data on commas
	PyBank = csv.reader(csvfile, delimiter=',')

	#Skip header row
	next(csvfile)

	#Initiate arrays for looping
	total_ProfitLoss = []
	date = []
	monthly_change = []
	

	#Begin loop to...
	for row in PyBank:

		#...check for number of months
		date.append(row[0])

		#...calculate total of profit/losses
		total_ProfitLoss.append(float(row[1]))

	#Print results
	print("Total Months: " + str(len(date)))
	print("Total: $" + str(sum(total_ProfitLoss)))

	
	#Begin loop to...
	for i in range(1, len(total_ProfitLoss)):

		#...calculate monthly average change
		monthly_change.append(total_ProfitLoss[i] - total_ProfitLoss[i-1])
		avg_change = sum(monthly_change) / len(monthly_change)

		#...calculate greatest increase/decrease of profits
		max_change = max(monthly_change)
		min_change = min(monthly_change)

		#...calculate months of greatest increase/decrease of profits
		max_change_date = str(date[monthly_change.index(max(monthly_change))])
		min_change_date = str(date[monthly_change.index(min(monthly_change))])


	#Print results
	print("Average Change: $" + str(round(avg_change)) )
	print("Greatest Increase in Profits: " + max_change_date + " ($" + str(max_change) + ")")
	print("Greatest Decrease in Profits: " + min_change_date + " ($" + str(min_change) + ")")


	#Writing to text file
	print("Financial Analysis", file=text_file)
	print("-----------------------------", file=text_file)
	print("Total Months: " + str(len(date)), file=text_file)
	print("Total: $" + str(sum(total_ProfitLoss)), file=text_file)
	print("Average Change: $" + str(round(avg_change)), file=text_file)
	print("Greatest Increase in Profits: " + max_change_date + " ($" + str(max_change) + ")", file=text_file)
	print("Greatest Decrease in Profits: " + min_change_date + " ($" + str(min_change) + ")", file=text_file)