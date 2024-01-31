import csv

#Dylan Fisher: W4 In Class Lab

#Prompt:
    #In Python, process the text file “lab4A_GOT_NEW.txt” to store each field into its own corresponding list

#Varriable Dictionary

    #recordTotal: defines amount of records

    #fname: list for first name values

    #lname : list for last name values

    #ages: list for first age values

    #nname: list for nick name values

    #hAlly: list for house alegiance values
    
    #houseMottos: dictionary between house alleinces and mottos
    
    #hMottos: list for house mottos
    
    #avg: defines current average age

#defines amount of records
recordTotal = 0

#list for first name values
fname = []

#list for last name values
lname = []

#list for age values
ages = []

#list for nickname values
nname = []

#list for house allience values
hAlly = []

#list for house mottos
hMottos = []

#dictionary between house alleinces and mottos
houseMottos = {
    "House Stark" : "Winter is Coming", 
    "House Baratheon" : "Ours is the fury",
    "House Tully" :  "Family. Duty. Honor",
    "Night's Watch" : "And now my watch begins.",
    "House Lannister" : "Hear me roar!",
    "House Targaryen" : "Fire & Blood"
}


#dictionary that contains house 
houseTallies = {
    "House Stark" : 0, 
    "House Baratheon" : 0,
    "House Tully" : 0,
    "Night's Watch" : 0,
    "House Lannister" : 0,
    "House Targaryen" : 0
}

#Opens and reads csv
with open("week4\lab4Indiv\lab4A_GOT_NEW.txt") as csvfile:
    #must indent when connected to and reading the file

    #defines fileContent
    file = csv.reader(csvfile)

    #itterates though records
    for rec in file:

        #Populates lists for each value in record
        fname.append(rec[0])
        lname.append(rec[1])
        ages.append(int(rec[2]))
        nname.append(rec[3])
        hAlly.append(rec[4])

        #Counts records
        recordTotal += 1


#Prints original header
print(f"\n{'First Name':10} \t {'Last Name':10} \t {'Age':10} \t {'Nickname':15} \t {'House Allegiance'}")

#PROCESS the lists --> for loop
#display the file data
for i in range(0, recordTotal):
    #Displays file data with spacing
    print(f"{fname[i]:10} \t {lname[i]:10} \t {str(ages[i]):10} \t {nname[i]:15} \t {hAlly[i]}")

#itterates though hAlly list to populate motto list and tally houses
for i in range(0, len(hAlly)):
    hMottos.append(houseMottos[hAlly[i]])
    houseTallies[hAlly[i]] += 1

#Reprints header with house mottos
print(f"\n{'First Name':10} \t {'Last Name':10} \t {'Age':10} \t {'Nickname':15} \t {'House Allegiance':5} \t {'House Mottos'}")

#display the file data
for i in range(0, recordTotal):
    print(f"{fname[i]:10} \t {lname[i]:10} \t {str(ages[i]):10} \t {nname[i]:15} \t {hAlly[i]:20} \t {hMottos[i]}")


#defines current average age
avg = 0

#itterates though ages list to calculate average
for i in range(0, len(ages)):
    avg += ages[i]

#devides avg to calculate rounded average
avg = round(avg/len(ages))

print(f"\nTotal People: {recordTotal}")
print(f"Average Age: {avg}")

#gets list of keys in houseTallies
houseTallyKeys = list(houseTallies.keys())
title = "\033[1m" + "Total Of Each House" + "\033[0m"
print("\n     " + title + f"\n   {'House':15} | Totals")

#ittertes to print each house tally
for i in range(0, len(houseTallyKeys)):
    print(f"{houseTallyKeys[i]:18} | {houseTallies[houseTallyKeys[i]]:3}")
