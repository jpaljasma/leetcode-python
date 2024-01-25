from typing import List


class Solution:
    """
    Backtracking (recursive) approach
    """

    def solution(self, nums: List[int], ans, cur, index):
        if index > len(nums):
            return

        # append a copy to our answer list
        ans.append(cur[:])

        for i in range(index, len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                self.solution(nums, ans, cur, i)
                cur.pop()
        return

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums is None or nums == []:
            return []

        ans = []
        cur = []
        self.solution(nums, ans, cur, 0)
        return ans

    def subsets_cascading(self, nums: List[int]) -> List[List[int]]:
        """
        The number of possible subsets is 2 ^ N
        (because we can choose whether to take it or not)
        No duplicates! Subsets [2,1] and [1,2] are duplicates
        """
        # n = len(nums)
        # print("Number of possible subsets for N=%d is %s" % (n, 2**n))

        """
        Cascading - pick a number and append it to already existing subsets we've generated
        """

        ans = [[]]
        # loop through each number
        for num in nums:
            # cascade through existing elements
            for j in range(len(ans)):
                row = ans[j]
                # add the number to the row and append to the list
                ans.append(row + [num])

        return ans


if __name__ == "__main__":
    s = Solution()
    # Backtracking:     [1,2] => [[], [1], [2, 2], [2]]
    # Cascading:        [1,2] => [[], [1], [2], [1, 2]]
    print(s.subsets([1, 2]))
    print(s.subsets_cascading([1, 2]))
