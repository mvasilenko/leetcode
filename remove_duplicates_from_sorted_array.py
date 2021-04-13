from typing import List
import unittest


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # pointer to list with unique elements only
        unique_idx = 0
        for idx in range(1, len(nums)):
            if nums[idx] != nums[unique_idx]:
                unique_idx += 1
                nums[unique_idx] = nums[idx]

        # need to increase result after the loop
        # or we will miss final unique element
        unique_idx += 1

        return unique_idx


class TestSolutionRemoveDuplicates(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.removeDuplicates([1, 1, 2]), 2)

    def test_2(self):
        self.assertEqual(self.solution.removeDuplicates(
            [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)

    def test_3(self):
        self.assertEqual(self.solution.removeDuplicates(
            [1, 1, 1, 2, 2, 2, 2, 4, 5, 6, 6, 8]), 6)

    def test_4(self):
        self.assertEqual(self.solution.removeDuplicates([0]), 1)

    def test_5(self):
        self.assertEqual(self.solution.removeDuplicates([]), 0)


if __name__ == "__main__":
    unittest.main()
