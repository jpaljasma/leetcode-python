from typing import List
"""
Amazon Array Question: Longest Substring Without Repeating Characters (Medium)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Given a string s, find the length of the longest substring without repeating characters.
        """
        
        """
        We should be using sliding window technique with hash mapping, L and R pointers.
        R is for searching, or adding characters
        Keep track of indicies of the characters, i.e. "acdeca" {
            a: 0,
            c: 1
        }
        """
        n_len = len(s)
        
        if n_len <= 1:
            return n_len
        
        m = {}
        ans = 0 
        left = 0
        right = 0
        
        for i in range(n_len):
            char = s[i]
            if char in m:
                left = max(left, m[char] + 1)
            right += 1
            m[char] = i # update our map that current character updates its latest position
            ans = max(right - left, ans)

        return ans

        """
        Brute force version - passes but sloooow
        """
        # if len(s) <= 1:
        #     return len(s)
        
        # i = 0
        # word_pointer = 0
        # n_len = len(s)
        # max_len = 0
        # w = {}

        # while i < n_len:
        #     # append the character if not exist
        #     char = s[i]
        #     if char not in w.keys():
        #         w[char] = 1
        #         i += 1
        #     else:
        #         # character found, reset
        #         if len(w.keys()) > max_len:
        #             max_len = len(w.keys())
        #         w = {}
        #         word_pointer += 1
        #         i = word_pointer                
        
        # if len(w.keys()) > max_len:
        #     max_len = len(w.keys())

        # return max_len
    
print(Solution().lengthOfLongestSubstring("abcabc"))