import unittest


class Solution:
    def intToRoman(self, num: int) -> str:
        s = str(num)
        res = ""
        roman_to_num = [
            ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
            ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
            ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
            ["", "M", "MM", "MMM"]
        ]
        # go from right to left, substitute 1234567890 numbers by romanian IVCXDM's
        for i in range(len(s), 0, -1):
            res = roman_to_num[len(s)-i][int(s[i-1])] + res
        return res


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.intToRoman(3), "III")

    def test_2(self):
        self.assertEqual(self.solution.intToRoman(4), "IV")

    def test_3(self):
        self.assertEqual(self.solution.intToRoman(9), "IX")

    def test_4(self):
        self.assertEqual(self.solution.intToRoman(58), "LVIII")

    def test_5(self):
        self.assertEqual(self.solution.intToRoman(1994), "MCMXCIV")


if __name__ == "__main__":
    unittest.main()
