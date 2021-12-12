import unittest


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointer, move from left & right to the center, skipping non-characters
        i, j = 0, len(s)-1
        result = True
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                result = False
                break
            i += 1
            j -= 1
        return result


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertTrue(self.solution.isPalindrome("A man, a plan, a canal: Panama"))

    def test_2(self):
        self.assertFalse(self.solution.isPalindrome("race a car"))

    def test_3(self):
        self.assertTrue(self.solution.isPalindrome(" "))


if __name__ == "__main__":
    unittest.main()
