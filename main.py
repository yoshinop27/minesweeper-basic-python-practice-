import random

## Global vars
board = [[0 for i in range(5)] for j in range(5)]
minesRaw = []
mines = []
dimension = len(board)
dirs = [
    [-1, 0],
    [1, 0],
    [0, 1],
    [0, -1],
    [-1, 1],
    [-1, -1],
    [1, 1],
    [1, -1],
]

## state variables
completed = []

# creating mines
minesRaw = random.sample(range(25), 5)
for mine in minesRaw:
    row = mine//5
    col = mine % 5
    mines.append([row, col])
print(mines)

# initialize grid and print
def printGrid ():
    print('  ', end='')  # Space for row label alignment
    for k in range(dimension):
        print(' {} '.format(k), end='')
    print()
    for i in range(dimension):
        print('{} '.format(i), end='')  # Add space after row number
        for j in range(dimension):
            if board[i][j] == 0:
                print('[ ]', end='')
            else:
                print('[x]', end='')
        print()  # Move to next line after each row

printGrid()

#take user input 
while len(completed) < (dimension**2-5):
    guess = input('Enter the row and column of your guess (i.e 34 = row 3 column 4): ')
    row = int(guess[0])
    col = int(guess[1])
    if row < dimension and col < dimension and row >= 0 and col >= 0 and [row, col] not in completed:
        if [row, col] in mines:
            print("Game Over")
            break
        else:
            count = 0
            for dir in dirs:
                check = [row + dir[0], col + dir[1]]
                if check in mines:
                    count+=1
            print("{} mines adjacent".format(count))
            print(mines)
            print()
            board[row][col] = 1
            completed.append([row, col])
            printGrid()
    else:
        print("Error try again")
