import csv
with open('data.csv','w') as fp:
	reader = csv.reader(fp)
	for row in reader:
		print(row)

