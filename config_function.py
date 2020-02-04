Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def maze_loaded():
    for line in dataInFile:
        print(line)

#######################

def maze_view(maze):
    outputString = ""
    if (maze != []):
        for i in maze:
            outputString += str(i) + "\n"
        else:
            outputString = "Please load a maze before configuring"

        return outputString

#######################

def maze_config():
    print ("="*41)
    print()
    maze_loaded()
    menu_option = None
    coordinate = None

    if dataInFile == []:
        print ("please load or create a maze before configuring")
        print()
    else:
        while menu_option != 5 and coordinate!= "M":
            print()
            print("Configuration Menu")
            print("="*16)
            configure_menu()
            print()
            menu_option = int(input("Enter Options: "))
            if menu_option <0 or menu_option > 5:
                print("Invalid input, please input a valid option from 0 to 4")
                print()
                maze_loaded()
                print()

            else:
                print()
                while True:
                    if menu_option == 1:
                        print()
                        
                        while True:
                            print("Enter the coordinate of the item you wish to change E.g Row,Column")
                            print("'B' to return to Configure menu.")
                            coordinate = input("'M' to return to Main Menu: ").upper()
                            
                            if maze_size(coordinate.split(",")) == True:
                            
                                break
                            maze_loaded()
                            
                            print("Please enter a valid coordinate within the maze")
                            print()
                             
                        if coordinate != "B" and coordinate != "M":
                            coordinate = coordinate.split(",")
                            y = int(coordinate[0])
                            x = int(coordinate[1])
                            if dataInFile[y-1][x-1] != "A" and dataInFile[y-1][x-1] != "B":
                                dataInFile[y-1][x-1] = "X"
                            else:
                                print("Please enter a valid input")
                        elif coordinate == "M":
                            break
                        elif coordinate == "B":
                            maze_loaded()
                            break

                    if menu_option == 2:
                        print()

                        while True: 
                            print("Enter the coordinate of the item you wish to change E.g Row,Column")
                            print("'B' to return to Configure menu.")
                            coordinate = input("'M' to return to Main Menu: ").upper()
                            
                            if maze_size(coordinate.split(",")) == True:
                            
                                break
                            maze_loaded()
                            print("Please enter a valid coordinate within the maze")
                            print()
                        if coordinate != "B" and coordinate != "M": 
                            coordinate = coordinate.split(",")
                            y = int(coordinate[0])
                            x = int(coordinate[1])
                            if dataInFile[y-1][x-1] != "A" and dataInFile[y-1][x-1] != "B":
                                dataInFile[y-1][x-1] = "O"
                            else:
                                print("Please Enter A Valid Input")
                        elif coordinate == "M":
                            break
                        elif coordinate == "B":
                            maze_loaded()
                            break

                    if menu_option == 3:
                        while True:
                            print("Enter the coordinate of the item you wish to change E.g Row,Column")
                            print("'B' to return to Configure menu.")
                            coordinate = input("'M' to return to Main Menu: ").upper()
                            
                            if maze_size(coordinate.split(",")) == True:
                            
                                break
                            maze_loaded()
                            print("Please enter a valid coordinate within the maze")
                            print()
                            
                        if coordinate != "B" and coordinate != "M":
                            coordinate = coordinate.split(",")
                            y = int(coordinate[0])
                            x = int(coordinate[1])
                            ya, xa = findaxisa()
                            if ya != -1 and xa != -1:
                                if dataInFile[y-1][x-1] != "A" and dataInFile[y-1][x-1] != "B":
                                    dataInFile[xa][ya] = "X"
                                    dataInFile[y-1][x-1] = "A"
                                else:
                                    break
                            else:
                                dataInFile[y-1][x-1] = "A"
                                
                        elif coordinate == "M":
                            break
                        elif coordinate == "B":
                            maze_loaded()
                            break



                    if menu_option == 4:
                        while True:
                            print("Enter the coordinate of the item you wish to change E.g Row,Column")
                            print("'B' to return to Configure menu.")
                            coordinate = input("'M' to return to Main Menu: ").upper()
                            
                            if maze_size(coordinate.split(",")) == True:
                            
                                break
                            correct_maze()
                            print("Please enter a valid coordinate within the maze")
                            print()
                            
                        if coordinate != "B" and coordinate != "M":
                            coordinate = coordinate.split(",")
                            y = int(coordinate[0])
                            x = int(coordinate[1])
                            yb, xb = findaxisb()
                            if yb != -1 and xb != -1:
                                if dataInFile[y-1][x-1] != "A" and dataInFile[y-1][x-1] != "B":
                                    dataInFile[xb][yb] = "X"
                                    dataInFile[y-1][x-1] = "B"
                                else:
                                    break
                            else:
                                dataInFile[y-1][x-1] = "B"
                                
                        elif coordinate == "M":
                            break
                        elif coordinate == "B":
                            maze_loaded()
                            break

                    if menu_option == 5:
                        break

                    maze_loaded()
