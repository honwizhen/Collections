myArray=[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def checkEmptySquare(myArray):
    for i in range(9):
        for j in range(9):
            if myArray[i][j] == 0:
                return i,j
    return None

def print_board(myArray):
    for i in range(len(myArray)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(len(myArray)):
            if j % 3 ==0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(myArray[i][j])
            else:
                print(str(myArray[i][j]) + " ", end="")

def valid(myArray,num,pos):
    # Check row
    for i in range(len(myArray[0])):
        if myArray[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(myArray[0])):
        if myArray[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3,box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if myArray[i][j] == num and (i,j) != pos:
                return False
    return True 

def solve(myArray):
    find = checkEmptySquare(myArray)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(myArray, i, (row, col)):
            myArray[row][col] = i
            
            if solve(myArray):
                return True

            myArray[row][col] = 0
    return False

print(print_board(myArray))
solve(myArray)
print("_____________________________________")
print(print_board(myArray))