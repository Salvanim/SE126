import csv

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

        #checks if first value greater value
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

#function itterates though list looking for exact search term, returns indexs of every value that matchs
def sequenceSearch(searchTerm, arrayToSearch):
    foundIndexs = []
    for i in range(0, len(arrayToSearch)):
        if arrayToSearch[i] == searchTerm:
            foundIndexs.append(i)
    return foundIndexs

#function itterates though list looking for content with search term, returns indexes of every value that matches
def contentSequenceSearch(searchTerm, arrayToSearch):
    foundIndexs = []
    for i in range(0, len(arrayToSearch)):
        if searchTerm in arrayToSearch[i]:
            foundIndexs.append(i)
    return foundIndexs

#funciton takes string and converts to lit of unicode values for each character in string
def stringToUnicodeValues(string):
    outputUnicode = []
    i = 1
    for s in string:
        outputUnicode.append(ord(s) * i)
        i += 1
    return outputUnicode

#funciton takes objects, gets string representation
#gets unicode values of each string
#determines difference between compareTo unicode and compare unicode
#returns sum of difference
def detrmineCompareativeValue(compare, compareTo):
    compare = str(compare)
    compareTo = str(compareTo)

    compareValues = stringToUnicodeValues(compare)
    compareToValues = stringToUnicodeValues(compareTo)

    if len(compareValues) < len(compareToValues):
        for i in range(0, len(compareToValues)):
            if i >= len(compareValues):
                compareValues.append(compareToValues[i])
    else:
        for i in range(0, len(compareValues)):
            if i >= len(compareToValues):
                compareToValues.append(compareValues[i])
    
    difference = []
    for i in range(0, len(compareToValues)):
        difference.append((compareToValues[i])-(compareValues[i]))
    
    return abs(sum(difference))

#function uses determineComparitiveValue function to populate list with comparisions values between a search term and values in given array
def getComparisonsOnSearch(searchTerm, arrayToSearch):
    comparisons = []
    for value in arrayToSearch:
        comparisons.append(detrmineCompareativeValue(value, searchTerm))
    return comparisons

#searches array for search term using comparisoin search function, then sorts sort array uses bubble sort
def searchSortComparison(searchTerm, sortArray, searchArray):
    return greaterBubbleSort(sortArray,getComparisonsOnSearch(searchTerm, searchArray))

#prints multiArray with heading based off of rowNames, and prints only to printTo value
def printMultiArray(rowNames, rowArrays, multiArray, printTo):

    generatedHeader = ""
    spacingList = []

    for i in range(0, len(rowNames)):
        maxRowNum = max([len(str(r)) for r in rowArrays[i]])
        generatedHeader += f" {rowNames[i]:^{max(maxRowNum-5,10)}} "
        spacingList.append(maxRowNum)
    print(generatedHeader)

    for i in range(0, len(multiArray)):
        finalPrintedCollumn = ""
        for j in range(0, len(multiArray[i])):
            finalPrintedCollumn += f" {multiArray[i][j]:^{max(spacingList[j]-5,10)}} "
        
        if i <= printTo:
            print(finalPrintedCollumn)

#Menu function for displaying user interactoin
def menu(individualArrays, multiArray):
    enter = input("\nWould you like to search the library? (Y/N): ").lower()
    while enter != "y" and enter != "n":
        print("\nPlease only enter 'y' or 'n")
        enter = input("\nWould you like to search the library? (Y/N): ").lower()

    options = ["Title", "Price", "Rating","Author","Year Published", "Genre"]
    
    if enter == "y":
        selectedOption = optionSelector(options)
        searchTerm = input("\nWhat do you want to search?: ")
        searchResult = searchSortComparison(searchTerm, multiArray, individualArrays[selectedOption])
        amount = input("\nHow many results do you want?: ")
        
        while not amount.isdigit():
            print("\nPlease only enter number: ")
            amount = input("\nHow many results do you want?: ")

        amount = min([100, abs(int(amount))])
        printMultiArray(options, individualArrays, searchResult, amount)

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

    selectedOption = int(selectedOption)-1
    return selectedOption

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
        fileValues.append([rec[1], float(rec[2]), float(rec[3]),rec[4],int(rec[5]),rec[6]])
        
        #Counts records
        recordTotal += 1

menu([titles, prices, ratings, authors, yearsPublished, genres], fileValues)