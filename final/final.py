import os
import csv  
import tkinter as tk
from tkinter import filedialog
import shutil
import pathlib

#Dylan Fisher: Final
#Prompt:
    # This program that uses the TKinter library to allow a user to upload any csv or txt file and it will represent the data within the file though the console. 
    #The user will be able to make changes to the data set by selecting a column and a row, which will then be updated in the file.

#Varriable Dictionary



def getCopyUsersFile(dst):
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx"), ("Text files", "*.txt"), ("CSV files", "*.csv")])
    size = os.path.getsize(dst)
    
    if size != 0:
        ask = input("Write over file?").lower()
        
        if ask == "y":
            shutil.copyfile(file_path, dst)

    else:
        shutil.copyfile(file_path, dst)
        

    return file_path, dst

def readFile(path):
    #2D array containing file values
    fileValues = []

    with open(path) as csvfile:
        #must indent when connected to and reading the file

        #defines fileContent
        file = csv.reader(csvfile)
        #itterates though records
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
    if addHeader == "y":
        anotherHeading = "y"
        header = ""
        while anotherHeading == "y":
            heading = input("What heading do you want to add")
            header += heading
            anotherHeadting = input("Add another heading? (y/n)")
        modifyFile(path, header)
getCopyUsersFile("final/destination")
modifyFile("final/destination", "Test")