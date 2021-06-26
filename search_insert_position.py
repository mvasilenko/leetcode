import unittest
from typing import List


class Solution:
    def searchInsertNaive(self, nums: List[int], target: int) -> int:
        i = 0
        if nums[len(nums)-1] < target:
            return len(nums)
        while nums[i] < target:
            i += 1
        return i

    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums[len(nums)-1] < target:
            return len(nums)
        left, right = 0, len(nums)-1
        # binary search
        while left <= right:
            middle = left + int((right - left)/2)
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return left


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 5), 2)

    def test_2(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 2), 1)

    def test_3(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 7), 4)

    def test_4(self):
        self.assertEqual(self.solution.searchInsert([1, 3, 5, 6], 0), 0)

    def test_5(self):
        self.assertEqual(self.solution.searchInsert([1], 0), 0)


if __name__ == "__main__":
    unittest.main()
