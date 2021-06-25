import math
import unittest
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []
        for i in range(len(nums)):
            if nums[i] != val:
                result.append(nums[i])
        for i in range(len(result)):
            nums[i] = result[i]
        return len(result)

    def removeElementUsingPointers(self, nums: List[int], val: int) -> int:
        # print("begin")
        slow, fast = 0, len(nums)
        while slow < fast:
            if nums[slow] == val:
                nums[slow] = nums[fast-1]
                fast -= 1
                #print(f"decreased fast pointer, now it is {fast} nums[fast]={nums[fast]}")
                # print(nums)
            else:
                slow += 1
                #print(f"increased slow pointer, now it is {slow} nums[slow]={nums[slow]}")
                # print(nums)

        return fast


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.removeElement([3, 2, 2, 3], 2), 2)

    def test_2(self):
        self.assertEqual(self.solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)

    def test_3(self):
        self.assertEqual(self.solution.removeElement([1], 1), 0)

    def test_4(self):
        self.assertEqual(self.solution.removeElement([2], 3), 1)

    def test_11(self):
        self.assertEqual(self.solution.removeElementUsingPointers([3, 2, 2, 3], 2), 2)

    def test_12(self):
        self.assertEqual(self.solution.removeElementUsingPointers([0, 1, 2, 2, 3, 0, 4, 2], 2), 5)

    def test_13(self):
        self.assertEqual(self.solution.removeElementUsingPointers([1], 1), 0)

    def test_14(self):
        self.assertEqual(self.solution.removeElementUsingPointers([2], 3), 1)


if __name__ == "__main__":
    unittest.main()
