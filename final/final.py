import os
import csv
import tkinter as tk
from tkinter import filedialog
import shutil

#Dylan Fisher: Final
#Prompt:
    # This program that uses the TKinter library to allow a user to upload any csv or txt file and it will represent the data within the file though the console.
    #The user will be able to make changes to the data set by selecting a column and a row, which will then be updated in the file.


# Copies a selected user file to a specified destination
def getCopyUsersFile(dst):
    size = os.path.getsize(dst)
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("Text files", "*.txt"), ("CSV files", "*.csv")])

    if size != 0 and len(file_path) != 0:
        ask = input("Write over file?: ").lower()

        if ask == "y":
            shutil.copyfile(file_path, dst)
    elif len(file_path) != 0:
        shutil.copyfile(file_path, dst)

# Reads a CSV file and returns its contents as a list of lists
def readFile(path):
    fileValues = []

    with open(path) as csvfile:
        file = csv.reader(csvfile)
        for rec in file:
            values = []
            for val in rec:
                values.append(val)
            fileValues.append(values)

    return fileValues

# Modifies a file by adding a new line at the beginning
def modifyFile(path, input):
    with open(path, "r+") as file:
        oldFile = file.read()  # read everything in the file
        file.seek(0)           # rewind
        file.write(input + "\n" + oldFile)  # write the new line before

# Removes a specified line from a file
def removeLine(path, lineNum):
    with open(path, "r+") as file:
        lines = file.readlines()
        file.seek(0)
        file.truncate()
        file.writelines(lines[0:lineNum-1] + lines[lineNum:])

# Adds a header to a CSV file
def addHeader(path):
    addHeader = input("Do you want to add a header to the file? (y/n): ").lower()
    headerAdded = "f"
    if addHeader == "y":
        anotherHeading = "y"
        header = ""
        while anotherHeading == "y":
            heading = input("What heading do you want to add?: ")
            header += heading + ","
            headerAdded = "f"
            anotherHeading = input("Add another heading? (y/n): ").lower()

        header = buildLine(path, header)
        modifyFile(path, header)
    return headerAdded

# Builds a line with commas to match the number of columns in a CSV file
def buildLine(path, string):
    if ',' not in string:
        string += ","

    with open(path) as csvfile:
        file = list(csv.reader(csvfile))
        rowLength = 0
        for row in file:
            if len(row) > rowLength:
                rowLength = len(row)

        while len(string.split(",")) < rowLength:
            string += ","
    return string

# Gets the column widths of a CSV file for formatting
def getSpacing(path):
    with open(path) as csvfile:
        file = list(csv.reader(csvfile))
        num_columns = len(file[0])
        column_widths = [0] * num_columns

        for row in file:
            for i, value in enumerate(row):
                column_widths[i] = max(column_widths[i], len(str(value)))

        return column_widths

# Converts a CSV file to a formatted string
def fileAsString(path):
    maxLengths = getSpacing(path)
    completeString = "\n"

    with open(path) as csvfile:
        file = csv.reader(csvfile)
        for row in file:
            formatted_row = ""
            for value, width in zip(row, maxLengths):
                formatted_row += f"{value:^{width+5}} "
            completeString += formatted_row + "\n"

    return completeString

# Adds a new line to a specified position in a CSV file
def addLine(path, lineNum, string):
    with open(path, "r+") as file:
        lines = file.readlines()
        lines.insert(lineNum-1, string + '\n')
        file.seek(0)
        file.writelines(lines)

#Finds every row with search value and returns 2d array of rows
def searchValue(path, search_value):
    matching_rows = []
    search_value = str(search_value)
    with open(path, 'r') as file:
        file_reader = csv.reader(file)
        for row in file_reader:
            for val in row:
                if search_value.lower() in val.lower():
                    matching_rows.append(row)
    return matching_rows

#Sorts array by a column
def bubbleSort2D(array, sort_column):
    rows = len(array)

    for i in range(rows - 1):
        for j in range(0, rows - i - 1):
            # Compare the values in the specified column
            if array[j][sort_column] > array[j + 1][sort_column]:
                # Swap rows if the values are out of order
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

#Takes 2d array and gets spacing based on length
def getSortedSpacing(sorted_array):
    num_columns = len(sorted_array[0])
    column_widths = [0] * num_columns

    for row in sorted_array:
        for i, value in enumerate(row):
            column_widths[i] = max(column_widths[i], len(str(value)))

    return column_widths

#Uses spacing to return string of 2d array
def getArrayAsString(array):
    maxLengths = getSortedSpacing(array)
    completeString = "\n"

    for row in array:
        formatted_row = ""
        for value, width in zip(row, maxLengths):
            formatted_row += f"{value:^{width+5}} "
        completeString += formatted_row + "\n"

    return completeString

# Main menu function that orchestrates file operations
# Has user add or remove lines in file
def menu():
    path = "final/destination"
    getCopyUsersFile(path)
    addHeader(path)
    print(fileAsString(path))

    editFile = input("Do you want to modify file lines? (y,n): ").lower()

    while editFile == 'y':
        remove = input("Do you want to remove a line? (y,n): ").lower()

        if remove == 'y':
            lineNumber = int(input("What line do you want to remove?: "))
            removeLine(path, lineNumber)
            print(fileAsString(path))

        add = input("Do you want to add a line? (y,n): ").lower()

        if add == 'y':
            lineNumber = int(input("What line do you want to add too?: "))

            atOnce = input("Do you want to add values all at once? (y,n): ")
            if atOnce == 'y':
                print("Type line below: ")
                stringValue = buildLine(path, input(""))
                addLine(path, lineNumber, stringValue)
            else:
                anotherValue = "y"
                stringValues = ""
                while anotherValue == "y":
                    string = input("What value do you want to add?: ")
                    stringValues += string + ","
                    anotherValue = input("Add another value? (y/n): ").lower()

                stringValues = buildLine(path, stringValues)
                addLine(path, lineNumber, stringValues)

            print(fileAsString(path))

        editFile = input("Do you want to modify more file lines? (y,n): ").lower()

    searchAndSort = input("Do you want to search or sort the file? (y,n): ").lower()

    while searchAndSort == "y":

        search = input("Do you want to search the file for a value? (y,n): ").lower()
        while search == "y":
            searchTerm = input("What value do you want to search for?")
            results = searchValue(path, searchTerm)
            print(getArrayAsString(results))

            search = input("Do you want to search the file for a value? (y,n): ").lower()

        sort = input("Do you want to get the file sorted? (y, n): ").lower()
        if sort == "y":
            columnNum = int(input("What column number do you want to sort by?: "))
            print(getArrayAsString(bubbleSort2D(readFile(path), columnNum)))

        searchAndSort = input("Do you want to search or sort the file? (y,n): ").lower()
menu()
