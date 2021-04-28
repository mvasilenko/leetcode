from typing import List
import unittest

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = ptr = ListNode()
        # empty input case handle
        if not l1:
            return l2
        if not l2:
            return l1

        # break from the loop when reaching l1 or l2 end
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                l1 = l1.next
            else:
                ptr.next = l2
                l2 = l2.next
            ptr = ptr.next

        # add what's remained
        if l1:
            ptr.next = l1
        if l2:
            ptr.next = l2

        # return head of the merged linked list
        return res.next

    # test helper methods
    def test_make_list(self, list):
        head_node = None  # init empty pointer
        # construct linked list from end to begin
        for i in reversed(list):
            node = ListNode()
            node.val = i  # store value in node
            node.next = head_node  # store pointer to next node
            head_node = node  # move pointer to head node
        return head_node

    def test_show_list(self, node_list):
        res = []
        while node_list:
            res.append(node_list.val)
            node_list = node_list.next
        return res


class TestMergeTwoListsSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        input_l1 = [1, 3, 4]
        input_l2 = [1, 2, 4]
        l1 = self.solution.test_make_list(input_l1)
        l2 = self.solution.test_make_list(input_l2)
        merged = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(self.solution.test_show_list(merged), [1, 1, 2, 3, 4, 4])

    def test_2(self):
        input_l1 = [1]
        input_l2 = [1, 3, 4]
        l1 = self.solution.test_make_list(input_l1)
        l2 = self.solution.test_make_list(input_l2)
        merged = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(self.solution.test_show_list(merged), [1, 1, 3, 4])

    def test_3(self):
        input_l1 = [1]
        input_l2 = []
        l1 = self.solution.test_make_list(input_l1)
        l2 = self.solution.test_make_list(input_l2)
        merged = self.solution.mergeTwoLists(l1, l2)
        self.assertEqual(self.solution.test_show_list(merged), [1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
