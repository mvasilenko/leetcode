import unittest
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = collections.defaultdict(int)
        for c in s:
            d[c] += 1
        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.firstUniqChar("leetcode"), 0)

    def test_2(self):
        self.assertEqual(self.solution.firstUniqChar("loveleetcode"), 2)

    def test_3(self):
        self.assertEqual(self.solution.firstUniqChar("aabb"), -1)

    def test_4(self):
        self.assertEqual(self.solution.firstUniqChar("abcdefgh"), 0)

if __name__ == "__main__":
    unittest.main()
