import os
import csv
import operator

#Path to collect data from Resources folder
PyPoll_path = os.path.join('Resources', 'election_data.csv')

#Print header on analysis screen
print("Election Results")
print("-----------------------------")

#Open text file
text_file = open("Election Results.txt", "w")

# Read in the CSV file
with open(PyPoll_path) as csvfile:

	#Split the data on commas
	PyPoll = csv.reader(csvfile, delimiter=',')

	#Skip header row
	next(csvfile)

	#Initiate starting statements and array/dictionary for looping
	total_votes = 0
	candidates = []
	individual_votes = {}

	#Begin loop to...
	for row in PyPoll:

		#...calculate total number of votes
		total_votes = total_votes + 1

		#...find unique candidate names by using If/Else statement
		#...plus find number of votes per candidate
		if row[2] not in candidates:
			candidates.append(row[2])
			individual_votes[row[2]] = 1

		else:
			individual_votes[row[2]] = individual_votes[row[2]] + 1


	#Print total votes on analysis screen
	print("Total Votes: " + str(total_votes))
	print("-----------------------------")

	#Find and print results of votes for each individual candidate
	for candidate_name in individual_votes:
		print(candidate_name + " " + str(round(((individual_votes[candidate_name]/total_votes)*100))) + "%" + " (" + str(individual_votes[candidate_name]) + ")")

	print("-----------------------------")
	
	#Find the WINNER!
	winner = max(individual_votes, key=individual_votes.get)
	print("Winner: " + winner)
	print("-----------------------------")

	#Writing to text file
	print("Election Results", file=text_file)
	print("-----------------------------", file=text_file)
	print("Total Votes: " + str(total_votes), file=text_file)
	print("-----------------------------", file=text_file)
	for candidate_name in individual_votes:
		print(candidate_name + " " + str(round(((individual_votes[candidate_name]/total_votes)*100))) + "%" + " (" + str(individual_votes[candidate_name]) + ")", file=text_file)
	print("-----------------------------", file=text_file)
	print("Winner: " + winner, file=text_file)
	print("-----------------------------", file=text_file)
	