import csv
import webbrowser

#Dylan Fisher: Midterm

#Prompt:
    #For your Midterm Project in SE126 you will be building a program of your own design! You must work individually to design a program and file of your choosing.  The program must include the following:

    #a file to be read and processed, data stored into respective lists
        #.csv or .txt
    #import csv will work for both of these file types, but all data must be separated with a comma!
    #>= 2 lists
    #these can be populated from a file or by hand
    #showcase understanding of control flow structures
    #showcase understanding of self-built functions
    #Starting Documentation
    #include a brief program description
    #include a variable dictionary with data types including your lists!
    #Documentation for anything used not introduced in the course
    #Creativity!

#Varriable Dictionary

    #recordTotal: defines amount of records

    # titles : list contianing book titles
    # prices : list containing book prices
    # ratings : list containing book ratings
    # authors : list contianing book authors
    # yearsPublished : list contianing years of publicatoins
    # genres : list containing genres of books
    # urls: list of urls to book on amazon
    # bubbleSort: function that uses bubble sort algorithim to sort given array
    # greaterBubbleSort: function that uses bubble sort algorithim to sort given 2d array based of sorting a given array

#Recurison works by calling a function within itself:
    #This would run in a infinite loop without a condition that allows for the functoin to stop being called
    #Helpful in situations where their is a unknown value, such as when it is not known how many times a loop needs to run
    #

#function that uses bubble sort algorithim to sort given array
def bubbleSort(arrayToSort):

    #varribe that is 0 if firstValue was never greater than secondValue, and 1 otherwise
    wasGreater = 0
    for i in range(1, len(arrayToSort)):
        #defines values to compare
        firstValue = arrayToSort[i-1]
        secondValue = arrayToSort[i]

        #checks if for greater value
        if firstValue > secondValue:

            #swaps so greate value is second
            arrayToSort[i] = firstValue
            arrayToSort[i-1] = secondValue

            #defines that greater was determined
            wasGreater = 1
            
    #recursivly runs algorithim untile firstValue never greater than second
    if wasGreater == 1:
        arrayToSort = bubbleSort(arrayToSort)
    return arrayToSort

#function that uses bubble sort algorithim to sort given 2d array based of sorting a given array
def greaterBubbleSort(given2D,arrayToSort):

    #varribe that is 0 if firstValue was never greater than secondValue, and 1 otherwise
    wasGreater = 0
    for i in range(1, len(arrayToSort)):
        #defines values to compare
        firstValue = arrayToSort[i-1]
        secondValue = arrayToSort[i]

        first2D = given2D[i-1]
        second2D = given2D[i]

        #checks if for greater value
        if firstValue > secondValue:

            #swaps so greater value is second
            arrayToSort[i] = firstValue
            arrayToSort[i-1] = secondValue
            
            #swaps 2d
            given2D[i] = first2D
            given2D[i-1] = second2D

            #defines that greater was determined
            wasGreater = 1
            
    #recursivly runs algorithim untile firstValue never greater than second
    if wasGreater == 1:
        given2D = greaterBubbleSort(given2D, arrayToSort)

    return given2D

def sequenceSearch(searchTerm, arrayToSearch):
    for i in range(0, len(arrayToSearch)):
        if arrayToSearch[i] == searchTerm:
            return i
    return -1

def findAllIndexs(searchTerm, arrayToSearch, indexes = []):
    searched = sequenceSearch(searchTerm, arrayToSearch)
    if searched > 1:
        indexes.append(searched)
        del arrayToSearch[searched]
        indexes = findAllIndexs(searchTerm, arrayToSearch, indexes)
    else:
        return indexes
#defines amount of records
recordTotal = 0

#list contianing book titles
titles = []

#list containing book prices
prices = []

#list containing book ratings
ratings = []

#list contianing book authors
authors = []

#list contianing years of publicatoins
yearsPublished = []

#list containing genres of books
genres = []

#list of urls to book on amazon
urls = []

#2D array containing file values
fileValues = []

#Opens and reads csv
with open("midterm/100TrendingBooks.csv") as csvfile:
    #must indent when connected to and reading the file

    #defines fileContent
    file = csv.reader(csvfile)
    #itterates though records
    for rec in file:

        #skips first value in record, is only the index
        #Populates lists
        titles.append(rec[1])
        prices.append(float(rec[2]))
        ratings.append(float(rec[3]))
        authors.append(rec[4])
        yearsPublished.append(int(rec[5]))
        genres.append(rec[6])
        urls.append(rec[7])
        fileValues.append([rec[1], float(rec[2]), float(rec[3]),rec[4],int(rec[5]),rec[6],rec[7]])
        
        #Counts records
        recordTotal += 1


print(greaterBubbleSort(fileValues, yearsPublished)[0])