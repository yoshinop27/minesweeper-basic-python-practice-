import random

## Global vars
board = [[' ' for i in range(5)] for j in range(5)]
minesRaw = []
mines = []
dimension = len(board)

## state variables
state = True
completed = []


# initialize grid and mine locations
def printGrid ():
    print('  ', end='')  # Space for row label alignment
    for k in range(dimension):
        print(' {} '.format(k), end='')
    print()
    for i in range(dimension):
        print('{} '.format(i), end='')  # Add space after row number
        for j in range(dimension):
            print('[ ]', end='')
        print()  # Move to next line after each row

    # identifying mines
    minesRaw = random.sample(range(25), 5)
    for mine in minesRaw:
        row = mine//5
        col = mine % 5
        mines.append([row, col])
    print(mines)

printGrid()

#take user input 
while state and len(completed) != dimension**2:
    guess = input('Enter the row and column of your guess (i.e 34 = row 3 column 4): ')
    row = int(guess[0])
    col = int(guess[1])
    if row < dimension and col < dimension and row >= 0 and col >= 0:
        if [row, col] in mines:
            print("Game Over")
            break
        else:

    else:
        print("Error try again")
