def check_col(sudoku):
    '''
    Function to check columns
    '''
    for every_row in range(len(sudoku)):
        col_set = set()
        for every_col in range(len(sudoku[0])):
            col_set.add(sudoku[every_col][every_row])
        if len(col_set) != len(sudoku):
            return False
    return True
def check_row(sudoku):
    '''
    function to check rows
    '''
    for every_row in sudoku:
        if len(set(every_row)) != len(sudoku):
            return False
    return True
def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    for every_row in sudoku:
        for i in every_row:
            if i not in "1234567890":
                return False
    if check_row(sudoku) is False:
        return False
    if check_col(sudoku) is False:
        return False
    # if check_grid(sudoku) is False:
    #     return False    
    return True
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i_num in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
        i_num += 1
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()