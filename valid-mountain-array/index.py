from typing import List
"""
Google Array Question: Valid Mountain Array (Easy)
"""
class Solution:
    """See https://leetcode.com/problems/valid-mountain-array/description/"""
    def validMountainArray(self, arr: List[int]) -> bool:

        # passes, 151ms runtime, 18.68 MB memory, beats 98.51% in runtime, 25.26% with memory in PY
        # space complexity O(1), we use only couple of variables
        # time complexity O(n), where n is length of the input list
        
        n_len = len(arr)

        # range checks
        if n_len < 3:
            return False
        elif arr[1] <= arr [0]:
            # immediate flat or fall
            return False

        raising = True
        true_mountain = False
        
        for i in range(1, n_len):
            if arr[i] == arr[i-1]:
                # edge case, line is horizontal
                true_mountain = False
                break
            elif raising and arr[i] < arr[i-1]:
               # start falling
               raising = False
               true_mountain = True
            elif not raising and arr[i] > arr[i-1]:
              # was suppose to fall, but changed direction
              true_mountain = False
              break
        return true_mountain
    
# Test Runner
class ValidMountainAreaTest:
    def run(self, arr: List[int], expected: int) -> bool:
        """Runs the test case against Solution()

        Arguments:
        arr (List[int]): The list of heights i.e. [1,2,3,4,5]
        expected (bool): The expected bool result of this test case, either True or False

        Returns:
        bool: True if test passes

        Raises:
        Exception: If the unit test does not pass
        """        
        s = Solution()
        result = s.validMountainArray(arr)
        if result == expected:
            print(f"Valid area is {result} for input {arr}")
            return True
        else:
            sx = f"Test failed, {result} != {expected} in {arr}"
            raise Exception(sx)
        
if __name__ == '__main__':
    test = ValidMountainAreaTest()
    test.run([0,1,2,3,4,5,6,7,8,9], False)
    test.run([2,1], False)
    test.run([], False)
    test.run([1], False)
    test.run([3,5,5], False)
    test.run([0,3,2,1], True)
    