#Dylan Fisher
#202420_SE126.10 Intermediate Prog Using Python

#Program Purpose:
#Write a program that displays all rooms that are over the maximum limit of people
#and the number of people that have to be notified that they will have to be put on the wait list.
#After the file is completely processed the program should display the number of records processed
#and the number of rooms that are over the limit.

#import csv library for text file handling functions
import csv

#Counts total amount of records
recTotal = 0

#Counts amount of rooms over limit
overTotal = 0

#connect to the file!
with open("ClassLab#2\lab2a.csv") as csvFile:

    #read the file - access
    file = csv.reader(csvFile)

    #print Header
    print(f"\n{'Room':20}\t {'Max'}\t {'Min'}\t{'Over'}")


    #Loop though records in file
    for rec in file:

        #Calcualtes amount over the maximum of the amount of people registered
        calculatedOver = int(rec[2])-int(rec[1])

        #Displays Rooms with too many registered people
        if calculatedOver > 0:

            #Prints each aspect of room to stay inline with header
            print(f"{rec[0]:20}\t{rec[1]}\t{rec[2]}\t {abs(calculatedOver)}")

            #Increments overTotal
            overTotal += 1

        #Increments recTotal
        recTotal += 1

    #prints number of total processed records
    print(f"\n\nProcessed {recTotal} records")

    #prints number of rooms over their limit
    print(f"Their are {overTotal} rooms over the limit.\n")
