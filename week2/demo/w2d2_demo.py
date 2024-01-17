#W2D2 - Text File Opening Review + 1D Lists

#import csv libarary
import csv

#initialize varriables
total_records = 0
#create empty lists for each field
fnames = []
lnames = []
favenums = []
faveanimals = []

with open("week2/demo/w2d2_demoTextFile.txt") as csvfile:
    #must indent when connected to and reading the file

    #defines fileContent
    file = csv.reader(csvfile)

    #accesses all rows withing csv
    for rec in file:

        print(rec)
        #append field to proper lists
        fnames.append(rec[0])
        lnames.append(rec[1])
        favenums.append(int(rec[2]))
        if len(rec) == 4:
            faveanimals.append(rec[3])
        else:
            faveanimals.append("---")

        #itterates amount of records
        total_records += 1
        
#process fnames + favanimals list to dipslay
for index in range(0,len(fnames)):
    print(f"{fnames[index]}'s fave animal is: {faveanimals[index]}")
