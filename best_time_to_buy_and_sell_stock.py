import unittest
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price, profit = float("inf"), 0
        for i in range(0, len(prices)):
            buy_price = min(buy_price, prices[i])
            profit = max(profit, prices[i]-buy_price)
        return profit


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)

    def test_2(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_3(self):
        self.assertEqual(self.solution.maxProfit([1, 2]), 1)

    def test_4(self):
        self.assertEqual(self.solution.maxProfit([1, 2, 3]), 2)


if __name__ == "__main__":
    unittest.main()
