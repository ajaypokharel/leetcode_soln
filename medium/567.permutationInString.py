"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

https://leetcode.com/problems/permutation-in-string/
"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ctr1 = Counter(s1)
        ctr2 = Counter(s2[:len(s1)])
            
        i = 0; j = len(s1)
        
        while j < len(s2):
            if ctr2 == ctr1:
                return True
            ctr2[s2[i]] -= 1

            if ctr2[s2[i]] < 1:
                ctr2.pop(s2[i]); 
            
            ctr2[s2[j]] = ctr2.get(s2[j], 0) + 1
            i += 1
            j += 1
            
        return ctr2 == ctr1
                
            
        