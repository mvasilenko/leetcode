import unittest
from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zeroes,ones = m,n
        count_strs = [[0 for _ in range(ones+1)] for _ in range(zeroes+1)]
        for str in strs:
            s1= str.count("1")
            s0 = len(str) - s1
            for i in range(zeroes, s0-1, -1):
                for j in range(ones, s1-1, -1):
                    if count_strs[i][j] < count_strs[i-s0][j-s1]+1:
                        count_strs[i][j] = count_strs[i-s0][j-s1]+1
        return count_strs[zeroes][ones]

class TestSolutionFindMaxForm(unittest.TestCase):
    solution = Solution()

    def test_5_3(self):
       strs, m, n = ["10","0001","111001","1","0"], 5, 3
       self.assertEqual(self.solution.findMaxForm(strs, m, n), 4)

    def test_1_1(self):
       strs, m, n = ["10","0","1"], 1, 1
       self.assertEqual(self.solution.findMaxForm(strs, m, n), 2)

if __name__ == "__main__":
    #print(Solution.findMaxForm(["10","0001","111001","1","0"], 5, 3))
    unittest.main()
