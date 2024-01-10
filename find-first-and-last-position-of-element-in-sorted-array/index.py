from typing import List

"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity. (like binary search through phone book)
https://stackoverflow.com/questions/2307283/what-does-olog-n-mean-exactly 
"""


class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # find all occurrences using count() and index()
        # pretty fast, 72ms
        # found = nums.count(target)
        # if 0 == found:
        #     return [-1,-1]

        # first_index = nums.index(target)
        # last_index = first_index + found - 1

        # return [first_index, last_index]

        # let's use binary search to quickly find item in a sorted set
        def binarysearch(x):
            l = 0
            r = len(nums)

            while l < r:
                # find midpoint
                mid = (l + r) // 2
                if nums[mid] < x:
                    # move left to midpoint + 1
                    l = mid + 1
                else:
                    # move right to midpoint
                    r = mid
            # return the leftmost index
            return l

        # sorted list means all we have to find first number that's larger than our target
        def findlast(x, from_index):
            if from_index < 0:
                return -1

            r = from_index
            for i in range(from_index, len(nums)):
                if nums[i] > x:
                    break
                r = i
            return r

        """
        Time Complexity: O(log(n))
        Space Complexity: O(1)
        """
        first = binarysearch(target)

        if first == len(nums) or nums[first] != target:
            return [-1, -1]
        else:
            return [first, binarysearch(target + 1) - 1]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([5, 7, 7, 8, 9, 11, 13, 15], 9))
