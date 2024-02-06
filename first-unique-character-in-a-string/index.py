import unittest


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s is None or len(s) == 0:
            return -1
        s_len = len(s)
        if 1 == s_len:
            return 0

        seen = {}
        for i in range(len(s)):
            c = s[i]
            if not seen.get(c):
                seen[c] = [i]
            else:
                seen[c].append(i)

        for v in seen.values():
            if len(v) == 1:
                return v[0]

        return -1


class TestFirstUniqueChar(unittest.TestCase):
    def test_correct_index(self):
        s = Solution()
        self.assertEqual(s.firstUniqChar("leetcode"), 0)
        self.assertEqual(s.firstUniqChar("dddccdbba"), 8)
        self.assertEqual(s.firstUniqChar("aa"), -1)

    def test_edge_cases(self):
        s = Solution()
        self.assertEqual(s.firstUniqChar(""), -1)
        self.assertEqual(s.firstUniqChar(None), -1)


if __name__ == "__main__":
    unittest.main()
