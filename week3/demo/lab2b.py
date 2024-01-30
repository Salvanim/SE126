#Dylan Fisher: Lab#3 Homework : W3D1 Demo - text file handling & storying to 1D lists

#Prompt:
    #Rewrite the Voter Registration Lab utilizing the data from the file voters.csv.  Store the field data into respective 1D lists, and then process the lists to determine the 4 final output values (make sure they are clearly labeled!). This final solution should have NO input() statements and when the console is ran it should print all 4 totals (you may reprint the data from the lists/fie if you would like)  Use your original Voter Registration Lab (or the solution file!) as starter code, but edit it to connect to a file and store data into lists, then use a for loop to process each voter and their data to find the 4 totals.

#Varriable Dictionary

    #total_records: defines amount of records

    #typeList: defines list that contians thge type of all computers

    #brandList: defines list that contians the brand of all computers

    #cpuList: defines list that contians the cpu of all computers

    #ramList: defines list that contians the ram of all computers

    #firstDiskList: defines list that contians the first disk of all computers

    #noHDDList: defines list that contians value of the HDD of all computers

    #secondDiskList: defines list that contians the second disk of all computers

    #osList: defines list that contians the os of all computers

    #yearList: defines list that contains the year of creation for all computers
    

import csv

#total counter for all records
total_records = 0

#defines list that contians types of all computers
typeList = []

#defines list that contians the brand of all computers
brandList = []

#defines list that contians the cpu of all computers
cpuList = []

#defines list that contians the ram of all computers
ramList = []

#defines list that contians the first disk of all computers
firstDiskList = []

#defines list that contians value of the HDD of all computers
noHDDList = []

#defines list that contians the second disk of all computers
secondDiskList = []

#defines list that contians the os of all computers
osList = []

#defines list that contains the year of creation for all computers
yearList = []

#Header
print(f"\n{'Type':8} {'Brand':8} {'CPU':6} {'RAM':6} {'1st Disk':6} {'No HDD':6} {'2nd Disk':6} {'OS':6} {'YR':6}")

with open("week3/demo/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)
    
    for rec in file:
        
        #Appends all record values to lists
        typeList.append(rec[0])
        brandList.append(rec[1])
        cpuList.append(rec[2])
        ramList.append(rec[3])
        firstDiskList.append(rec[4])
        noHDDList.append(rec[5])

        #accounts for length inconsitancy
        if rec[5] == "1":
            secondDiskList.append("   ")
            osList.append(rec[6])
            yearList.append(rec[7])

        elif rec[5] == "2":
            secondDiskList.append(rec[6])
            osList.append(rec[7])
            yearList.append(rec[8])

        #print(rec[0]) #shows as LIST -> []

        #keep track of the rec count in the file
        total_records += 1
        #total_records = total_records + 1
        

#Prints content of csv
for index in range(0, total_records):

    #FILTER for DISPLAY-----------------
    #--comp type-- rec[0]
    if typeList[index] == "D":
        typeList[index] = "Desktop"
    elif typeList[index] == "L":
        typeList[index]  = "Laptop"
    else:
        #only happens if file has unexpected value
        typeList[index] = "*ERROR --" + str(typeList[index])

    #--manufacturer-- rec[1]
    if brandList[index] == "DL":
        brandList[index] = "Dell"
    elif brandList[index] == "GW":
        brandList[index] = "Gateway"
    elif brandList[index] == "HP":
        brandList[index] = brandList[index]
    else:
        #only happens if file has unexpected value
        brandList[index] = "*ERROR --" + str(brandList[index])

    print(f"\n{typeList[index]:8} {brandList[index]:8} {cpuList[index]:6} {ramList[index]:6} {firstDiskList[index]:10} {noHDDList[index]:6} {secondDiskList[index]:6} {osList[index]:6} {yearList[index]:6}")
#----DISCONNECTED FROM FILE-------------------------------------------

print(f"\nTOTAL AMOUNT OF COMPUTERS: {total_records}")
