import os
import csv
import statistics

csvpath=os.path.join('PyPoll','Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    py_poll=[row for row in csvreader]
    ballot_id=[row[0] for row in py_poll]
    county=[row[1] for row in py_poll]
    candidates=[row[2] for row in py_poll]
    total_vote_count=len(py_poll)
    Stockham_votecount=candidates.count("Charles Casper Stockham")
    DeGette_votecount=candidates.count("Diana DeGette")
    Doane_votecount=candidates.count("Raymon Anthony Doane")
    winner=statistics.mode(candidates)


print("Election Results")
print("--------------------------")
print(f'Total Votes: {total_vote_count}')
print("--------------------------")
print(f'Charles Casper Stockham: {round(((Stockham_votecount/total_vote_count)*100),3)}% ({Stockham_votecount})')
print(f'Diana DeGette: {round(((DeGette_votecount/total_vote_count)*100),3)}% ({DeGette_votecount})')
print(f'Raymon Anthony Doane: {round(((Doane_votecount/total_vote_count)*100),3)}% ({Doane_votecount})')
print("--------------------------")
print(f'Winner: {winner}')
print("--------------------------")


output_path = os.path.join('PyPoll','analysis','pypoll_analysis.csv')
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results",""])
    csvwriter.writerow(["--------------"])
    csvwriter.writerow(["Total Votes::", total_vote_count])
    csvwriter.writerow(["--------------"])
    csvwriter.writerow(["Charles Casper Stockham:", f'{round(((Stockham_votecount/total_vote_count)*100),3)}% ({Stockham_votecount})'])
    csvwriter.writerow(['Diana DeGette:', f'{round(((DeGette_votecount/total_vote_count)*100),3)}% ({DeGette_votecount})'])
    csvwriter.writerow(['Raymon Anthony Doane:', f'{round(((Doane_votecount/total_vote_count)*100),3)}% ({Doane_votecount})'])
    csvwriter.writerow(["--------------"])
    csvwriter.writerow(['Winner:', winner])



