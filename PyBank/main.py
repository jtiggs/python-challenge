
import os
import csv
import statistics

csvpath=os.path.join("PyBank","Resources","budget_data.csv")

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    csv_header=next(csvreader)
    py_bank=[row for row in csvreader]
    dates=[row[0] for row in py_bank]
    pnl=[int(row[1]) for row in py_bank]
    months=len(pnl)
    total=sum(pnl)
    change=[pnl[x]-pnl[x-1]for x in range(1,months)]
    avgchange=statistics.mean(change)
    biggest_increase=max(change)
    biggest_decrease=min(change)
    biggest_increase_month=(dates[(change.index(biggest_increase))+1])
    biggest_decrease_month=(dates[(change.index(biggest_decrease))+1])

print("Financial Analysis")
print("------------------------------------")
print(f'Total Months: {months}')
print(f'Total: ${total}')
print(f'Average Change: {"${:.2f}".format(avgchange)}')
print(f'Greatest Increase in Profits: {biggest_increase_month} (${biggest_increase})')
print(f'Greatest Decrease in Profits: {biggest_decrease_month} (${biggest_decrease})')

output_path = os.path.join("PyBank","analysis","PyBank_analysis.csv")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis",""])
    csvwriter.writerow([""])
    csvwriter.writerow(["Total Months:", months])
    csvwriter.writerow(["Total:", "${:.2f}".format(total)])
    csvwriter.writerow(["Average Change:", "${:.2f}".format(avgchange)])
    csvwriter.writerow(["Greatest Increase in Profits:", biggest_increase_month+" ($"+str(biggest_increase)+")"])
    csvwriter.writerow(["Greatest Decrease in Profits:", biggest_decrease_month+" ($"+str(biggest_decrease)+")"])



