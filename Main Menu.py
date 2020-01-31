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
    
    
MainMenu()

