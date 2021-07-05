import unittest
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            # include next num in sum or just start fromo next list element?
            sum = max(nums[i], sum+nums[i])
            # keep the track for global maximum
            max_sum = max(max_sum, sum)
        return max_sum


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_2(self):
        self.assertEqual(self.solution.maxSubArray([5, 4, -1, 7, 8]), 23)

    def test_3(self):
        self.assertEqual(self.solution.maxSubArray([1]), 1)


if __name__ == "__main__":
    unittest.main()
