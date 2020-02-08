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
        trace = viewMaze(maze)
        print(trace)
    
    elif option == "3":
        print("Option 3")
    
    elif option == "4":
        print("Option 4")

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

def viewMaze(maze):
    trace = ""
    if 1 not in maze or exist == False:
        for i in range(len(maze)): #prints maze_list line by line for user to read
            print(maze[i])
    else:
        trace = "Please load your maze first"
        
    return trace

if __name__ == "__main__":
    while run != False:
        display_menu(True)
        run = check_option(input ("Enter your option: "))
