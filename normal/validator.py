from normal.matrix import *


def __validate_columns_number_equality(matrix_1, matrix_2):
    if get_cols_number(matrix_1) != get_cols_number(matrix_2):
        raise ValueError('Invalid sizes of matrices')


def __validate_rows_number_equality(matrix_1, matrix_2):
    if get_rows_number(matrix_1) != get_rows_number(matrix_2):
        raise ValueError('Invalid sizes of matrices')


def __validate_sizes_equality(matrix_1, matrix_2):
    if get_cols_number(matrix_1) != get_rows_number(matrix_2):
        raise ValueError('Invalid sizes of matrices')


def __validate_if_matrix_empty(matrix):
    if len(matrix) == 0:
        raise ValueError("Empty matrix")


def __validate_if_first_row_empty(matrix):
    if len(matrix[0]) == 0:
        raise ValueError("First empty row of matrix")


def __validate_rows_length_equality(matrix):
    first_row_len = len(matrix[0])
    for row in matrix:
        if len(row) != first_row_len:
            raise ValueError("Different sizes of matrix rows")


def __validate_matrix(matrix):
    __validate_if_matrix_empty(matrix)
    __validate_if_first_row_empty(matrix)
    __validate_rows_length_equality(matrix)


def validate_matrices_to_add(matrix_1, matrix_2):
    __validate_columns_number_equality(matrix_1, matrix_2)
    __validate_rows_number_equality(matrix_1, matrix_2)
    __validate_matrix(matrix_1)
    __validate_matrix(matrix_2)


def validate_matrices_to_multiply(matrix_1, matrix_2):
    __validate_matrix(matrix_1)
    __validate_matrix(matrix_2)
    __validate_sizes_equality(matrix_1, matrix_2)
