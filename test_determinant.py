
import unittest

from main import calculate_determinant


class TestDeterminant(unittest.TestCase):

    def test_matrix_1x1(self):
        matrix = [[5]]
        self.assertEqual(calculate_determinant(matrix), 5)

    def test_matrix_2x2(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        self.assertEqual(calculate_determinant(matrix), -2)

    def test_identity_matrix(self):
        matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ]
        self.assertEqual(calculate_determinant(matrix), 1)

    def test_zero_matrix(self):
        matrix = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(calculate_determinant(matrix), 0)

    def test_singular_matrix(self):
        matrix = [
            [1, 2],
            [2, 4]
        ]
        self.assertEqual(calculate_determinant(matrix), 0)

    def test_row_swap(self):
        matrix = [
            [0, 1],
            [1, 0]
        ]
        self.assertEqual(calculate_determinant(matrix), -1)

    def test_matrix_3x3(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 10]
        ]
        self.assertEqual(calculate_determinant(matrix), -3)

    def test_original_matrix_unchanged(self):
        matrix = [
            [1, 2],
            [3, 4]
        ]
        original = [row[:] for row in matrix]

        calculate_determinant(matrix)

        self.assertEqual(matrix, original)


if __name__ == "__main__":
    unittest.main()
