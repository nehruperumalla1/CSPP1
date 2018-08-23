import copy
def mult_matrix(m1, m2):
    '''
        check if the matrix1 columns = matrix2 rows
        mult the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for mult
        and return None
        error message should be "Error: Matrix shapes invalid for mult"
    '''
    if len(m1) != len(m2[0]):
        print("Error: Matrix shapes invalid for mult")
        return None
    matmul = copy.deepcopy(m1)
    mat = []
    for index in range(len(m1)):
        m = []
        for jindex in range(len(m2[0])):
                # matmul[index][jindex] = 0
                sum1 = 0
                for kindex in range(len(m2)):
                    sum1 += m1[index][kindex] * m2[kindex][jindex]
                m.append(sum1)
        mat.append(m)
    return mat
def add_matrix(m1, m2):
    '''
        check if the matrix shapes are similar
        add the matrices and return the result matrix
        print an error message if the matrix shapes are not valid for addition
        and return None
        error message should be "Error: Matrix shapes invalid for addition"
    '''
    if len(m1) != len(m2):
        print("Error: Matrix shapes invalid for addition")
        return None
    matsum = copy.deepcopy(m1)
    for index in range(len(m1)):
        for jindex in range(len(m2[0])):
            matsum[index][jindex] += m2[index][jindex]
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
