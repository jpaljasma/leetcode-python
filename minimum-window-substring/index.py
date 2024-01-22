import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hash_pat = {}
        hash_str = {}

        # if s == t:
        #     return s

        if len(t) > len(s):
            return ""

        # count characters in hash pattern
        for c in t:
            if c not in hash_pat:
                hash_pat[c] = 0
            hash_pat[c] += 1

        # left boundary of our window
        left = 0

        # length of the pattern, character matching score
        count = 0

        # should be set to largest int
        min_len = sys.maxsize

        # starting position (index) of substring of the best window
        start_index = -1

        # increment current element number of occurances in the string hash map
        # loop index acts as a right pointer
        for right in range(0, len(s)):
            c = s[right]

            # count characters in string
            if c not in hash_str:
                hash_str[c] = 0
            hash_str[c] += 1

            # if character is not in pattern, add it but set to zero
            if c not in hash_pat:
                hash_pat[c] = 0

            # keep incrementing the count if string hash is less then pattern hash
            if hash_pat[c] > 0 and hash_str[c] <= hash_pat[c]:
                count += 1

            if count == len(t):
                if s[left] not in hash_str:
                    hash_str[s[right]] = 0

                if s[left] not in hash_pat:
                    hash_pat[s[right]] = 0

                # can we minimize the window range from left side
                while hash_str[s[left]] > hash_pat[s[left]] or hash_pat[s[left]] == 0:
                    if hash_str[s[left]] > hash_pat[s[left]]:
                        hash_str[s[left]] -= 1

                    # increment the left pointer
                    left += 1

                window_len = right - left + 1
                if min_len > window_len:
                    min_len = window_len
                    start_index = left

                if len(t) == window_len:
                    print("Length match")
                    return s[start_index : start_index + min_len]

        print("Start index: %d, min len: %d" % (start_index, min_len))

        if start_index == -1:
            return ""

        return s[start_index : start_index + min_len]
