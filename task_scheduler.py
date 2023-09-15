# forumula
# calculate how many f of most_common values=X from tasks list
# f
# res = (n-1)*(f-1)+X
import unittest
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = Counter(tasks)
        print(cnt.most_common())
        f = cnt.most_common()[0][1]

        x = 0
        x_max = cnt.most_common()[0][1]
        for i in cnt:
            # print(f"{i=} {cnt[i]=}")
            if cnt[i] == x_max:
                x += 1
        # print(f"{f=} {x=} {cnt=} {x_max=}")
        return max((n+1)*(f-1)+x, len(tasks))


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.leastInterval(["A", "A", "A", "B", "B", "B"], 2), 8)

    def test_2(self):
        self.assertEqual(self.solution.leastInterval(["A", "A", "A", "B", "B", "B"], 0), 6)

    def test_3(self):
        self.assertEqual(self.solution.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2), 16)


if __name__ == "__main__":
    unittest.main()
