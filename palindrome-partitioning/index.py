from typing import List


class Solution:
    def is_palindrome(self, segment: str) -> bool:
        left = 0
        right = len(segment) - 1
        while left < right:
            if segment[left] != segment[right]:
                return False
            left += 1
            right -= 1

        return True

    def _solution(self, s: str, partition: List[str], result: List[List[str]]):
        if len(s) == 0:
            result.append(partition[:])
            return

        for i in range(1, len(s) + 1):
            segment = s[0:i]
            if self.is_palindrome(segment):
                partition.append(segment[:])
                # recursively call with the remainder part
                self._solution(s[i:], partition, result)
                partition.pop()

    """
    A partition is a collection of substrings that, when added together, gives us the original string
     - a Palindrome partition simply means each substring is also a palindrome
    """

    def partition(self, s: str) -> List[List[str]]:
        if 0 == len(s):
            return []
        if 1 == len(s):
            return [[s]]

        result = []
        self._solution(s, [], result)
        return result


if __name__ == "__main__":
    s = Solution()
    # will return [['a', 'a', 'b'], ['aa', 'b']]
    print(s.partition("aab"))
