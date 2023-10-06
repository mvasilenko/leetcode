import unittest
from copy import deepcopy
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans, curr = list(), list()

        def bt(curr):
            if len(curr) == len(nums):
                ans.append(deepcopy(curr))
                return

            for n in nums:
                if n not in curr:
                    curr.append(n)
                    bt(curr)
                    curr.pop()
            return

        bt([])
        return ans


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        nums = [1, 2, 3]
        result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(result, self.solution.permute(nums))

    def test_2(self):
        nums = [0, 1]
        result = [[0, 1], [1, 0]]
        self.assertEqual(result, self.solution.permute(nums))

    def test_3(self):
        nums = [1]
        result = [[1]]
        self.assertEqual(result, self.solution.permute(nums))


if __name__ == "__main__":
    unittest.main()
