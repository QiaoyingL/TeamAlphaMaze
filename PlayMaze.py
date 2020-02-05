maze=[
    ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'O', 'X', 'O', 'A', 'X'],
    ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'X'],
    ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'O', 'X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X'],
    ['X', 'O', 'X', 'O', 'O', 'O', 'X', 'X'],
    ['X', 'B', 'X', 'X', 'X', 'X', 'X', 'X']
    ]

def mainmenu():
    print('MAIN MENU')
    print('=========')
    print('[1] Read and load maze from file')
    print('[2] View maze')
    print('[3] Play maze game')
    print('[4] Configure current maze')
    print()
    print('[0] Exit Maze')

#Option 3
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
                    print('Invalid Movement,try again!')
                else:
                    maze[row][col]='O'
                    maze[row-1][col]='A'
                    print('UP successfully, press')
            elif movement=='S':
                if maze[row+1][col]=='X':
                    print('Invalid Movement,try again!')
                else:
                    maze[row][col]='O'
                    maze[row+1][col]='A'
                    print('DOWN successfully, press')
            elif movement=='A':
                if maze[row][col-1]=='X':
                    print('Invalid Movement,try again!')
                else:
                    maze[row][col]='O'
                    maze[row][col-1]='A'
                    print('LEFT successfully, press')
            elif movement=='D':
                if maze[row][col+1]=='X':
                    print('Invalid Movement,try again!')
                else:
                    maze[row][col]='O'
                    maze[row][col+1]='A'
                    print('RIGHT successfully, press')
            else:   
                print('Invalid Movement, try again!')
        except 	IndexError:
            print ('Oops! Out of Zone')
            break
            mainmenu()
  
        
  
    
while True:
    mainmenu()
    print()
    option=input('Enter your option: ')
    if option =='3':
        play_maze(maze)
    else:
        print('Invalid option, try again')
