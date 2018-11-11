import csv

with open('instagram.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    list = []
    first_line = True
    for row in csv_reader:
        if row[7] != '':
            if first_line:
                first_line = False
                continue
            question = row[4][row[4].index("!")+2:row[4].index("?")+1]
            list.append([row[2], row[5], row[7], question])
    print(list)
