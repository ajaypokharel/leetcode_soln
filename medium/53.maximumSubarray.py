"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

https://leetcode.com/problems/maximum-subarray/
"""
from typing import List

class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        
# DYNAMIC PROGRAMMING APPROACH
#         memo = [nums[0]]
        
#         for i in range(1, len(nums)):
#             if memo[i - 1] + nums[i] > nums[i] + nums[i-1]:
#                 memo.append(memo[i-1] + nums[i])
#             else:
#                 memo.append(nums[i] + nums[i-1])
        
#         return max(max(memo), max(nums))

#  EASIER Prefix Sum Approach
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)