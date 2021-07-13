import unittest
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals_sorted = sorted(intervals, key=lambda intervals: intervals[0])
        last_interval = intervals_sorted[0]

        result = [last_interval]
        for current_interval in intervals_sorted:
            current_left = current_interval[0]
            current_right = current_interval[1]

            # not used can be removed, just for clarity
            last_left = last_interval[0]

            last_right = last_interval[1]
            if last_right >= current_left:
                # extend interval
                last_interval[1] = max(current_right, last_right)
            else:
                # no overlaps
                last_interval = current_interval
                result.append(last_interval)

        return result


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.merge(
            [[1, 3], [2, 6], [8, 10], [15, 18]]),
            [[1, 6], [8, 10], [15, 18]]
        )

    def test_2(self):
        self.assertEqual(self.solution.merge(
            [[1, 4], [0, 4]]),
            [[0, 4]]
        )

    def test_3(self):
        self.assertEqual(self.solution.merge(
            [[1, 4], [0, 0]]),
            [[0, 0], [1, 4]]
        )

    def test_4(self):
        self.assertEqual(self.solution.merge(
            [[1, 4], [4, 5]]),
            [[1, 5]]
        )

if __name__ == "__main__":
    unittest.main()
