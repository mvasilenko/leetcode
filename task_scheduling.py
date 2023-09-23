import math
import unittest

# The data analysts of Hackerland want to schedule some long-running tasks on remote servers optimally to minimize the cost of running them locally. The analysts have two servers, a paid one and a free one. The free server can be used only if
# the paid server is occupied.
# The ith task is expected to take timeli] units of time to complete and the cost of procasing the task on the paid server is cost[i]. The task can be run on the free server only if some task is already running on the paid server. The cost of the free
# server is 0 and it can process any task in 1 unit of time.
# Find the minimum cost to complete all the tasks if tasks are scheduled optimally.
# case 1:
# cost = [1, 1, 3, 4]
# time = [3, 1, 2, 3]
# ---------------------> time
#       0   1   2   3   4  5
# paid (1) (1) (1) ( )
# free (4) (3) (2) ( )
# tasks (1) and (2) are placed on the paid server
# tasks (3) and (4) are placed on the free server
# cost = 1
# ---------------------
# case 4:
# cost = [2, 3, 4, 5]
# time = [1, 1, 5, 3]
# ---------------------> time
#       0   1   2   3   4  5
# paid (1) (2) (1) ( )
# free (4) (3) (2) ( )
# tasks (1) and (2) are placed on the paid server
# tasks (3) and (4) are placed on the free server
# cost = 5
# ---------------------
# case 5:
# cost = [5, 6, 7, 8, 8, 10]
# time = [1, 1, 1, 1, 1, 10]
# ---------------------> time
#       0   1   2   3   4  5
# paid (1) (2) (3) ( )
# free (6) (5) (4) ( )
# tasks ( ) and ( ) are placed on the paid server
# tasks ( ) and ( ) are placed on the free server
# cost = 5

class Solution:
    def getMinCost(self, cost, time):
        res = 0
        print(f"{cost=} {time=}")
        # sort by cost, then time
        zipped = sorted(list(zip(time, cost)), key=lambda x: x[1])
        print(zipped)
        l, r = 0, len(zipped)-1
        while l <= r:
            t = zipped[l][0]  # time
            c = zipped[l][1]  # cost
            res += c  # increment cost by current cost
            # we are jumping by tasks, not time
            r -= t  # decrement time by current time
            l += 1  # free server process next task
        return res


class TestGetMinCost(unittest.TestCase):
    solution = Solution()


    def test_1(self):
        self.assertEqual(self.solution.getMinCost([1, 1, 3, 4], [3, 1, 2, 3]),1)


    def test_2(self):
        self.assertEqual(self.solution.getMinCost([1, 2, 3, 2], [1, 2, 3, 2]),3)


    def test_3(self):
        self.assertEqual(self.solution.getMinCost([2, 3, 4, 2], [1, 1, 1, 1]),4)


    def test_4(self):
        self.assertEqual(self.solution.getMinCost([2, 3, 4, 5], [1, 1, 5, 3]), 5)


    def test_5(self):
        self.assertEqual(self.solution.getMinCost([5, 6, 7, 8, 8, 10], [1, 1, 1, 1, 1, 10]), 18)


    def test_6(self):
        self.assertEqual(self.solution.getMinCost([10, 10, 10, 10, 10, 20, 20, 20], [3, 3, 3, 3, 3, 6, 6, 6]), 20)


    def test_7(self):
        self.assertEqual(self.solution.getMinCost([5, 6, 7, 8, 1000000], [1, 1, 1, 1, 1000]), 18)

if __name__ == '__main__':
    unittest.main()
