import os
import csv
import tkinter as tk
from tkinter import filedialog
import shutil

#Dylan Fisher: Final
#Prompt:
    # This program that uses the TKinter library to allow a user to upload any csv or txt file and it will represent the data within the file though the console.
    #The user will be able to make changes to the data set by selecting a column and a row, which will then be updated in the file.

#Varriable Dictionary

def getCopyUsersFile(dst):
    size = os.path.getsize(dst)
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("Text files", "*.txt"), ("CSV files", "*.csv")])
    if size != 0 and len(file_path) != 0:
        ask = input("Write over file?: ").lower()

        if ask == "y":
            shutil.copyfile(file_path, dst)

    elif len(file_path) != 0:
            shutil.copyfile(file_path, dst)


    return file_path, dst

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

def modifyFile(path, input):
    with open(path, "r+") as file:
        oldFile = file.read() # read everything in the file
        file.seek(0) # rewind
        file.write(input + "\n" + oldFile) # write the new line before


def addHeader(path):
    addHeader = input("Do you want to add a header to the file? (y/n): ").lower()
    headerAdded = "f"
    if addHeader == "y":
        anotherHeading = "y"
        header = ""
        while anotherHeading == "y":
            heading = input("What heading do you want to add")
            header += heading
            headerAdded = "f"
            anotherHeading = input("Add another heading? (y/n): ").lower()
        modifyFile(path, header)
    return headerAdded

def getSpacing(path):
    rowMaxLengths = []
    with open(path) as csvfile:
        file = csv.reader(csvfile)
        for rec in file:
            maxLength = 0
            for r in rec:
                if len(r) > maxLength:
                    maxLength = len(r)
            if maxLength != 0:
                rowMaxLengths.append(maxLength)
    return rowMaxLengths

def fileAsString(path):
    maxLengths = getSpacing(path)
    compleateString = ""

    with open(path) as csvfile:
        file = csv.reader(csvfile)
        i = 0
        for rec in csvfile:
            recStringBuild = ""
            for r in rec:
                recStringBuild += f"{r:^{abs(maxLengths[i] - len(r))}}"
            i += 1
            compleateString += recStringBuild + "\n"

    return compleateString


getCopyUsersFile("final/destination")

addHeader("final/destination")

print(fileAsString("final/destination"))
