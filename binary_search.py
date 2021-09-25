import unittest
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = int((right-left)/2)+left
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1
            else:
                return mid
        return -1


class TestSolutionBinarySearch(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.search([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_2(self):
        self.assertEqual(self.solution.search([-1, 0, 3, 5, 9, 12], 2), -1)


if __name__ == "__main__":
    unittest.main()
