#W3D1 Demo - text file handling & storying to 1D lists

import csv

#total counter for all records
total_records = 0

#Header
print(f"\n{'Type':8} {'Brand':8} {'CPU':6} {'RAM':6} {'1st Disk':6} {'No HDD':6} {'2nd Disk':6} {'OS':6} {'YR':6}")

with open("week3/demo/lab2b.csv") as csvfile:

    file = csv.reader(csvfile)
    
    for rec in file:
       
        #print(rec[0]) #shows as LIST -> []

        #keep track of the rec count in the file
        total_records += 1
        #total_records = total_records + 1
        #FILTER for DISPLAY-----------------
        #--comp type-- rec[0]
        if rec[0] == "D":
            comp_type = "Desktop"
        elif rec[0] == "L":
            comp_type = "Laptop"
        else:
            #only happens if file has unexpected value
            comp_type = "*ERROR --" + str(rec[0])

        #--manufacturer-- rec[1]
        if rec[1] == "DL":
            manu = "Dell"
        elif rec[1] == "GW":
            manu = "Gateway"
        elif rec[1] == "HP":
            manu = rec[1]
        else:
            #only happens if file has unexpected value
            manu = "*ERROR --" + str(rec[1])

        #--processor / ram / hdd_1 / num_hdd - exact from file
        processor = rec[2]
        ram = rec[3]
        hdd_1 = rec[4]
        num_hdd = rec[5]

        #--hdd_2 / os / year
        if rec[5] == "1":
            hdd_2 = "   " #"---"  #"none"
            os = rec[6]
            year = rec[7]

        elif rec[5] == "2":
            hdd_2 = rec[6]
            os = rec[7]
            year = rec[8]

        else:
            hdd_2 = "*ERROR -- " + str(rec[5])
            os = "ERROR"
            year = "ERROR"

        #finalprint for each record
        print(f"{comp_type:8} {manu:8} {processor:6} {ram:6} {hdd_1:10} {num_hdd:6} {hdd_2:6} {os:6} {year:6}")
#----DISCONNECTED FROM FILE-------------------------------------------

print(f"TOTAL AMOUNT OF COMPUTERS: {total_records}")
