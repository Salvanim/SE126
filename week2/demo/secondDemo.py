#import csv library for text file hanling functions
import csv

#initialize counting vars - founts from file
total_records = 0
total_salaries = 0

#initialize empty list - 1 list per FIELD
names = []
ages = []
salaries = []

#connect to the file!
with open("week2\demo\example.csv") as csvFile:

    #read the file - access
    file = csv.reader(csvFile)

    #Enter and "Read" each record in file

    #Itterates though records in file
    for record in file:
        #"for every record found in the file (entire row of feild data)"
        
        #display data VALUES in NEAT colums
        print(f"{record[0]:10} \t{record[1]:3} \t{float(record[2]):10.2f}")

        #store data from rec list (current record being read) to list
        #adding data to a list --. .append(); requires LIST NAME as starting object
        names.append(record[0]) #NAME
        ages.append(int(record[1])) #AGE
        salaries.append(float(record[2])) #SALARY

        #keep literal count of number of records
        total_records += 1

        #keep running total of salaries
        total_salaries += float(record[2])

#final total displays
print(f"TOTAL RECORDS: {total_records} | TOTAL SALARY: ${total_salaries:.2f}")

#proecess the lists to display the text file informatoin
#PROCESS LIST --> FOR LOOP!
for index in range(0, total_records):
    #for each value in the range of 0 to # of the times represented by total_records
    print(f"Index: {index} \t{names[index]} is {ages[index]} years old")

#process though teh lists to create total age value
total_age = 0

for index in range(0, total_records):
    #adds each age to a total age variable
    total_age += ages[index]

average_age = total_age / total_records

#age displays
print(f"TOTAL AGE: {total_age:4}")

print(f"AVERAGE AGE: {average_age}")