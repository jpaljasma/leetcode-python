from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Runtime: 120ms, beats 98.35% of users with Python3
        Memory: 18.86 MB, beats 15.61% of users with Python3

        Time complexity: O(N+m) due to two loops - one for every single element, and loop for number of zeroes 
        Space complexity: O(1) we're just moving things around and have two numbers to keep track
        """
        n_len = len(nums)
        j_ptr = 0
        for i in range(n_len):
            if nums[i] != 0:
                nums[j_ptr] = nums[i]
                # increase number position counter
                j_ptr += 1
        # set numbers from the counter to zeroes
        for i in range(j_ptr, n_len):
            nums[i] = 0


arr = [0, 1, 0, 3, 12]
Solution().moveZeroes(arr)
print(arr)

arr = [0, 0, 0, 0]
Solution().moveZeroes(arr)
print(arr)
