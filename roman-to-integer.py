import unittest


class Solution:
    def romanToInt(self, s: str) -> int:
        map = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000}

        res = cur = prev = 0
        for i in range(len(s)-1, -1, -1):
            prev = cur
            cur = map[s[i]]
            if cur >= prev:
                res += cur
            else:
                res -= cur
        return res

class TestRomanToInt(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.romanToInt("III"),3)

    def test_2(self):
        self.assertEqual(self.solution.romanToInt("IIII"),4)

    def test_3(self):
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)

    def test_4(self):
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)

if __name__ == "__main__":
    unittest.main()
