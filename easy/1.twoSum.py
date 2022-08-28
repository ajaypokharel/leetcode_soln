"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""



from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_1 = {}

        for i in range(len(nums)):
            
            if nums[i] in dict_1:
                return [i, dict_1[nums[i]]]
            else:
                dict_1[target - nums[i]] = i
