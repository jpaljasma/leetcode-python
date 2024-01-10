from typing import List

"""
https://leetcode.com/problems/contains-duplicate/description/

"""


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _seen = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in _seen:
                return True
            _seen[num] += 1
        return False
