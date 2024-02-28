#Dylan Fisher, Idrees Abdurrazzak, Latoya Hall
#Generates seats 2d array
seats = []
for i in range(0, 7):
    seats.append(["A", "B", "C", "D"])

#function allows user to select row and seat for flight
def selectSeat(seats):
    #Prints array
    printSeats(seats)

    #loops and checks if user is getting seat placement
    selectSeatPlacement = "y"
    while selectSeatPlacement == "y":
        #Asks user for seat row, and makes sure that row is not greater then largest amount fo rows
        #Makes sure that value is number and within range
        seatRow = -1
        while seatRow not in range(0, len(seats)):
            try:
                seatRow = int(input("What row do you want to sit in?: "))-1
            except:
                print("ROW must be a Integer")

            if seatRow not in range(0, len(seats)):
                print(f"ROW must be greater than 0 and less than or equal to {len(seats)}")

        isInproperLetter = "y"
        while isInproperLetter == "y":
            #asks user for seat letter
            seatLetter = input("What seat do you want?: ")

            #converts seat letter to index
            letterDictionary = {"A": 0, "B":1, "C":2, "D":3}
            if seatLetter in letterDictionary.keys():
                isInproperLetter = 'n'
            else:
                print("Not a proper Seat")

        #gets seat user has slected
        selectedSeat = seats[seatRow][letterDictionary[seatLetter]]

        #checks if seat has been slected already
        if selectedSeat != "X":
            #sets seat at position to X
            seats[seatRow][letterDictionary[seatLetter]] = "X"
            printSeats(seats)
            # asks user if the want to select another seat
            another = input("\nWould you like to select another seat? (y/n): ")
            if another != "y":
                seatselectSeatPlacement = "n"
        else:
            print("Select another seat: ")
    return seats

#Itterates though seat array and prints 2d
def printSeats(seats):
    print("\nAirDrogon ~ Valyria Bount Flight #4815")
    #prints top boarder and heading
    print("-"*39)
    print("|\tRow #\t-  -\t\t-  -  |")

    #itterates though rows
    for i in range(0, len(seats)):
        #builds base starting string for row
        rowString = "|\t " + str(i+1) + "\t"
        #itterates though seat letters
        for seat in range(0, len(seats[i])):
            #changes spacing in rowString
            if seat % 2 == 1 and seat != 3:
                rowString += seats[i][seat] + "\t\t"
            else:
                rowString += seats[i][seat] + "  "
        rowString += "|"
        print(rowString)
    print("-"*39)

printSeats(selectSeat(seats))
