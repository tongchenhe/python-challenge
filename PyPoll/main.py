# import modules
import csv, os

# create paths for files to read and write
csvpath = os.path.join('Resources','election_data.csv')
txtpath = 'analysis.txt'

with open(csvpath) as csvfile:
    # create a csv reader for the file
    reader = csv.reader(csvfile, delimiter=',')

    # skip the header
    next(reader)

    # create an empty list of candidates to be added to
    candidate_list = []

    # another empty list for the vote count of each candidate
    candidate_vote = []

    # set default total vote to 0
    total_vote = 0

    # read through each line
    for line in reader:

        # add one vote each line
        total_vote += 1

        # check if current candidate is (not) included in the list
        if line[2] not in candidate_list:

            # add the new candidate and set his vote to 0
            candidate_list.append(line[2])
            candidate_vote.append(0)
        
        # add one vote to the candidate
        candidate_vote[candidate_list.index(line[2])] += 1

# find out the winner
winner = candidate_list[candidate_vote.index(max(candidate_vote))]

# print out results to terminal
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_vote}')
print('-------------------------')

# loop through candidate list
for i in range(len(candidate_list)):

    # find out how many percent of the total vote he/she has
    percent_vote = round(candidate_vote[i] / total_vote * 100,3)

    #print the candidate's result
    print(f"{candidate_list[i]}: {percent_vote}% ({candidate_vote[i]})")

print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')

# open text file to write to
with open(txtpath, 'w') as txtfile:
    # write result to the text file
    txtfile.write('Election Results\n')
    txtfile.write('-------------------------\n')
    txtfile.write(f'Total Votes: {total_vote}\n')
    txtfile.write('-------------------------\n')

    # loop through candidate list
    for i in range(len(candidate_list)):

        # find out how many percent of the total vote he/she has
        percent_vote = round(candidate_vote[i] / total_vote * 100,3)

        #print the candidate's result
        txtfile.write(f"{candidate_list[i]}: {percent_vote}% ({candidate_vote[i]})\n")

    txtfile.write('-------------------------\n')
    txtfile.write(f'Winner: {winner}\n')
    txtfile.write('-------------------------\n')