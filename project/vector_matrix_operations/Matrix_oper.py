def matrix_addition(mat1, mat2):
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrix should have same sizes")

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result


def matrix_multiplication(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        raise ValueError("The number of columns in the first matrix must equal the number of rows in the other matrix.")

    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            sum_val = 0
            for k in range(len(mat2)):
                sum_val += mat1[i][k] * mat2[k][j]
            row.append(sum_val)
        result.append(row)
    return result


def matrix_transpose(matrix):
    if not matrix:
        return []

    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)
    return result
