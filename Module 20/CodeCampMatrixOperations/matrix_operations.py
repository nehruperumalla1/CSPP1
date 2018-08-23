'''Matrix Multiplication and Addition'''
import copy
def mult_matrix(matrix1, matrix2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(matrix1) != len(matrix2[0]):
        print("Error: Matrix shapes invalid for mult")
        return None
    matmul = []
    matlen1 = len(matrix1)
    for index in range(matlen1):
        mat = []
        for jindex in range(len(matrix2[0])):
            sum1 = 0
            for kindex in range(len(matrix2)):
                sum1 += matrix1[index][kindex] * matrix2[kindex][jindex]
            mat.append(sum1)
        matmul.append(mat)
    return matmul
def add_matrix(matrix1, matrix2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(matrix1) != len(matrix2):
        print("Error: Matrix shapes invalid for addition")
        return None
    matsum = copy.deepcopy(matrix1)
    for index in range(len(matrix1)):
        for jindex in range(len(matrix2[0])):
            matsum[index][jindex] += matrix2[index][jindex]
    return matsum

def read_matrix(matlen):
    '''
        read the matrix dimensions from input
        create a list of lists and read the numbers into it
        in case there are not enough numbers given in the input
        print an error message and return None
        error message should be "Error: Invalid input for the matrix"
    '''
    roww = []
    for index in range(matlen[0]):
        row = input()
        #print(row)
        row = list(map(int, row.split(' ')))
        roww.append(row)
    if matlen[0] != len(roww):
        return None
    for index in roww:
        if len(index) != matlen[1]:
            return None
    return roww
# def input_format(matrix, matrixlst):

def main():
    '''Main Function for Matrices'''
    # read matrix 1
    matlen1 = input()
    matlen1 = list(map(int, matlen1.split(',')))
    matrix1 = read_matrix(matlen1)
    matlen2 = input()
    matlen2 = list(map(int, matlen2.split(',')))
    matrix2 = read_matrix(matlen2)
    if matrix1 == None or matrix2 == None:
        print("Error: Invalid input for the matrix")
    else:
        matrix_add = add_matrix(matrix1, matrix2)
        print(matrix_add)
        matrix_mult = mult_matrix(matrix1, matrix2)
        print(matrix_mult)

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()
