import unittest


class Solution:
    def isPalindrome(self, x: int) -> bool:
        is_palindrome = True
        x_str = str(x)
        left, right = 0, len(x_str)-1
        while left < right:
            if x_str[left] != x_str[right]:
                is_palindrome = False
                break
            left += 1
            right -= 1
        return is_palindrome


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertTrue(self.solution.isPalindrome(121))

    def test_2(self):
        self.assertFalse(self.solution.isPalindrome(-121))

    def test_3(self):
        self.assertFalse(self.solution.isPalindrome(10))

    def test_4(self):
        self.assertFalse(self.solution.isPalindrome(-101))


if __name__ == "__main__":
    unittest.main()
