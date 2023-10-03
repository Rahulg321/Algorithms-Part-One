def matrix(m, n):
    target = []
    for i in range(m):
        row = []
        for j in range(n):
            element = int(input(f"enter value at[{i}][{j}] ==>"))
            row.append(element)

        target.append(row)

    return target


def initializeEmptyMatrix(m, n):
    target = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(0)

        target.append(row)

    return target


# m = int(input("enter the number of rows \n"))
# n = int(input("enter the number of columns \n"))


# A = matrix(m, n)
# B = matrix(m, n)


def print_matrix(A):
    print("*********************************************")
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end=" ")

        print()
    # print("*********************************************")


# print_matrix(A)
# print_matrix(B)


A = [[2, 0], [0, 2]]
B = [[1, 2], [1, 5]]


def multiplyMatrix(A, B):
    if len(A[0]) != len(B):
        print("invalid matrix")
        print("cannot multiply them")
        return False

    m = len(A)
    n = len(B)
    k = len(B[0])

    result = []

    for i in range(m):
        row = []

        for j in range(k):
            productElement = 0
            for e in range(n):
                productElement += A[i][e] * B[e][j]

            row.append(productElement)

        result.append(row)

    print("printing after multiplying is ")
    print_matrix(result)


def addMatrix(A, B):
    result = []
    """
        works on the assumption that
        Both a and b are guranteed to have rows * cols => [m * n]
    """

    for i in range(len(A)):
        row = []

        for j in range(len(A[i])):
            sum = A[i][j] + B[i][j]

            row.append(sum)

        result.append(row)

    return result


multiplyMatrix(A, B)
