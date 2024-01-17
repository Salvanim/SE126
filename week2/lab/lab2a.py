#W2LAB

#Prompt:
    #Write a program that displays all rooms that are over the maximum limit of people and the number of people that have to be notified that 
    #they will have to be put on the wait list. 
    #After the file is completely processed the program should display the number of records processed and the number of rooms that are over the limit.

#import csv libarary
import csv

#initialize varriables
total_records = 0
amountOverLimit = 0

with open("week2\lab\lab2a.csv") as csvfile:
    #must indent when connected to and reading the file

    #defines fileContent
    file = csv.reader(csvfile)

    #Header
    print(f"{'Room':20} \t{' Max'}\t{' Min'}\t{'Over'}")

    #accesses all rows withing csv
    for rec in file:
        if int(rec[1]) < int(rec[2]):
            print(f"{rec[0]:20}\t{rec[1]}\t{rec[2]}\t {int(rec[2])-int(rec[1])}")
            amountOverLimit += 1
        #itterates amount of records
        total_records += 1
    
    print(f"\n\nProccessed {total_records} records")
    print(f"Their are {amountOverLimit} rooms over the limit")