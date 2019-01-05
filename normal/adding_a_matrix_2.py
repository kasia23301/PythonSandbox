from normal.validator import validate_of_adding_matrices
from normal.matrix import *


def sum_row_element(i, j):
    return i + j


def iteration_after_element_of_matrix(row_of_the_first_matrix, row_of_the_second_matrix):
    score = []
    for elem1, elem2 in zip(row_of_the_first_matrix, row_of_the_second_matrix):
        result_summing = sum_row_element(elem1, elem2)
        score.append(result_summing)
    return score


def adding_a_matrix(matrix_1, matrix_2):
    validate_of_adding_matrices(matrix_1, matrix_2)
    matrix_1_rows_num = get_rows_number(matrix_1)
    matrix_2_rows_num = get_rows_number(matrix_2)
    for row_of_the_first_matrix in range(matrix_2_rows_num):
        row_of_the_first_matrix = get_nth_row(matrix_2, row_of_the_first_matrix)
    for row_of_the_second_matrix in range(matrix_1_rows_num):
        row_of_the_second_matrix = get_nth_row(matrix_1, row_of_the_second_matrix)
        result = iteration_after_element_of_matrix(row_of_the_first_matrix, row_of_the_second_matrix)
    return result
