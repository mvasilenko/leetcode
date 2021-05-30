import unittest
from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # https://www.quora.com/How-would-you-explain-an-algorithm-that-generates-permutations-using-lexicographic-ordering
        # step 1 - find largest x where P[x] < P[x+1]
        x = -1
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                x = i

        # if such element was not found, skip to step 4 - reverse and done
        if x > -1:
            # step 2 - find largest y where P[x] < P[y]
            y = -1
            for j in range(len(nums)):
                if nums[x] < nums[j]:
                    y = j
            # step 3 - swap P[x] and P[y]
            nums[x], nums[y] = nums[y], nums[x]

        # step 4 - reverse P[x+1...n]
        l, r = x+1, len(nums)-1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        nums = [1, 2, 3]
        nums_next_permutation = [1, 3, 2]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums_next_permutation, nums)

    def test_2(self):
        nums = [3, 2, 1]
        nums_next_permutation = [1, 2, 3]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums_next_permutation, nums)

    def test_3(self):
        nums = [1, 1, 5]
        nums_next_permutation = [1, 5, 1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums_next_permutation, nums)

    def test_4(self):
        nums = [1]
        nums_next_permutation = [1]
        self.solution.nextPermutation(nums)
        self.assertEqual(nums_next_permutation, nums)


if __name__ == "__main__":
    unittest.main()
