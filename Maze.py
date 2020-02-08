import csv
import datetime
from datetime import datetime
import time
from time import strptime
import sys
import os.path
import copy

maze = []
menu = ("Read and load maze from file", "View maze", "Play maze game", "Configure current maze")
configuration_menu = ["Create Wall", "Create Passageway", "Create Start Point", "Create End Point"]
run = True

#Display menu function
def display_menu(check):
    if check == True:
        print('\n=========\nMAIN MENU \n=========')
        for i, item in enumerate(menu,1):
            print([i],'',item)
        print()
        print('[0]  Exit Maze')
        print('')
        return "Displaying Menu"
    else:
        return "Invalid menu"

def check_option(option, end=''):
    if option == "1":
        if end=="break":
            return "Option 1 selected"
        maze.clear()
        file = input("Enter the name of the data file: ")
        check_filename(file)
        return "Option 1 selected"

    elif option == "2":
        print("Option 2")
        print("View Maze")
        print("========================================")
        trace = viewMaze(maze)
        print(trace)
    
    elif option == "3":
        play_maze(maze)
    
    elif option == "4":
        config_menu()

    else:
        print ("Invalid option")
        return "Invalid Option"

# Function to check filename
def check_filename(filename):
    try :
        f = open(filename)
        csv_reader = csv.reader(f,delimiter=',')
        line_count = 0
        for row in csv_reader:
            maze.append(row)
            line_count += 1
        print("Number of lines read: " + str(line_count))
        return "Filename correct"
    except IOError:
        print("Error, file not found")
        return "Filename incorrect"

####################################################################################

def viewMaze(maze):
    trace = ""
    if 1 not in maze or exist == False:
        for i in range(len(maze)): #prints maze_list line by line for user to read
            print(maze[i])
    else:
        trace = "Please load your maze first"
        
    return trace

###################################################################################

def play_maze(maze):
    print('Option [3] Play maze game')
    print('=================================')
    
    while True:
        try:
            for a in range(len(maze)):
                for b in range(len(maze[a])):
                    if maze[a][b]=='B':
                        b_row=a
                        b_col=b
            for c in range(len(maze)):
                for d in range(len(maze[c])):
                    if maze[c][d]=='A':
                        row = c
                        col = d
            for item in range(len(maze)):
                print(maze[item])
            print('Location of You(A) = (Row {}, Column {})'.format(row,col))
            print('Location of End (B) = (Row {}, Column {})'.format(b_row,b_col))
            movement=input("Press 'W' for UP, 'A' for LEFT, 'S' for DOWN, 'D' for RIGHT, 'M' for MAIN NENU': ")
            movement = movement.upper()
            if movement=='W':
                if maze[row-1][col]=='X':
                    print('Sorry, Wall Ahead. Please try another path')
                else:
                    maze[row][col]='O'
                    maze[row-1][col]='A'
                    print('UP successfully, press')
            elif movement=='S':
                if maze[row+1][col]=='X':
                    print('Sorry, Wall Ahead. Please try another path')
                else:
                    maze[row][col]='O'
                    maze[row+1][col]='A'
                    print('DOWN successfully, press')
            elif movement=='A':
                if maze[row][col-1]=='X':
                    print('Sorry, Wall Ahead. Please try another path')
                else:
                    maze[row][col]='O'
                    maze[row][col-1]='A'
                    print('LEFT successfully, press')
            elif movement=='D':
                if maze[row][col+1]=='X':
                    print('Sorry, Wall Ahead. Please try another path')
                else:
                    maze[row][col]='O'
                    maze[row][col+1]='A'
                    print('RIGHT successfully, press')
            elif movement =='M':
                print ('Return to Menu')
                break
                display_menu()
            else:   
                print('Invalid Movement, try again!')
        except 	IndexError:
            print ('Oops! Out of Zone')
            break
            display_menu()

#####################################################################################

def config_menu():

    print("Configuration Menu")
    print("="*16)

    options = 1
    for i in configuration_menu:
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
    elif config_options == 3:
        config_create_start()
    elif config_options == 4:
        config_create_end()

def config_create_wall(input_row,input_col):
    print("Enter the coordinate of the item you wish to change E.g. Row, Column")
    print("'B' to return to Configure Menu")
    input_row, input_col = input("'M' to return to Main Menu: ").split(",")

    if (input_row.isdigit() and 0 <= int(input_row) < 9 and 0 <= int(input_col) < 9):
        maze[(int(input_row)-1)][(int(input_col)-1)] = "X"

        file = open("maze.csv","w")
        for row in maze:
            for col in row:
                file.write("\n")
    elif input_row == "B":
        config_menu()
    elif input_row == "M":
        display_menu()
    else:
        print("Invalid input, please enter a valid input of either “B/M” or coordinate in the correct format")

def config_create_passageway():
    print("Enter the coordinate of the item you wish to change E.g. Row, Column")
    print("'B' to return to Configure Menu")
    input_row, input_col = input("'M' to return to Main Menu: ").split(",")

    if (input_row.isdigit() and 0 <= int(input_row) < 9 and 0 <= int(input_col) < 9):
        maze[(int(input_row)-1)][(int(input_col)-1)] = "O"

        file = open("maze.csv","w")
        for row in maze:
            for col in row:
                file.write("\n")
    elif input_row == "B":
        config_menu()
    elif input_row == "M":
        display_menu()
    else:
        print("Invalid input, please enter a valid input of either “B/M” or coordinate in the correct format")        

def config_create_start():
    print("Enter the coordinate of the item you wish to change E.g. Row, Column")
    print("'B' to return to Configure Menu")
    input_row, input_col = input("'M' to return to Main Menu: ").split(",")

    if (input_row.isdigit() and 0 <= int(input_row) < 9 and 0 <= int(input_col) < 9):
        maze[(int(input_row)-1)][(int(input_col)-1)] = "A"

        file = open("maze.csv","w")
        for row in maze:
            for col in row:
                file.write("\n")
    elif input_row == "B":
        config_menu()
    elif input_row == "M":
        display_menu()
    else:
        print("Invalid input, please enter a valid input of either “B/M” or coordinate in the correct format")

def config_create_end():
    print("Enter the coordinate of the item you wish to change E.g. Row, Column")
    print("'B' to return to Configure Menu")
    input_row, input_col = input("'M' to return to Main Menu: ").split(",")

    if (input_row.isdigit() and 0 <= int(input_row) < 9 and 0 <= int(input_col) < 9):
        maze[(int(input_row)-1)][(int(input_col)-1)] = "B"

        file = open("maze.csv","w")
        for row in maze:
            for col in row:
                file.write("\n")
    elif input_row == "B":
        config_menu()
    elif input_row == "M":
        display_menu()
    else:
        print("Invalid input, please enter a valid input of either “B/M” or coordinate in the correct format")



if __name__ == "__main__":
    while run != False:
        display_menu(True)
        run = check_option(input ("Enter your option: "))
