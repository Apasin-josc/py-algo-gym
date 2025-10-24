"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true


Example 2:
Input: s = "jar", t = "jam"
Output: false
"""
from collections import Counter
class Solution:
    def is_anagram(self, s : str, t : str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_freq = {}
        t_freq = {}
        for c in s:
            s_freq[c] = s_freq.get(c,0) + 1
        
        for c in t:
            t_freq[c] = t_freq.get(c,0) + 1
        
        if s_freq.items() == t_freq.items():
            return True
        else:
            return False
                  

sol = Solution()
print(sol.is_anagram("racecar", "carrace"))
print(sol.is_anagram("jar", "jam"))
