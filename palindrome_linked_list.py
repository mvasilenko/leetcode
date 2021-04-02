# Definition for singly-linked list.
import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # dummy solution, convert numbers to string, check original == reversed string using python ::-1
        string = ""
        while True:
            string += str(head.val)
            if head.next is None:
                break
            head = head.next
        return string == string[::-1]


class TestSolutinIsPalindromeLinkedList(unittest.TestCase):
    solution = Solution()

    def test_not_palindrome(self):
        a, b = ListNode(1), ListNode(2)
        a.next = b
        # [1,2] -> False
        self.assertFalse(self.solution.isPalindrome(a))

    def test_is_palindrome(self):
        a, b, c, d = ListNode(1), ListNode(2), ListNode(2), ListNode(1)
        a.next = b
        b.next = c
        c.next = d
        # [1,2,2,1] -> True
        self.assertTrue(self.solution.isPalindrome(a))


if __name__ == "__main__":
    unittest.main()
