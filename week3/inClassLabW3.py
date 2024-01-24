#Dylan Fisher: W3 In Class Lab

#Prompt:
    #Your CIO (Chief Information Officer) has asked you to determine how much it would cost the company to replace all machines that are from 2016 and earlier. He plans on spending not more than $2,000 dollars for desktops and $1,500 for laptops.  Store the data from the file lab3a.csv into lists.  Then process the lists to reprint all of the file information (exactly as you did in Lab 2) and also produce an end report that lists the number of desktops that will be replaced, the cost to replace the desktops, the number of laptops that will be replaced, and the cost to replace the laptops.
#Varriable Dictionary

    #recordTotal: defines amount of records

    #deskSpendMax: defines maximum spending amount for desktops

    #lapSpendMax: defines maximum spending amount for laptops

    #desktopTotalCost: defines total cost to replace desktops

    #laptopTotalCost: defines total cost to replace laptop

    #desktopAmount: defines amount of desktops

    #laptopAmount: defines amount of laptop

    #typeList: defines list that contians thge type of all computers

    #brandList: defines list that contians the brand of all computers

    #cpuList: defines list that contians the cpu of all computers

    #ramList: defines list that contians the ram of all computers

    #firstDiskList: defines list that contians the first disk of all computers

    #noHDDList: defines list that contians value of the HDD of all computers

    #secondDiskList: defines list that contians the second disk of all computers

    #osList: defines list that contians the os of all computers

    #yearList: defines list that contains the year of creation for all computers
    

#import csv libarary
import csv

#initialize varriables

#defines amount of records
recordTotal = 0

#defines maximum spending amount for desktops
deskSpendMax = 2000

#defines maximum spending amount for laptops
lapSpendMax = 1500

#defines total cost to replace desktops
desktopTotalCost = 0

#defines total cost to replace laptop
laptopTotalCost = 0

#defines amount of desktops
desktopAmount = 0

#defines amount of laptops
laptopAmount = 0

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


with open("week3\lab3a.csv") as csvfile:
    #must indent when connected to and reading the file

    #defines fileContent
    file = csv.reader(csvfile)

    #accesses all records withing csv
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


        #Checks if year is 2016 or earlier
        if int(yearList[len(yearList)-1]) <= 16:

            #Checks if computers is desktop or laptop
                #Increments varribles assosationg to desktop and laptops
            if rec[0] == 'D':
                desktopTotalCost += deskSpendMax
                desktopAmount += 1
            elif rec[0] == 'L':
                laptopTotalCost += lapSpendMax
                laptopAmount += 1
        
        #increments recordTotal
        recordTotal += 1

#Prints content of csv
for index in range(0, recordTotal):
    print(f"\n{typeList[index]:8} {brandList[index]:8} {cpuList[index]:6} {ramList[index]:6} {firstDiskList[index]:10} {noHDDList[index]:6} {secondDiskList[index]:6} {osList[index]:6} {yearList[index]:6}")

#Prints replacment costs
print(f"\nTo Replace {desktopAmount} it will cost $ {desktopTotalCost:8}")

print(f"\nTo Replace {laptopAmount} it will cost $ {laptopTotalCost:8}\n")