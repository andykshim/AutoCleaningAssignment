import csv
from brother import brother
from cleanings import cleanings

brother_list = []

#importing brothers
with open('inputs/brothers_master.csv', 'r') as brother_file:
    brother_reader = csv.reader(brother_file)
    next(brother_reader)

    for line in brother_reader:
        brother_list.append(brother(line[0],line[1],line[2],line[3],line[4]))

#import outputted weekly cleaning
with open('output/weekly_cleaning.csv', 'r') as assigned_file:
    assigned_reader = csv.reader(assigned_file)

    for line in assigned_reader:
        updatedNum = line[2]
        name = line[1]

        for brother in brother_list:
            nameOnFile = brother.first + " " + brother.last
            if name == nameOnFile:
                brother.num = updatedNum


with open('inputs/brothers_master.csv', 'w', newline = '') as brother_file:
    brother_writer = csv.writer(brother_file)
    brother_writer.writerow(["First", "Last", "livesIn", "dishes", "num"])

    for row in brother_list:
        brother_writer.writerow([row.first, row.last, row.livesIn, row.dishes, row.num])
