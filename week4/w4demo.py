import csv

#Dylan Fisher: W4 In Class Lab

#Prompt:
    #Write a program that reads the data file (below) and stores the data into 1D parallel lists (remember, one list for every field).  Once the lists are populated (and the file is "closed"), process the lists to reprint the file data, record by record as they originally appear in the file.

#Varriable Dictionary

    #recordTotal: defines amount of records

    #fname: list for first name values

    #lname : list for last name values

    #test1: list for first test values

    #test2: list for second test values

    #test3: list for third test values


#defines amount of records
recordTotal = 0


#list for first name values
fname = []

#list for last name values
lname = []

#list for first test values
test1 = []

#list for second test values
test2 = []

#list for third test values
test3 = []

#Calculate and store each students average test score
avg = 0
total_count = 0
average = []


#Opens and reads csv
with open("week4/files/listPractice1.txt") as csvfile:
    #must indent when connected to and reading the file

    #defines fileContent
    file = csv.reader(csvfile)

    #itterates though records
    for rec in file:

        #Populates lists for each value in record
        fname.append(rec[0])
        lname.append(rec[1])
        test1.append(int(rec[2]))
        test2.append(int(rec[3]))
        test3.append(int(rec[4]))

        #Counts records
        recordTotal += 1


#Prints original header
print(f"{'First Name':10} \t {'Last Name':10} \t {'Test 1':10} \t {'Test 2'} \t {'Test 3'}")

#PROCESS the lists --> for loop
#display the file data
for i in range(0, recordTotal):
    #len() --> returns LENGTH of (item) -> for lists, it is the # of items in the list

    #Displays file data with spacing
    print(f"{fname[i]:10} \t {lname[i]:10} \t {test1[i]:5} \t {test2[i]:12} \t {test3[i]:12}")

#Itterates though lists to calculate average
for i in range(0, len(fname)):
    #calculate avg for student
    avg = (test1[i] + test2[i] + test3[i])/3
    #append this avg to the average list
    average.append(avg)

#displays the students's fname and the test average
print(f"\n{'FIRST':12}\t{'AVERAGE'}")
for i in range(0, len(fname)):
    print(f"{fname[i]:12} \t {average[i]:3.1f}")


#SEQUENTIAL SEARCH - "in sequence" --> for beginning THOUGH the end\
low_name = ""
low_avg = 100 #start with highest value to drop to find the lowest

for i in range(0, len(average)):

    #determine if current average is lower than current low_avg
    if average[i] < low_avg:
        low_avg = average[i] #current average is lower so becomes new low value
        low_name = fname[i]

print(f"\nSTUDENTS IN FILE: {len(fname)}")
print(f"LOWEST AVERAGE: {low_name} - {low_avg:.1f}")

#DISPLAY: total students in file:
