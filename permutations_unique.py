import unittest
from copy import deepcopy
from collections import Counter
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans, curr =  list(), list()
        cnt = Counter(nums)
        def bt(curr):
            if len(curr) == len(nums):
                    ans.append(curr[:])
                    return
            for n in cnt:
                if cnt[n] > 0:
                    cnt[n] -= 1
                    bt(curr + [n])
                    cnt[n] += 1

            return
        
        bt([])
        return ans


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        nums = [1, 2, 3]
        result = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
        self.assertEqual(result, self.solution.permuteUnique(nums))

    def test_2(self):
        nums = [0, 1]
        result = [[0, 1], [1, 0]]
        self.assertEqual(result, self.solution.permuteUnique(nums))

    def test_3(self):
        nums = [1]
        result = [[1]]
        self.assertEqual(result, self.solution.permuteUnique(nums))


if __name__ == "__main__":
    unittest.main()
