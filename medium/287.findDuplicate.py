"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
https://leetcode.com/problems/find-the-duplicate-number/
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        rabbit, turtle = 0, 0
        
        while True:
            turtle = nums[turtle]
            rabbit = nums[nums[rabbit]]
            
            if rabbit == turtle:
                break
        
        turtle_2 = 0
        
        while True:
            
            turtle = nums[turtle]
            turtle_2 = nums[turtle_2]
            
            if turtle == turtle_2:
                break
        
        return turtle