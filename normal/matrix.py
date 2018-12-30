def __get_cols_number(matrix):
    return len(matrix[0])


def __get_rows_number(matrix):
    return len(matrix)


def __get_nth_row(matrix, n):
    return matrix[n]


def __get_nth_col(matrix, n):
    col = []
    for row in matrix:
        col.append(row[n])
    return col


def __init_result_matrix_of_size(rows_num, cols_num):
    matrix = []
    for row_num in range(rows_num):
        matrix.append([])
        for col_num in range(cols_num):
            matrix[row_num].append(0)
    return matrix


def __compute_sum_of_multiplications(vector1, vector2):
    sum = 0
    for index, value in enumerate(vector1):
        sum += value * vector2[index]
    return sum


def __validate_sizes(matrix_1, matrix_2):
    if __get_cols_number(matrix_1) != __get_rows_number(matrix_2):
        raise ValueError('Invalid sizes of matrices')


def __validate_if_matrix_empty(matrix):
    if len(matrix) == 0:
        raise ValueError("Empty matrix")


def __validate_matrix_first_empty_row(matrix):
    if len(matrix[0]) == 0:
        raise ValueError("First empty row of matrix")


def __validate_rows_length_equality(matrix):
    first_row_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_len:
            raise ValueError("Different sizes of matrix rows")


def __validate_matrix(matrix):
    __validate_if_matrix_empty(matrix)
    __validate_matrix_first_empty_row(matrix)
    __validate_rows_length_equality(matrix)


def __validate_matrices(matrix_1, matrix_2):
    __validate_sizes(matrix_1, matrix_2)
    __validate_matrix(matrix_1)
    __validate_matrix(matrix_2)


def multiply_matrix(matrix_1, matrix_2):
    __validate_matrices(matrix_1, matrix_2)
    matrix_1_rows_num = __get_rows_number(matrix_1)
    matrix_2_rows_num = __get_rows_number(matrix_2)
    matrix_2_cols_num = __get_cols_number(matrix_2)
    result_matrix = __init_result_matrix_of_size(matrix_1_rows_num, matrix_2_rows_num)
    for col_num in range(matrix_2_cols_num):
        col = __get_nth_col(matrix_2, col_num)
        for row_num in range(matrix_1_rows_num):
            row = __get_nth_row(matrix_1, row_num)
            result_matrix[row_num][col_num] = __compute_sum_of_multiplications(row, col)
    return result_matrix





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
