# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

bad_version = 0


def isBadVersion(version: int) -> bool:
    print(f"isBadVersion({version})")
    return version >= bad_version


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        found_bad = -1
        if n == 1:
            b = isBadVersion(1)
            if True == b:
                return 1
        else:
            # use binary search to find the most recent bad version
            # Time complexity: O(log(n)) because of binary search
            # Space complexity: O(1) as we use barely no data
            while l <= r:
                m = (l + r) // 2
                b = isBadVersion(m)
                if True == b:
                    print(f"Version {m} is bad")
                    found_bad = m
                    # move right pointer to keep searching
                    r = m - 1
                else:
                    # keep searching from right
                    l = m + 1
        return found_bad


bad_version = 19
print(Solution().firstBadVersion(11324))

bad_version = 2
print(Solution().firstBadVersion(2))
