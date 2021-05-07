from typing import List
import unittest

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val='#', next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head_node = curr_node = ListNode()
        carry = rem = 0  # like 9+3=12, save 1 in carry and 2 in rem
        while l1.val != '#' or l2.val != '#' or carry:  # iterate over input digits in linked lists
            sum = 0
            if l1.val != '#':
                sum += l1.val
                l1 = l1.next
            if l2.val != '#':
                sum += l2.val
                l2 = l2.next
            sum += carry # add carry from previous step
            carry, rem = divmod(sum, 10)
            #print(f"rem={rem} carry={carry} sum={sum}")
            curr_node.next = ListNode(rem)
            curr_node = curr_node.next

        return head_node.next

    # helper methods
    def make_list(self, list: list) -> ListNode:
        head_node = ListNode()
        for i in reversed(list):
            curr_node = ListNode(i)  # create new node
            curr_node.next = head_node  # point it to the current head
            head_node = curr_node  # move head to newly created node
        return head_node

    def show_list(self, list_node):
        result = []
        while list_node.next is not None:
            result.append(list_node.val)
            list_node = list_node.next

        # add last item to the list
        if list_node.val != '#':
            result.append(list_node.val)
        return result


class TestAddTwoNumbers(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        l1 = self.solution.make_list([2, 4, 3])
        l2 = self.solution.make_list([5, 6, 4])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.solution.show_list(result), [7, 0, 8])

    def test_2(self):
        l1 = self.solution.make_list([0])
        l2 = self.solution.make_list([0])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.solution.show_list(result), [0])

    def test_3(self):
        l1 = self.solution.make_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.solution.make_list([9, 9, 9, 9])
        result = self.solution.addTwoNumbers(l1, l2)
        self.assertEqual(self.solution.show_list(result), [8, 9, 9, 9, 0, 0, 0, 1])


if __name__ == "__main__":
    unittest.main()
