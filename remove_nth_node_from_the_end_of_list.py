import unittest


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # create dummy head
        dummy_head = ListNode(0)
        dummy_head.next = head
        ptr = head
        # calculate list length
        list_length = 0
        while ptr.next:
            list_length += 1
            ptr = ptr.next
        # search and remove n-th element from the end
        i = 0
        ptr = dummy_head
        while i <= list_length - n:
            ptr = ptr.next
            i += 1
        ptr.next = ptr.next.next
        return dummy_head.next

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


class TestSolution(unittest.TestCase):
    solution = Solution

    def test_1(self):
        input = self.solution.test_make_list(self, [1, 2, 3, 4, 5])
        result = self.solution.removeNthFromEnd(self, input, 2)
        self.assertEqual(self.solution.test_show_list(self, result), [1, 2, 3, 5])

    def test_2(self):
        input = self.solution.test_make_list(self, [1])
        result = self.solution.removeNthFromEnd(self, input, 1)
        self.assertEqual(self.solution.test_show_list(self, result), [])

    def test_3(self):
        input = self.solution.test_make_list(self, [1, 2])
        result = self.solution.removeNthFromEnd(self, input, 1)
        self.assertEqual(self.solution.test_show_list(self, result), [1])


if __name__ == "__main__":
    unittest.main()
