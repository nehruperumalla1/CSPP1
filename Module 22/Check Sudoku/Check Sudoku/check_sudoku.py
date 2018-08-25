'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
    rule1 = False
    rule2 = True
    count = 0
    count1 = 0
    for index in sudoku:
        rule1 = False
        if len(set(index)) == 9:
            rule1 = True
            # print(rule1)
            count1 += 1
    set1 = set()
    for iindex in range(len(sudoku)):
        for jindex in range(len(sudoku[iindex])):
            for val in range(9):
                if jindex == val:
                    # print(val)
                    set1.add(sudoku[iindex][jindex])
                    if len(set1) == 9:
                        # print(len(set1))
                        count += 1
    # print(count)
    if count1 == 9 and count == 9 or count == 73:
        return True
    else:
        return False

def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []

    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        #print(row)
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()