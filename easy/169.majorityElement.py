"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

https://leetcode.com/problems/majority-element/
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        count = 0
        majority = 0
        
        for i in range(len(nums)):
            
            if count == 0:
                majority = nums[i]
                count += 1
            
            elif nums[i] == majority:
                count += 1
                
            elif nums[i] != majority:
                count -= 1
        
        return majority