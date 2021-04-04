#Sudoku 9x9
#In this approach we will use recursion and backtracking
#We will check each cell which are empty or 0 by putting valur from 1 to 9
#Checking column, row and submatrix to see if that number exist or not
#If exist then put the number and check for other empty cell, else remove the number from previous location
#and try the next number 
#When the column and row reaches the last index, simply print the sudoku


import math
#This function takes 4 argument i.e i = current row, j = current column, grid = sudoku and n = length of row and column
def solveSudoku(i,j,grid,n):
    ni = 0
    nj = 0
    #Base Case
    #If the row and column reached the last index, print the current grid
    if i == n:
        printGrid(grid,n)
        return
    #If current row is lower than the last index and current row reached the last index
    if j == n-1:
        #Shift the row and change the column back to the first column
        ni = i+1
        nj = 0
    #Else the column is less than the last column and row also smaller then go to next column in the same row
    else:
        ni = i
        nj = j+1
    #If there is already a number exist then move to the next number
    if grid[i][j] != 0:
        solveSudoku(ni,nj,grid,n)
    #Else check the index with value 0-9
    else:
        #Iterate through possible solution from 0 to 9
        for k in range(0,10,1):
            #Check if the number already exist in that row, column or submatrix
            #Call function safe to check, it passes 5 argument i.e the current row, current column, k = possible number
            #grid and size of each row and column
            if safe(i,j,k,grid,n) == True:
                #If the possible solution is safe, then put it in that location
                grid[i][j] = k
                #Solve the next index by recursively calling the function solveSudoku
                solveSudoku(ni,nj,grid,n)
                #If the possible solution does not solve the sudoku then check for next possible solution and put 0 back
                grid[i][j] = 0

#This Function takes 5 argument i.e i = current row, j = current column, k = possible solution, grid = sudoku and n = size
def safe(i,j,k,grid,n):
    #Iterate through current row to check if the number exist or not
    for column in range(n):
        if grid[i][column] == k:
            #If k is already present then return False
            return False
    #Iterate thorugh current colummn to check if the number exist or not
    for row in range(n):
        if grid[row][j] == k:
            #If k is already present in return False
            return False
    #Location of the submatrix i.e starting index of the submatrix from location of current row and column
    row = math.floor(i/3)*3
    column = math.floor(j/3)*3
    #Iterate through each index of the submatrix to checck if the number exist
    for subrow in range(0,3):
        for subcol in range(0,3):
            if grid[subrow+row][subcol+column] == k:
                #K is already present, return False
                return False
    #If non of the iteration return False then the number is safe to put in that location
    return True

#This function takes 2 argument i.e grid = sudoku, n = size
def printGrid(grid,n):
    for i in range(n):
        for j in range(n):
            print(grid[i][j],end = " ")
        print("")
    return 
#For input
if __name__ == "__main__":
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    n = len(grid)
    print("Unsolved Sudoku")
    printGrid(grid,n)
    print("Solved Sudoku")
    solveSudoku(0,0,grid,n)
else:
    print("Error")