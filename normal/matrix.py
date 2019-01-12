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
