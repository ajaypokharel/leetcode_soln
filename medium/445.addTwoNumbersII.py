"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

https://leetcode.com/problems/add-two-numbers-ii/
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1, sum2 = 0, 0
        
        while l1:
            sum1 = sum1*10 + l1.val
            l1 = l1.next
            
        while l2:
            sum2 = sum2*10 + l2.val
            l2 = l2.next
            
        total = sum1 + sum2
        
        current = result = ListNode(0)
        
        for i in str(total):
            current.next = ListNode(int(i))
            current = current.next
            
        return result.next
    