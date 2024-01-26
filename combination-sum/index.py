from typing import List

"""
https://leetcode.com/problems/combination-sum/description/

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

"""


class Solution:
    def _solution(
        self,
        candidates: List[int],
        ans: List[int],
        cur: List[int],
        target: int,
        index: int,
        tot: int,
    ):
        if tot == target:
            # we have found valid combination, append a copy of it in the answer
            ans.append(cur[:])
        elif tot < target:
            for i in range(index, len(candidates)):
                # backtracking steps
                # 1. add candidates to our current
                cur.append(candidates[i])
                # 2. explore possibility whether the candidate should be added
                self._solution(candidates, ans, cur, target, i, tot + candidates[i])
                # 3. pop it out and try next
                cur.pop()
        return ans

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self._solution(candidates, [], [], target, 0, 0)


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 6], 8))
