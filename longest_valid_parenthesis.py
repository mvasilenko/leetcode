import unittest

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        lvp = 0
        stack = list()
        stack.append(-1)
        for c in range(len(s)):
            if s[c] == '(':
                stack.append(c)
            if s[c] == ')':
                _ = stack.pop()
                if len(stack) == 0:
                    stack.append(c)
                lvp_last = c - stack[-1]
                lvp = max(lvp, lvp_last)

        return lvp


class TestSolutionFindMaxForm(unittest.TestCase):
    solution = Solution()

    def test_2(self):
       self.assertEqual(self.solution.longestValidParentheses("(()"), 2)

    def test_4(self):
       self.assertEqual(self.solution.longestValidParentheses(")()())"), 4)

    def test_0(self):
       self.assertEqual(self.solution.longestValidParentheses(""), 0)

if __name__ == "__main__":
    unittest.main()
