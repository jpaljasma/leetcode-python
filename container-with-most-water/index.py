from typing import List

"""
Microsoft Array Question: Container With Most Water (Medium)
"""


class Solution:
    """
    See https://leetcode.com/problems/container-with-most-water/description/
    """

    def maxArea(self, height: List[int]) -> int:
        """Calculates maximum area of container with most water

        Arguments:
        height (List[int]): The list of heights i.e. [1,2,3,4,5]

        Returns:
        int: Max area of container
        """
        # passes, 545ms runtime, 30.07 memory, beats 87.14% in runtime, 18.49% with memory in PY
        # space complexity O(1), we use only couple of variables
        # time complexity O(n), where n is length of the input list
        max_area, left, right = 0, 0, len(height) - 1
        while left < right:
            max_area = max(max_area, (right - left) *
                           min(height[left], height[right]))
            # determine which pointer to move
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return max_area


# Test Runner
class MaxAreaTest:
    def run(self, height: List[int], expected: int) -> bool:
        """Runs the test case against Solution()

        Arguments:
        height (List[int]): The list of heights i.e. [1,2,3,4,5]
        expected (int): The expected result of this test case

        Returns:
        bool: True if test passes

        Raises:
        Exception: If the unit test does not pass
        """
        s = Solution()
        result = s.maxArea(height)
        if result == expected:
            print(f"Max area is {result} for input {height}")
            return True
        else:
            sx = f"Test failed, {result} != {expected}"
            raise Exception(sx)


# Run the unit tester
if __name__ == '__main__':
    test = MaxAreaTest()
    test.run([1, 8, 6, 2, 5, 4, 8, 3, 7], 49)
    test.run([1, 2, 3, 4, 5], 6)
    test.run([1, 1], 1)
