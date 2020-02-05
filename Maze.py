import csv
import datetime
from datetime import datetime
import time
from time import strptime
import sys
import os.path
import copy


fileoutput = []


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
        Read()
    elif option == "2":
        print("View Maze")
        viewMaze()
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
    
def Read():
    datafile = input("Enter the name of the data file: ")
    try:
        
        with open(datafile, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            row_count = sum(1 for row in csv_file)
            print("Reading", datafile ,"...")
            time.sleep(2)
            print('Number of lines read: ', row_count)
            fileoutput.append(datafile)
            (print)
            MainMenu()
    except FileNotFoundError:
        print(datafile, "does not exist. Try again")
        (print)
        Read()

MainMenu()

def viewMaze():
    if 1 not in option_list or exist == False: #parameters set so that option 2 cannot run if maze is not loaded or if file does not exist to prevent the code from breaking
        print('Please load maze first.')
        MainMenu()
    continue
else:
    print()
    print('Option [2] View Maze')
    print('=========================================')
    print()
    for i in range(len(maze_list)): #prints maze_list line by line for user to read
        print(maze_list[i])
 #   with open('maze1.csv','rt')as f:
  #      data = csv.reader(f)
   #     for row in data:
    #        print(row)

MainMenu()






