"""
Given a string s, find the length of the longest substring without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        count = 0
        count_list = list()
        
        if len(s) < 1:
            return 0
        
        for i in range(len(s)):
            if not s[i] in sub:
                sub.append(s[i])
                count += 1
                count_list.append(count)
                
            else:
                j = sub.index(s[i])
                sub = sub[j+1:]
                sub.append(s[i])
                count = len(sub)
                count_list.append(count)
        
        return (max(count_list))