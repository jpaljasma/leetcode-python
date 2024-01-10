from typing import List


class Solution:
    """
    See https://leetcode.com/problems/missing-number/description/
    """

    def missingNumber(self, nums: List[int]) -> int:
        """
        Most optimal is gauss formula (if numbers are really in sequence)
        2s = n * (n + 1)

        s = (n * (n + 1)) / 2
        s = n_len * (n_len + 1) / 2
        s in this case is the indtendedSum
        """
        # find max and length
        n_len = len(nums)

        # use gauss formula for intended sum
        a_sum = n_len * (n_len + 1) // 2

        # calculate actual sum
        b_sum = 0
        for i in range(n_len):
            b_sum += nums[i]

        # result is the difference
        return a_sum - b_sum


print(Solution().missingNumber([3, 0, 1]))
