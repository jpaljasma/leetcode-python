from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        d = deque()
        par = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        rap = {
            ")": "(",
            "}": "{",
            "]": "[",
        }

        for char in s:
            if char in par:
                d.append(char)
            elif char in rap:
                if len(d) == 0:
                    return False
                comp = d.pop()
                if comp != rap[char]:
                    return False

        return 0 == len(d)


if __name__ == "__main__":
    s = Solution()
    print(s.isValid("{( test ])}"))                 # False
    print(s.isValid("{(a + (b-c)) == [d,e] }"))     # True
