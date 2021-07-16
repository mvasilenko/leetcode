import unittest
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, area, area_max = 0, len(height)-1, 0, 0
        while i < j:
            area = max(area, (j-i)*min(height[i], height[j]))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return area


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_2(self):
        self.assertEqual(self.solution.maxArea([1, 1]), 1)

    def test_3(self):
        self.assertEqual(self.solution.maxArea([4, 3, 2, 1, 4]), 16)

    def test_4(self):
        self.assertEqual(self.solution.maxArea([1, 2, 1]), 2)

    def test_5(self):
        self.assertEqual(self.solution.maxArea([2, 3, 4, 5, 18, 17, 6]), 17)

if __name__ == "__main__":
    unittest.main()