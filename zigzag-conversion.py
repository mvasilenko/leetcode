import unittest


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        [0] -> 'P'
        [1] -> 'A'
        [2] -> 'Y'
        '''

        if numRows == 1:
            return s

        step = 1
        rows = ['' for i in range(numRows)]
        i = 0
        for c in s:
            rows[i] += c
            # going up until the end of numRows, then going down and again
            if (i == 0 and step == -1) or (i == numRows - 1 and step == 1):
                step = step * -1
            i += step

        res = ''
        for i in range(len(rows)):
            res += ''.join(rows[i])
        return res


class testSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.convert(
            'PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')

    def test_2(self):
        self.assertEqual(self.solution.convert('AB', 1), 'AB')

    def test_3(self):
        self.assertEqual(self.solution.convert('ABC', 1), 'ABC')


if __name__ == "__main__":
    unittest.main()
