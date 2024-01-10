from typing import List
"""
Google Array Question: Boats to Save People (Medium)
"""


class Solution:
    """See https://leetcode.com/problems/boats-to-save-people/description/"""

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        You are given an array people where people[i] is the weight of the ith person,
        and an infinite number of boats where each boat can carry a maximum weight of limit.

        Each boat carries at most **two** people at the same time, provided the sum of the weight of those people is at most limit.
        Return the minimum number of boats to carry every given person.
        """

        """
        Runtime: 352ms, beats 93.94% of users with Python3
        Memory: 24.27 MB, beats 14.62% of users with Python3

        Time complexity: O(N Log(N)) due the fact we sort input. N Log(N) is the worst case scenario
        Space complexity: O(N) - because people.sort() uses internally has O(N) space compexity
        """
        people.sort(reverse=True)
        left, right, boats = 0, 0, 0
        right = len(people) - 1

        while left <= right:
            boats += 1
            if left == right:
                # last person on a boat
                break

            # see if we can take rightmost person?
            if people[left] + people[right] <= limit:
                # we can put two people together on the boat
                right -= 1

            # we definitely will take leftmost person
            left += 1

        return boats

# Test Runner


class ValidNumRescueBoatsTest:
    def run(self, people: List[int], limit: int, expected: int) -> bool:
        """Runs the test case against Solution()

        Arguments:
        people (List[int]): The weights of people [1,2,3,4,5]
        limit (int): maximum boat weight
        expected (bool): The expected bool result of this test case, either True or False

        Returns:
        bool: True if test passes

        Raises:
        Exception: If the unit test does not pass
        """
        s = Solution()
        result = s.numRescueBoats(people, limit)
        if result == expected:
            print(f"Valid number of boats is {result} for input {people}")
            return True
        else:
            sx = f"Test failed, {result} != {expected} in {people}"
            raise Exception(sx)


if __name__ == '__main__':
    test = ValidNumRescueBoatsTest()
    test.run([3, 2, 1, 2], 4, 2)
    test.run([3, 8, 7, 1, 4], 9, 3)
    test.run([1, 1, 1, 1], 5, 2)
    test.run([1, 2], 3, 1)
    test.run([3, 2, 2, 1], 3, 3)
    test.run([3, 5, 3, 4], 5, 4)
