#Dylan Fisher: Final Lab

#Prompt:
    #Write a program that can be used by a small theater to sell tickets for performances.  The theater’s auditorium has 15 rows of seats with 30 seats in each row. The program should display a screen that shows which seats are available and which are taken.  Seats thar are available are represented by # and seats that are taken are represent by a *. 

    

#import csv libarary
import csv

with open("finalLab\seats.csv") as csvfile:
    #must indent when connected to and reading the file

    #defines fileContent
    file = csv.reader(csvfile)
    recIndex = 0
    #accesses all records withing csv
    for rec in file:
        if recIndex > 0 and recIndex < 16:
            print(rec)
        recIndex += 1
