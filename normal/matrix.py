def get_cols_number(matrix):
    if len(matrix) == 0:
        return 0
    else:
        return len(matrix[0])


def get_rows_number(matrix):
    return len(matrix)


def get_nth_row(matrix, n):
    return matrix[n]


def get_nth_col(matrix, n):
    col = []
    for row in matrix:
        col.append(row[n])
    return col





    # for i in range()
    #     a = matrix_1[0]
    # if len(a) == len(matrix_2):
    #     a = matrix_1[0]
    #     c = matrix_2[0]
    #     d = matrix_1[1]
    #     new_matrix = []
    #     i = 0
    #     b = matrix_2[i]
    #     f = b[0]
    #     for e in range(len(a) * len(c)):
    #         for number in a:
    #             result = number * f
    #             new_matrix.append(result)
    #             i += 1
    #         a = d
    #         f = b[1]
    # else:
    #     return ArithmeticError("Nieprawidłowe dane")
    #
    # return sum(new_matrix)
