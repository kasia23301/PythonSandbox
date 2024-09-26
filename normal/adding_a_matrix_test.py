import unittest
from normal.adding_a_matrix import add_matrices


class MyTestCase(unittest.TestCase):
    def test_adding_a_matrix(self):
        # given
        matrix_1 = [[2, 1, 3],
                    [8, 4, 0]]
        matrix_2 = [[1, 3, 2],
                    [2, 0, 1]]
        # when
        result_matrix = add_matrices(matrix_1, matrix_2)
        # then
        expected_result_matrix = [[3, 4, 5],
                                  [10, 4, 1]]
        self.assertEqual(expected_result_matrix, result_matrix)

    def test_should_return_value_error_because_empty_matrices(self):
        # given
        matrix_1 = [[]]
        matrix_2 = [[]]
        # when & then
        self.assertRaises(ValueError, add_matrices, matrix_1, matrix_2)

    def test_should_return_value_error_because_sizes_of_metrices_are_different(self):
        # given
        matrix_1 = [[1, 2, 3],
                    [4, 5, 6],
                    [5, 8, 9]]
        matrix_2 = [[7, 6, 2],
                    [9, 5, 2]]
        # when & then
        self.assertRaises(ValueError, add_matrices, matrix_1, matrix_2)

    def test_should_return_value_error_because_one_of_matrices_is_empty(self):
        # given
        matrix_1 = [[3, 7, 9],
                    [5, 2, 8]]
        matrix_2 = []
        # when & then
        self.assertRaises(ValueError, add_matrices, matrix_1, matrix_2)

    def test_should_return_value_error_because_first_empty_row_of_matrix(self):
        # given
        matrix_1 = [[],
                    [4, 5, 6]]
        matrix_2 = [[7, 6, 2],
                    [9, 5, 2],
                    [2, 5, 7]]
        # when & then
        self.assertRaises(ValueError, add_matrices, matrix_1, matrix_2)

    def test_should_return_value_error_because_matrices_are_empty(self):
        # given
        matrix_1 = []
        matrix_2 = []
        # when & then
        self.assertRaises(ValueError, add_matrices, matrix_1, matrix_2)


if __name__ == '__main__':
    unittest.main()
