import csv

with open('instagram.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    list = []
    for row in csv_reader:
        if row[7] != '':
            # print()
            list.append([row[2], row[5], row[7]])
    print(list)
