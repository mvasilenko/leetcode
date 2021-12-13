import unittest
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set()
        for i in arr:
            if i*2 in s or i/2 in s:
                return True
            s.add(i)
        return False


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertTrue(self.solution.checkIfExist([10, 2, 5, 3]))

    def test_2(self):
        self.assertTrue(self.solution.checkIfExist([7, 1, 14, 11]))

    def test_3(self):
        self.assertFalse(self.solution.checkIfExist([3, 1, 7, 11]))

    def test_4(self):
        self.assertTrue(self.solution.checkIfExist([0, 0]))

    def test_5(self):
        self.assertTrue(self.solution.checkIfExist([-10, 12, -20, -8, 15]))

    def test_6(self):
        self.assertTrue(self.solution.checkIfExist([2, 3, 3, 0, 0]))

    def test_7(self):
        self.assertFalse(self.solution.checkIfExist([7, -19, -6, 8, 11, -6, -6]))


if __name__ == "__main__":
    unittest.main()
