import unittest

# https://leetcode.com/problems/is-subsequence/discuss/87254/Straight-forward-Java-simple-solution
# two pointers approach
# iterate through t and increment s if the current s matches t.
# If you exhaust t you have failed, if you exhaust s you have succeeded.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index_s, index_t = 0, 0
        if len(s) == 0:
            return True
        while index_t < len(t):
            #print(f"index_s={index_s} s[index_s]={s[index_s]} index_t={index_t} t[index_t]={t[index_t]}")
            if s[index_s] == t[index_t]:
                index_s += 1
                # we've exhausted s?
                if index_s == len(s):
                    return True
            index_t += 1
        # we've exhaused t
        return False


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertTrue(self.solution.isSubsequence("abc", "ahbgdc"))

    def test_2(self):
        self.assertFalse(self.solution.isSubsequence("axc", "ahbgdc"))

    def test_3(self):
        self.assertTrue(self.solution.isSubsequence("", "ahbgdc"))

    def test_4(self):
        self.assertTrue(self.solution.isSubsequence("b", "abc"))


if __name__ == "__main__":
    unittest.main()
