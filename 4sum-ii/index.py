from typing import List

"""

https://leetcode.com/problems/4sum-ii/description/

Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

"""
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        """
        Time complexity is O(N^4) and will never work well
        """
        m = {}

        for x in nums1:
            for y in nums3:
                sum = (x + y)
                if sum not in m:
                    m[sum] = 0
                
                m[sum] += 1
        
        ans = 0

        for x in nums2:
            for y in nums4:
                target = -(x + y)
                if target in m:
                    ans += m[target]

        return ans
    

print(Solution().fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))