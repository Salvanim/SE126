import csv

#Dylan Fisher: Midterm

#Prompt:
    #In this lab, you will build a Python application that allows a user to repeatedly choose an option from a menu to search through the data provided in the text file: lab5.txt
#Varriable Dictionary

    #recordTotal: defines amount of records

    
#---MAIN PROGRAM--------------------------------------------------------------------

#function for selecting option
def optionSelector(options):
    print("\nThese are your searching options: ")
        
    for i in range(0, len(options)):
        print(f"\n{i+1}. {options[i]}")
        
    selectedOption = ""
    while not selectedOption.isdigit():

        selectedOption = input("\nPlease select your searching option based by giving number: ")

        if selectedOption.isdigit():
            selectedOption = int(selectedOption)
            if not (selectedOption in list(range(1, len(options)+1))):
                print("\nNot a option, please try again: ")
                selectedOption = ""
                
        else:
            print("\nNot a number, please try again: ")

        selectedOption = str(selectedOption)

    selectedOption = int(selectedOption)
    return selectedOption
    
def menu():
    options = [
        "See All Student Report",
        "Search for a Student [ID]",
        "Search for a Student [Last]",
        "View a Class Roster [class1, class2, and class3]",
        "Exit/Quit Program",
    ]
    return optionSelector(options)


    
def seqSearch(searchTerm, searchLists):
    
    found = [] #allows for multiples in search
    seq_count = 0
    #for loop allows review of each value in list (sequence)
    for listIndex in range(0, len(searchLists)):
        searchList = searchLists[listIndex]
        for i in range(0, len(searchList)):
            seq_count += 1
            #ask if search value matches current value in list (search)
            if searchTerm.lower() == searchList[i].lower():
                #store found value's LOCATION (index)
                found.append(i)

    return found

def binarySearch(searchTerm, searchList):
    searchTerm = input("\nWhat do you want to search for?: ")
    min = 0 #first position of the list to be searched (ascending) 
    max = len(searchList) - 1 #last position of the list to be searched (ascending)
    #mid = int((0 + (len(searchList) - 1)) / 2)
    mid = int((min + max) / 2)
    bin_count = 0
    #this is for INCREASING (ascending) order
    while (min < max and searchTerm.lower() != searchList[mid].lower()):
        bin_count += 1
        if searchTerm.lower() < searchList[mid].lower():
            max = mid - 1
        else:
            min = mid + 1

        mid = int((min + max) / 2)
    return mid

def compleatBinarySearch(context, searchList, lists, spacing):
    searchQuestion = input(f"\nWhat {context} do you want to search for?: ")
    mid = binarySearch(searchQuestion, searchList)
    printList = ""
    for i in range(0, lists):
        print(f"{lists[i][mid]:^{spacing[i]}} \t {lists[i][mid]:^{spacing[i]}} \t {lists[i][mid]:^{spacing[i]}} \t {lists[i][mid]:^{spacing[i]}} \t {lists[i][mid]:^{spacing[i]}} \t {lists[i][mid]:^{spacing[i]}}")


#Varribles:
recordTotal = 0

#create empty 1D lists to hold data in text file
id_stud = []
lname = []
fname = []
class1 = []
class2 = []
class3 = []

with open("lab5\lab5_students.txt") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
    
        id_stud.append(int(rec[0]))
        lname.append(rec[1])
        fname.append(rec[2])
        class1.append(rec[3])
        class2.append(rec[4])
        class3.append(rec[5])
        recordTotal += 1

searchFile = 'y'
while searchFile == 'y':

    choice = int(menu())
    if choice == 1:

        print(f"\n {'ID':5} \t {'Last Name':8} \t {'First Name':10} \t {'Class 1':8} \t {'Class 2':8} \t {'Clsss 3':8}")
    
        for i in range(0, recordTotal):
            print(f"{id_stud[i]:5} \t {lname[i]:8} \t {fname[i]:10} \t {class1[i]:8} \t {class2[i]:8} \t {class3[i]:8}")
    
    elif choice == 2:
        compleatBinarySearch("ID", id_stud, [id_stud, lname, fname, class1, class2, class3], [5, 8, 10, 8, 8, 8])
    
    elif choice == 3:
        compleatBinarySearch("last name", lname, [id_stud, lname, fname, class1, class2, class3], [5, 8, 10, 8, 8, 8])
    
    elif choice == 4:
        classToSearch = input("\nWhat class would you want to search for?: ")
        foundStudents = seqSearch(classToSearch, [class1, class2, class3])

    else:
        searchFile = 'n'
        print("GoodBye!")