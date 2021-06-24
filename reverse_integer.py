import unittest


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_str = str(abs(x))[::-1]
        x_int = int(x_str)
        if x_int > 2 ** 31 - 1 or x_int < (2 ** 31) * (-1) or x > 2 ** 31 - 1 or x < (2 ** 31) * (-1):
            x_int = 0
        else:
            x_int = x_int * sign
        return x_int


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.reverse(123), 321)

    def test_2(self):
        self.assertEqual(self.solution.reverse(-123), -321)

    def test_3(self):
        self.assertEqual(self.solution.reverse(0), 0)

    def test_4(self):
        self.assertEqual(self.solution.reverse(1563847412), 0)

    def test_5(self):
        self.assertEqual(self.solution.reverse(1534236469), 0)


if __name__ == "__main__":
    unittest.main()
