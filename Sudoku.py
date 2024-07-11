# numpy helps us get the sudoku in a grid.
import numpy as np

#Creating a grid for the sudoku puzzle, blank space represented by zero
sudoku_puzzle = [[8,4,0,2,0,0,7,6,9], 
                 [0,0,2,6,3,4,0,1,8],
                 [0,5,6,7,0,8,3,2,4],
                 [0,0,0,9,8,0,1,0,0],
                 [0,0,9,0,0,0,2,7,3],
                 [6,0,4,0,0,7,8,0,0],
                 [0,3,8,4,0,2,6,0,0],
                 [2,0,0,8,6,9,0,3,0],
                 [4,6,0,0,7,0,9,8,0]]

#creating a possiility function to check if a number is in the 3 by 3 grid or horizontally or vertically
def possibility(row, column, num):
    global sudoku_puzzle
    #Is the Num appearing in the given Row?
    for i in range(0,9):
        if sudoku_puzzle[row][i] == num:
            return False
        
    #Is the Num appearing in the given Column?
    for i in range(0,9):
        if sudoku_puzzle[i][column] == num:
            return False

# checking if the number we are entering its present in the 3 by 3 grid or the square.        
    x0 = (column // 3) * 3
    y0 = (row //3 ) * 3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku_puzzle[y0+1][x0+1] == num:
                return False
            
    return True

#creating a function that would be the solution .

def solution():
    global sudoku_puzzle
    for row in range(0,9):
        for column in range(0,9):
            if sudoku_puzzle[row][column] == 0:
                for num in range(1,10):
                    if possibility(row, column, num):
                        sudoku_puzzle[row][column] = num
                        solution()
                        sudoku_puzzle[row][column] = 0
                return
            
    print(np.matrix(sudoku_puzzle))
    input('More possible solutions')

solution()


            
