#written for Sigma Nu Gamma Theta
#Andrew Shim
#July 2023


import csv
import random
from brother import brother
from cleanings import cleanings


cleaning_list = []
brother_list = []

output_list = []

#importing cleanings
with open('inputs/cleanings_master.csv', 'r') as cleaning_file:
    cleaning_reader = csv.reader(cleaning_file)
    next(cleaning_reader)

    for line in cleaning_reader:
        cleaning_list.append(cleanings(line[0],line[1],line[2], line[3]))

#importing brothers
with open('inputs/brothers_master.csv', 'r') as brother_file:
    brother_reader = csv.reader(brother_file)
    next(brother_reader)

    for line in brother_reader:
        brother_list.append(brother(line[0],line[1],line[2],line[3],line[4]))


#returns a list of elligible brothers by credentials + lowest number of cleanings. 
def eligibleList(cleaning, brother_list):
    listToReturn = []

    #sunday morning cleanings (all can do)
    if cleaning.canLiveOuts == True:
        min = 10000
        for brother in brother_list:
            if brother.num < min:
                min = brother.num

        for brother in brother_list:
            if brother.num == min:
                listToReturn.append(brother)
    
    else:

        #dishes (live ins & needs to know how to do dishes)
        if cleaning.isDishes == True:
            min = 10000
            for brother in brother_list:
                if brother.dishes == True and brother.num < min:
                    min = brother.num
            for brother in brother_list:
                if brother.dishes == True and brother.num == min:
                    listToReturn.append(brother)

        #during week cleanings (live ins)
        else:
            min = 10000
            for brother in brother_list:
                if brother.livesIn == True and brother.num < min:
                    min = brother.num
            for brother in brother_list:
                if brother.livesIn == True and brother.num == min:
                    listToReturn.append(brother)     

    return listToReturn


for cleaning in cleaning_list:
    shortList = eligibleList(cleaning, brother_list)
    brotherChosen =  shortList[ random.randint(0, len(shortList) - 1) ]
    brotherChosen.num += 1
    output_list.append([cleaning, brotherChosen])


translatedList = []
for line in output_list:
    translatedList.append([line[0].name, line[1].first + " " + line[1].last, line[1].num])


with open("output/weekly_cleaning.csv", 'w', newline = '') as csv_file:
    csv_writer = csv.writer(csv_file)

    for row in translatedList:
        csv_writer.writerow(row)