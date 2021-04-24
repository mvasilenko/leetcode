import unittest


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openers = ['(', '[', '{']
        closers = [')', ']', '}']
        match = {')': '(', ']': '[', '}': '{'}
        res = False
        for c in s:
            if c in openers:
                stack.append(c)
            elif c in closers:
                # if stack is empty and we have closer bracket - invalid
                if not stack:
                    return False
                # if last stack element have no match - invalid
                if stack[-1] != match[c]:
                    return False
                del stack[-1]
            else:
                return False

        return not stack


class TestValidParentesisSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertTrue(self.solution.isValid("()"))

    def test_2(self):
        self.assertTrue(self.solution.isValid("()[]{}"))

    def test_3(self):
        self.assertFalse(self.solution.isValid("(]"))

    def test_4(self):
        self.assertFalse(self.solution.isValid("([)]"))

    def test_5(self):
        self.assertTrue(self.solution.isValid("{[]}"))


if __name__ == "__main__":
    unittest.main()
