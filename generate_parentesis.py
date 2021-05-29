import unittest
from typing import List


class Solution():
    def generateParenthesis(self, n: int) -> List[str]:
        """
        1 -> ()
        2 -> (()), ()()
        3 -> ((())), (()()), (())(), ()(()), ()()()
        parentesis length should be n*2, i.e. for n=3 we should generate ()()() or ((())) etc

        what we can do based on remaining parentesis count
        3L 3R -> can put 1L, 2L 3R will remain, call backtracking(L-1, R)
        3L 3R -> can't put 1R, it will be unbalanced,

        2L 3R -> can put 1L, 1L 3R will remain, call backtracking(L-1, R)
        2L 3R -> can put 1R, 2L 2R will remain, call backtracking(L, R-1)

        1L 3R -> can put 1L, 0L 3R will remain, call backtracking(L-1, R)
        0L 3R -> can put 1R, 0L 2R will remain, call backtracking(L, R-1)

        1L 1R -> can't put 1R, it will be unbalanced
        1L 1R -> can put 1L, 0L 1R will remain, call backtracking(L-1, R)

        0L 1R - can't put 1L
        0L 1R - can put 1R

        0L 0R - join, return
        in general, we should:
        recurse(L-1,R) when L < R and L>0
        recurse(L,R-1) when L < R and R>0

        """

        result = []

        def backtrack(S: str, n: int, left=n, right=n):
            # check if all combinations were found
            #print(f"S={S}, left={left} right={right}")
            if len(S) == n * 2:
                result.append(''.join(S))
                return
            # if
            if left <= right and left > 0:
                S.append("(")
                backtrack(S, n, left-1, right)
                S.pop()
            if left <= right and right > 0:
                S.append(")")
                backtrack(S, n, left, right-1)
                S.pop()

        backtrack([], n)
        return result


class TestSolution(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        self.assertEqual(self.solution.generateParenthesis(1), ["()"])

    def test_2(self):
        self.assertEqual(self.solution.generateParenthesis(2), ["(())", "()()"])

    def test_3(self):
        self.assertEqual(self.solution.generateParenthesis(3), ["((()))", "(()())", "(())()", "()(())", "()()()"])


if __name__ == "__main__":
    unittest.main()
