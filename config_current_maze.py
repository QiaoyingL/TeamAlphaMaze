
import csv

datafile = [maze.csv]
config_menu_list = ["Create Wall", "Create Passageway", "Create Start Point", "Create End Point"]

def config_menu():

    print("Configuration Menu")
    print("="*16)

    options = 1
    for i in config_menu_list:
        print("[{0}] {1}".format(options, i))
        options += 1
    
    print()
    print("[0] Exit to Main Menu")
    print()

    config_options = input("Enter your options: ")
    if( 0 <= int(config_options) < 5):
        config_options = int(config_options)
        options()
    else:
        print("Invalid input, please input a valid option from 0 to 4")
    return config_options

def options():
    if config_options == 1:
        config_create_wall()
    elif config_options == 2:
        config_create_passageway()
    elif config_opitons == 3:
        config_create_start()
    elif config_options == 4:
        config_create_end()

def config_create_wall(input_row,input_col):
    print("Enter the coordinate of the item you wish to change E.g. Row, Column")
    print("'B' to return to Configure Menu")
    input_row, input_col = input("'M' to return to Main Menu: ").split(",")

    if (input_row.isdigit() and 0 <= int(input_row) < 9 and 0 <= int(input_col) < 9):
        datafile[(int(input_row)-1)][(int(input_col)-1)] = "X"

        file = open("maze.csv","w")
        for row in datafile:
            for col in row:
                file.write("\n")
    elif input_row == "B":
        config_menu()
    elif input_row == "M":
        MainMenu()
    else:
        print("Invalid input, please enter a valid input of either “B/M” or coordinate in the correct format")

def config_create_passageway():
    print("Enter the coordinate of the item you wish to change E.g. Row, Column")
    print("'B' to return to Configure Menu")
    input_row, input_col = input("'M' to return to Main Menu: ").split(",")

    if (input_row.isdigit() and 0 <= int(input_row) < 9 and 0 <= int(input_col) < 9):
        datafile[(int(input_row)-1)][(int(input_col)-1)] = "O"

        file = open("maze.csv","w")
        for row in datafile:
            for col in row:
                file.write("\n")
    elif input_row == "B":
        config_menu()
    elif input_row == "M":
        MainMenu()
    else:
        print("Invalid input, please enter a valid input of either “B/M” or coordinate in the correct format")        

def config_create_start():
    print("Enter the coordinate of the item you wish to change E.g. Row, Column")
    print("'B' to return to Configure Menu")
    input_row, input_col = input("'M' to return to Main Menu: ").split(",")

    if (input_row.isdigit() and 0 <= int(input_row) < 9 and 0 <= int(input_col) < 9):
        datafile[(int(input_row)-1)][(int(input_col)-1)] = "A"

        file = open("maze.csv","w")
        for row in datafile:
            for col in row:
                file.write("\n")
    elif input_row == "B":
        config_menu()
    elif input_row == "M":
        MainMenu()
    else:
        print("Invalid input, please enter a valid input of either “B/M” or coordinate in the correct format")

def config_create_end():
    print("Enter the coordinate of the item you wish to change E.g. Row, Column")
    print("'B' to return to Configure Menu")
    input_row, input_col = input("'M' to return to Main Menu: ").split(",")

    if (input_row.isdigit() and 0 <= int(input_row) < 9 and 0 <= int(input_col) < 9):
        datafile[(int(input_row)-1)][(int(input_col)-1)] = "B"

        file = open("maze.csv","w")
        for row in datafile:
            for col in row:
                file.write("\n")
    elif input_row == "B":
        config_menu()
    elif input_row == "M":
        MainMenu()
    else:
        print("Invalid input, please enter a valid input of either “B/M” or coordinate in the correct format")

        
