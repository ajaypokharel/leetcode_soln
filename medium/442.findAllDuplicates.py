"""
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant extra space.

https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:        
          
        res = []
        
        for i in range(len(nums)):
            while i != nums[i] - 1 and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        return [nums[i] for i in range(len(nums)) if i != nums[i] - 1]
                