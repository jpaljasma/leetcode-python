from typing import List

"""

https://leetcode.com/problems/two-sum/description/

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

"""


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _track = {}

        for i in range(len(nums)):
            num = nums[i]
            remainder = target - num
            if remainder in _track:
                return [_track[remainder], i]

            _track[num] = i

        # while i < n-1 and not found:
        # #for i in range(0, n-1):
        #     left = nums[i]

        #     # if left > target:
        #     #     i += 1
        #     #     continue

        #     for j in range(n-1, i, -1):
        #         # print("I, J =", i, ",", j)
        #         right = nums[j]

        #         if target == left + right:
        #             # we have match
        #             result = [i, j]
        #             found = True
        #             break
        #         # elif right > target:
        #         #     n -= 1
        #         #     continue

        #     i += 1

        # return result


print(Solution().twoSum([3, 2, 4], 6))

print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([-3, 4, 3, 90], 0))

print(Solution().twoSum([2, 5, 5, 11], 10))
print(Solution().twoSum([9, 8, 3, 1], 4))
print(Solution().twoSum([0, 4, 3, 0], 0))
print(Solution().twoSum([2, 7, 11, 15], 9))
