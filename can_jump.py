import unittest
from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = j = 0
        while i < len(nums)-1 and i <= j:
            j = max(j, i+nums[i])
            #print(i,j)
            i += 1
        #print("end")
        return j >= len(nums)-1


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertTrue(self.solution([3, 0, 8, 2, 0, 0, 1]))

    def test_2(self):
        self.assertFalse(self.solution([0, 2, 3]))

    def test_3(self):
        self.assertFalse(self.solution([3, 2, 1, 0, 4]))

    def test_4(self):
        self.assertTrue(self.solution([2, 3, 1, 1, 4]))

    def test_5(self):
        self.assertTrue(self.solution([0]))

    def test_6(self):
        self.assertTrue(self.solution([2, 0]))

    def test_7(self):
        self.assertTrue(self.solution([2, 5, 0, 0]))
