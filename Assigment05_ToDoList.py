# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# SAnderson,11.14.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
strFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
strTask = ""  # Capture task value
strPriority = ""  # Capture priority value


# -- Processing -- #
# Load any data from a text file called ToDoList.txt
# into a python list of dictionaries rows

objFile = open(strFile, "r")
for row in objFile:
    # removes the comma between elements in the text file
    lstRow = row.split(",")
    # use strip function to remove the \n from printing out
    dicRow = {"Task": lstRow[0].strip(), "Priority": lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()
print("Successfully loaded data")

# -- Input/Output -- #
# Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Current Data: \n")
        for row in lstTable:
            print(row)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Enter a task: ")
        strPriority = input("Enter a priority (high, medium, low): ")
        lstTable.append({"Task": strTask.strip().lower(), "Priority": strPriority.strip().lower()})
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print(lstTable)
        strRemove = input("Enter a task to remove: ")
        strRemove.strip()
        for row in lstTable.copy():
            if row.get("Task") == strRemove.lower():
                print("row removed")
                lstTable.remove(row)
                break
        # Placing the else statement outside the For loop prevents
        # the program from printing multiple lines of "row not found"
        else:
            print("row not found")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # Open a new text file to save the data entered by the user
        objFile = open(strFile, "w")
        print("Data saved")
        for row in lstTable:
            objFile.write(row["Task"] + ',' + row["Priority"] + '\n')
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Closing Program. Good Bye")
        break  # and Exit the program
