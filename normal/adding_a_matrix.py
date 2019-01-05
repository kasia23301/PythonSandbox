def number_of_rows(matrix):
    return len(matrix)


def number_of_columns(matrix):
    return len(matrix[0])


def __validate_sizes_of_columns(matrix_1, matrix_2):
    if number_of_columns(matrix_1) != number_of_columns(matrix_2):
        raise ValueError('Invalid sizes of matrices')


def __validate_if_matrix_empty(matrix):
    if len(matrix) == 0:
        raise ValueError("Empty matrix")


def __validate_sizes_of_rows(matrix_1, matrix_2):
    if number_of_rows(matrix_1) != number_of_rows(matrix_2):
        raise ValueError('Invalid sizes of matrices')


def __validate_matrix_first_empty_row(matrix):
    if len(matrix[0]) == 0:
        raise ValueError("First empty row of matrix")


def calculator(i, j):
    result = []
    summing = i + j
    result.append(summing)
    return result


def iteration_after_element_of_matrix(row_one, row):
    for i in row_one:
        for j in row:
            result_one = calculator(i, j)
    return result_one


def get_cols_number(matrix):
    if len(matrix) == 0:
        return 0
    else:
        return len(matrix[0])


def get_rows_number(matrix):
    return len(matrix)


def get_nth_row(matrix, n):
    return matrix[n]


def adding_a_matrix(matrix_1, matrix_2):
    __validate_sizes_of_columns(matrix_1, matrix_2)
    __validate_sizes_of_rows(matrix_1, matrix_2)
    __validate_if_matrix_empty(matrix_1)
    __validate_if_matrix_empty(matrix_2)
    __validate_matrix_first_empty_row(matrix_1)
    __validate_matrix_first_empty_row(matrix_2)
    matrix_1_rows_num = get_rows_number(matrix_1)
    matrix_2_rows_num = get_rows_number(matrix_2)
    for row_num_one in range(matrix_2_rows_num):
        row_one = get_nth_row(matrix_2, row_num_one)
        for row_num in range(matrix_1_rows_num):
            row = get_nth_row(matrix_1, row_num)
            result = iteration_after_element_of_matrix(row_one, row)
    return result
