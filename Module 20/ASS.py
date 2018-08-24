def access_elements(mat1):
    ele = input("Enter the location")
    ele = list(map(int, ele.split()))
    x = len(mat1)
    m = ele[0]
    n = ele[1]
    hor = []
    ver = []
    diag = []
    sum1 = []
    for i in range(x):
        for j in range(len(mat1[i])):
            if i == m:
                hor.append(mat1[i][j])
            if j == n:
                ver.append(mat1[i][j])
            if m == n:
                if i == j:
                    diag.append(mat1[i][j])
    sum1.append(hor)
    sum1.append(ver)
    k = m-n
    for i in range(x):
        for j in range(len(mat1[i])):
            if m + n == i + j:
                diag.append(mat1[i][j])
            if m - n == i - j:
                diag.append(mat1[i][j])
    diag = set(diag)
    diag = list(diag)
    mul = 1
    for i in range(len(ver)):
        mul = mul * ver[i]
    print(mul)
    print(hor)
    print(ver)
    print(diag)
    sum1.append(diag)
    print(sum1)
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
    # matlen2 = input()
    # matlen2 = list(map(int, matlen2.split(',')))
    # matrix2 = read_matrix(matlen2)
    if matrix1 is None:
        print("Error: Invalid input for the matrix")
    else:
        elements = access_elements(matrix1)

    # read matrix 2

    # add matrix 1 and matrix 2

    # multiply matrix 1 and matrix 2

if __name__ == '__main__':
    main()