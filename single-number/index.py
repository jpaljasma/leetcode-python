from typing import List

"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
        
Input: nums = [4,1,2,1,2]
Output: 4

https://leetcode.com/problems/single-number/description/
"""

class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        """
        We're going to XOR the numbers one by one
        0 XOR 8 XOR 8 = 0
        Time complexity: O(N) - a single loop
        Space complexity: O(1) - a single number
        """
        final = 0
        for num in nums:
            final ^= num
        return final
    
    def singleNumberLinear(self, nums: List[int]) -> int:
        """
        Great, linear implementation, but there's a faster way using XOR
        """
        # use dictionary comprehension to set init values to 0
        found = {key: 0 for key in nums}
        for i in range(len(nums)):
            found[nums[i]] += 1

        num_found = -1
        
        for k in found:
            if found[k] < 2:
                num_found = int(k)
                break
        return num_found
    
print(Solution().singleNumber([4,1,2,1,2]))