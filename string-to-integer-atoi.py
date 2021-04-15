import unittest


class Solution:
    def myAtoi(self, s: str) -> int:

        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        i = 0
        sign = 1
        res = 0
        positive_idx = 0
        negative_idx = 0
        positive_count = 0
        negative_count = 0

        # skip spaces in the beginning
        while i < len(s) and s[i] == ' ':
            i += 1

        # find positive signs
        while i < len(s) and s[i] == '+':
            i += 1
            sign = 1
            positive_idx = i
            positive_count += 1

        # find negative signs
        while i < len(s) and s[i] == '-':
            i += 1
            sign = -1
            negative_idx = i
            negative_count += 1

        if (positive_count + negative_count) > 1:
            return 0
        if positive_idx > 0 and negative_idx > 0:
            return 0

        while i < len(s) and s[i].isdigit():
            res *= 10
            res += int(s[i])
            i += 1

        res *= sign

        if res > MAX_INT:
            res = MAX_INT
        elif res < MIN_INT:
            res = MIN_INT

        return res


class TestMyAtoiSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.myAtoi("42"), 42)

    def test_2(self):
        self.assertEqual(self.solution.myAtoi("   -42"), -42)

    def test_3(self):
        self.assertEqual(self.solution.myAtoi("4193 with words"), 4193)

    def test_4(self):
        self.assertEqual(self.solution.myAtoi("words and 987"), 0)

    def test_5(self):
        self.assertEqual(self.solution.myAtoi("-91283472332"), -2147483648)

    def test_6(self):
        self.assertEqual(self.solution.myAtoi("-+12"), 0)

    def test_7(self):
        self.assertEqual(self.solution.myAtoi("+-12"), 0)


if __name__ == "__main__":
    unittest.main()
