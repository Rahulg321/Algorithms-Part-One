def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end=" ")

        print()


def add_matrix(matrix1, matrix2):
    matrix3 = [[0,0,0], [0,0,0], [0,0,0]]
    """
        matrix1 === matrix2 === [m * n]
    """

    for i in range(len(matrix1)):
        for j in range(len(matrix1[i])):
            sum = matrix1[i][j] + matrix2[i][j]

            matrix3[i][j] = sum

    return matrix3


A = [[1, 2, 7], [8, 11, 12], [2, 8, 1]]
B = [[1, 7, 4], [1, 2, 7], [0, 3, 5]]

C = add_matrix(A, B)

print_matrix(C)
