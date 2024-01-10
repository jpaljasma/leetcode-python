from typing import List
"""
https://leetcode.com/problems/majority-element/description/

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

class Solution:

    def majorityElement(self, nums: List[int]) -> int:
        """ Boyer-Moore majority vote algorithm is most optimal approach """
        count = 1
        candidate = nums[0]
        
        for i in range(1, len(nums)):
            current = nums[i]
            
            if count == 0:
                candidate = current

            # fancy if then else inline
            count += 1 if(candidate == current) else -1
            

        return candidate


    """ Fastest in Python is actually finding a median, but it only works with TWO candidates """
    # a = sorted(nums)
    # return a[len(nums)//2]

    """ Using a map to count -- works """    
    #     m = {}
    #     target = len(nums) / 2
    #     for i in range(len(nums)):
    #         num = nums[i]
    #         if num in m:
    #             m[num] += 1
    #             if m[num] > target:
    #                 return num
    #         else:
    #             m[num] = 1
    #     return 0

print(Solution().majorityElement([2,2,1,1,3,3,0,0,3,3,1,2,3,2]))
print(Solution().majorityElement([2,2,1,1,1,2,2]))