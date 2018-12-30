from normal.validator import validate_matrices
from normal.matrix import *


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


def multiply_matrix(matrix_1, matrix_2):
    validate_matrices(matrix_1, matrix_2)
    matrix_1_rows_num = get_rows_number(matrix_1)
    matrix_2_rows_num = get_rows_number(matrix_2)
    matrix_2_cols_num = get_cols_number(matrix_2)
    result_matrix = __init_result_matrix_of_size(matrix_1_rows_num, matrix_2_rows_num)
    for col_num in range(matrix_2_cols_num):
        col = get_nth_col(matrix_2, col_num)
        for row_num in range(matrix_1_rows_num):
            row = get_nth_row(matrix_1, row_num)
            result_matrix[row_num][col_num] = __compute_sum_of_multiplications(row, col)
    return result_matrix
