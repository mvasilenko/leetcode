import unittest
from typing import List


class Solution:
    """
    modify matrix in-place

    1 2 3      7 4 1
    4 5 6  ->  8 5 2
    7 8 9      9 6 3

    save 7, 9->7, 3->9, 1->3, 7->1
    save 4, 8->4, 6->8, 2->6, 4->2
    """

    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        for i in range(n//2 + n % 2):  # range(2) -> 0 1
            for j in range(n//2):  # range(1) -> 0
                # print(f"i={i} j={j}")                                        # 1st pass # 2nd pass
                # print(f"save tmp [{n-1-j}][{i}] {matrix[n-1-j][i]}")        # [2][0] # [2][1]
                # print(f"next is [{n-1-i}][{n-1-j}] {matrix[n-1-i][n-1-j]}") # [2][2] # [1][2]
                # print(f"next is [{j}][{n-1-i}] {matrix[j][n-1-i]}")         # [0][2] # [0][1]
                # print(f"next is [{i}][{j}] {matrix[i][j]}")                 # [0][0] # [1][0]

                tmp = matrix[n-1-j][i]                           # save 7
                matrix[n - 1 - j][i] = matrix[n-1-i][n-1-j]      # 9 -> 7
                matrix[n - 1 - i][n - 1 - j] = matrix[j][n-1-i]  # 3 -> 9
                matrix[j][n - 1 - i] = matrix[i][j]              # 1 -> 3
                matrix[i][j] = tmp                               # 7 -> 1a

        return matrix

    def rotate_naive(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        rotated = [[0 for _ in range(n)] for _ in range(n)]
        for y in range(n):
            for x in range(n):
                rotated[x][n-y-1] = matrix[y][x]
        return rotated


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.rotate([[1, 2, 3],
                                               [4, 5, 6],
                                               [7, 8, 9]]),
                         [[7, 4, 1],
                          [8, 5, 2],
                          [9, 6, 3]])

    def test_2(self):
        self.assertEqual(self.solution.rotate([[5, 1, 9, 11],
                                               [2, 4, 8, 10],
                                               [13, 3, 6, 7],
                                               [15, 14, 12, 16]]),
                         [[15, 13, 2, 5],
                          [14, 3, 4, 1],
                          [12, 6, 8, 9],
                          [16, 7, 10, 11]])

    def test_3(self):
        self.assertEqual(self.solution.rotate([[1]]), [[1]])

    def test_4(self):
        self.assertEqual(self.solution.rotate([[1, 2], [3, 4]]), [[3, 1], [4, 2]])


if __name__ == "__main__":
    unittest.main()
