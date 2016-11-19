import csv

reader=csv.reader(open('GB.txt', 'r'), delimiter='\t')
writer=csv.writer(open('GB_nodups.csv', 'w'), delimiter=',')

placenames = set()
for row in reader:
    if row[2] not in placenames:
        writer.writerow(row)
        placenames.add( row[2] )