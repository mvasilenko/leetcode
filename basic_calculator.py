import math
import unittest


class Solution:
    def calculate(self, s: str) -> int:
        cur, op, stack = 0, "+", []
        for i in range(len(s)):
            # support multi-digit numbers
            if s[i].isdigit():
                cur = cur * 10 + int(s[i])
            # match "+-*/", strip whitespaces, evaluate last operation
            if (not s[i].isdigit() and not s[i].isspace()) or i == (len(s) - 1):
                if op == "+":
                    stack.append(cur)
                elif op == "-":
                    stack.append(-cur)
                elif op == "*":
                    stack.append(stack.pop() * cur)
                elif op == "/":
                    stack.append(math.trunc(stack.pop() / cur))
                # update operation which should be done at next step
                op = s[i]
                # reset current number, needed for multi-digit support
                cur = 0
        return sum(stack)


class TestSolutionBasicCalculator(unittest.TestCase):
    solution = Solution()

    def test_3_plus_2_multiply_2(self):
        self.assertEqual(self.solution.calculate("3+2*2"), 7)

    def test_3_div_2(self):
        self.assertEqual(self.solution.calculate(" 3/2 "), 1)

    def test_3_plus_5_div_2(self):
        self.assertEqual(self.solution.calculate(" 3+5 / 2 "), 5)


if __name__ == "__main__":
    unittest.main()
