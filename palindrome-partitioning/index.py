from typing import List


class Solution:
    def _solution(self, s: str, ans=List[List[str]]):
        return

    """
    A partition is a collection of substrings that, when added together, gives us the original string
    """
    def partition(self, s: str) -> List[List[str]]:
        if 0 == len(s):
            return []
        if 1 == len(s):
            return [[s]]

        ans = []
        self._solution(s, ans)
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))
