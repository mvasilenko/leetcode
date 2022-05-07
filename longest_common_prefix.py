import math
import unittest
from typing import List


class Solution:
    def longestCommonPrefixNaive(self, strs: List[str]) -> str:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            prefix = ""
            shortest = math.inf
            for s in strs:
                shortest_len = min(shortest, len(s))
            # print(shortest_len)
            continue_search = True
            while len(prefix) < shortest_len and continue_search and shortest_len > 0:
                # print(f"len(prefix)={len(prefix)}")
                if len(strs[0]) > len(prefix):
                    prefix += strs[0][len(prefix)]
                else:
                    break
                for s in strs:
                    # print(f"s[0:len(prefix)]={s[0:len(prefix)]} prefix={prefix}")
                    if not s.startswith(prefix):
                        # print("break")
                        continue_search = False
                        if len(prefix) > 0:
                            prefix = prefix[:-1:]
                        # print(f"return {prefix}")
                        break

            return prefix

    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = ""
        shortest = min(strs, key=len)
        for i in range(len(shortest)):
            for s in strs:
                if s[i] != shortest[i]:
                    prefix = s[:i]
                    if i > 0:
                        return prefix
                    else:
                        return ""
        return prefix


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.longestCommonPrefix(["dog", "racecar", "car"]), "")

    def test_2(self):
        self.assertEqual(self.solution.longestCommonPrefix(["flower", "flow", "fl"]), "fl")

    def test_3(self):
        self.assertEqual(self.solution.longestCommonPrefix([""]), "")

    def test_4(self):
        self.assertEqual(self.solution.longestCommonPrefix(["a"]), "a")

    def test_5(self):
        self.assertEqual(self.solution.longestCommonPrefix(["", "b"]), "")


if __name__ == "__main__":
    unittest.main()
