from normal.validator import validate_matrices_to_add
from normal.matrix import *


def __sum_corresponding_elements(i, j):
    return i + j


def __add_corresponding_rows(row_of_the_first_matrix, row_of_the_second_matrix):
    score = []
    for elem1, elem2 in zip(row_of_the_first_matrix, row_of_the_second_matrix):
        result_summing = __sum_corresponding_elements(elem1, elem2)
        score.append(result_summing)
    return score


def add_matrices(matrix_1, matrix_2):
    validate_matrices_to_add(matrix_1, matrix_2)
    rows_num = get_rows_number(matrix_1)
    result_matrix =[]
    for row_num in range(rows_num):
        row_of_the_first_matrix = get_nth_row(matrix_1, row_num)
        row_of_the_second_matrix = get_nth_row(matrix_2, row_num)
        result_matrix.append(__add_corresponding_rows(row_of_the_first_matrix, row_of_the_second_matrix))
    return result_matrix
