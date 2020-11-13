###############################################################################################################
#                                                                                                             #
#                                      N_QUEENS BACK TRACKING ALGORITHM                                       #          
#                                                                                                             #
###############################################################################################################

###############################################################################################################
#These functions deal with board creation and printing them in a proper format
def generateBoard(N):
    #generate board based on User Input N in Main()
    Board = [[0 for i in range(0,N)] for j in range(0,N)]
    return Board

def printBoard(arr):
    #Loop through each row to print an organized board
    for row in arr:
        print(row)

###############################################################################################################
#This function determines whether we can put a Queen in a certain orientation on the board
def isValid(row,col,Current,N):
    #check whether current state of game has queen in row/column
    for i in range(0,N):
        #checks column/row and sees whether a queen exists already
        if Current[row][i] == "Q" or Current[i][col] == "Q":
            return False
    
    # Check upper diagonal on right side 
    i = row-1
    j = col + 1
    
    #Do while row is greater than 0 and column is less than N
    while i >= 0 and j < N:
        if Current[i][j] == "Q":
            return False
        i -= 1
        j += 1
       
    # Check upper diagonal on left side
    #Do while row is greater than 0 and column is greater than N
    i = row-1
    j = col - 1
    while i >= 0 and j >= 0:
        if Current[i][j] == "Q":
            return False
        i -= 1
        j -= 1
    #If we pass the diagonal/row/column tests, we can then determine this is a valid move
    return True

###############################################################################################################
#This is our main recursive function that will determine optimal outcome
def NQueens(row,Current,N):
    #this tells us when to stop
    if row == N:
        print("\n")
        return printBoard(Current) 
    
    for choice in range(0,N):
        if isValid(row,choice,Current,N):
            #Place Queen in appropriate spot
            Current[row][choice] = "Q"
            
            #Go to next row
            NQueens(row+1,Current,N)
        Current[row][choice] = 0
    return "All Solutions Found"
        

                
def main():
    #ask number from user
    print("What sized board would you like?"
    " Please input a number higher that 3: ")

    #user input used to determine size of board
    N = int(input())

    #generate Board that will be used
    Board = generateBoard(N)

    #this is the current status of the board
    printBoard(Board)
    print("\n")

    #Test
    print(NQueens(0,Board,N))
    

if __name__ == "__main__":
    main()
