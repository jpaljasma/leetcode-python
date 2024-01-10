from typing import List

"""
https://leetcode.com/problems/group-anagrams/description/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if 1 == len(strs):
            return [strs]
        
        xormap = {}
        for word in strs:
            xorr = ''.join(sorted(word))
            
            if xorr in xormap:
                xormap[xorr].append(word)
            else:
                xormap[xorr] = [word]
        
        return list(xormap.values())


print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))