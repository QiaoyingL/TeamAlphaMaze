import csv
import datetime
from datetime import datetime
import time
from time import strptime
import sys
import os.path
import copy

maze = []
start = []
end = []

#Displays the Main Menu
def MainMenu():
    print("MAIN MENU")
    print("=========")
    print("[1] Read and load maze from file")
    print("[2] View Maze")
    print("[3] Play maze game")
    print("[4] Configure current maze")
    print()
    print("[0] Exit Maze")
    print()
    option = input("Enter your option: ")
    print()

    if option == "1":
        print("Read and load maze from file")
        maze = Read()
        start, end = Store(maze)
        
    elif option == "2":
        print("View Maze")
        trace = viewMaze(maze)
        print(trace)
              
    elif option == "3":
        print("Play maze game")
        
    elif option == "4":
        print("Configure current maze")
        
    elif option == "0":
        print("Exiting Maze...")
        exit
        
    else:
        print("Invalid Option. Try Again")
        MainMenu()

#######################################################################################

#Reads the input of the file
def Read():
    file_name = input('Enter the name of the data file: ')
    maze = []
    num_lines = 0
    
    try:
        with open(file_name, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                maze.append(row)
            num_lines = csv_reader.line_num
        print('Number of lines read: {}'.format(num_lines))
        print()
        MainMenu()
    except FileNotFoundError:
        print('Invalid file type!')
        print()
        MainMenu()
    return maze

#Stores the input of the file in memory
def Store(maze):
    start_coordinate = []
    end_coordinate = []
    
    for row_index, row in enumerate(maze):
        for column_index, column in enumerate(row):
            if (column == 'A'):
                start_coordinate.append(column_index + 1)
                start_coordinate.append(row_index + 1)
                break
            elif (column == 'B'):
                end_coordinate.append(column_index + 1)
                end_coordinate.append(row_index + 1)
                break
    if (len(start_coordinate) == 0 or len(end_coordinate) == 0):
        print('Invalid maze!')
        return -1, -1

    return start_coordinate, end_coordinate

#######################################################################################

def viewMaze(game):
    trace = ""
    if 1 not in maze or exist == False:
        for i in range(len(maze)): #prints maze_list line by line for user to read
            print(maze[i])
    else:
        trace = "Please load your maze first"
        
    return trace


if __name__ == '__main__':
    MainMenu()

#######################################################################################
