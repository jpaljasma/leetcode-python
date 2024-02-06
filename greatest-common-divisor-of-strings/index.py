import unittest

"""
For two strings `s` and `t`, we say "t divides s" if and only if `s = t + ... + t` (i.e., t is concatenated with itself one or more times).

Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`.

See https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # it's a match
        if str1 == str2:
            return str1

        if len(str1) < len(str2):
            # swap so str1 is always longer string
            str1, str2 = str2, str1

        # return nothing is strings don't share the same prefix
        if (str1[: len(str2)]) != str2:
            return ""

        # remove common prefix from longer string and try recursively
        return self.gcdOfStrings(str1[len(str2) :], str2)


class TestGcdString(unittest.TestCase):
    def test_correct_gcd(self):
        s = Solution()
        self.assertEqual(s.gcdOfStrings("ABABAB", "ABAB"), "AB")
        self.assertEqual(s.gcdOfStrings("ABBA", "CAB"), "")
        self.assertEqual(s.gcdOfStrings("LEET", "TEEL"), "")
        self.assertEqual(s.gcdOfStrings("FEEL", "EEL"), "")
        self.assertEqual(s.gcdOfStrings("ABCABC", "ABC"), "ABC")
        self.assertEqual(s.gcdOfStrings("ABCBAABCBA", "ABC"), "")


if __name__ == "__main__":
    unittest.main()
