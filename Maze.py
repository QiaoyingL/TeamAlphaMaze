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
        #Read()
        trace = viewMaze(fileoutput)
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

#######################################################################################

def viewMaze(game):
    trace = ""
    #Read()
    if (game != []):
        for i in range(len(fileoutput)): #prints maze_list line by line for user to read
            print(fileoutput[i])
    else:
        trace = "Please load your maze first"
        
    return trace


if __name__ == '__main__':
    MainMenu()


    






